"""Building energy dashboard. Run with python app.py or gunicorn app:server."""
from pathlib import Path
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output


def build_dashboard(data):
    """Create a new app from the original UCI table without mutating it."""
    energy = data.copy(deep=True)
    required = [f'X{i}' for i in range(1, 9)] + ['Y1', 'Y2']
    if energy[required].isna().any().any():
        raise ValueError('The fixed source should contain no missing values.')
    energy = energy.rename(columns={'X5': 'height', 'X7': 'glazing',
                                    'Y1': 'heating', 'Y2': 'cooling'})
    energy['record'] = np.arange(1, len(energy) + 1)
    energy['glazing_pct'] = energy['glazing'] * 100
    heights = [3.5, 7.0]
    glazing_levels = [0, 10, 25, 40]
    colors = {3.5: '#087f8c', 7.0: '#c56822'}
    bins = np.arange(0, 51, 5)
    full_cooling = energy.groupby(['height', 'glazing_pct'])['cooling'].mean()
    app = Dash(__name__)
    app.title = 'Building energy explorer'
    app.index_string = '''<!DOCTYPE html><html><head>{%metas%}<title>{%title%}</title>
    {%favicon%}{%css%}<style>
    body{margin:0;background:#f3f5f7;color:#183042;font-family:Arial,sans-serif}
    *{box-sizing:border-box}.shell{max-width:1360px;margin:auto;padding:32px}
    h1{font-size:36px;margin:8px 0 12px;letter-spacing:-1px}h2{font-size:20px;margin:0 0 12px}
    p{line-height:1.6}.eyebrow{color:#087f8c;font-size:12px;font-weight:700;letter-spacing:2px}
    .intro{max-width:950px}.control,.card,.notes{background:white;border:1px solid #dce4ea;border-radius:12px;padding:22px}
    .control{margin:24px 0}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}
    .card{padding:12px;min-width:0}.notes{margin-top:22px}.status{font-weight:700;margin-top:14px;color:#075a64}
    .hint{font-size:14px;color:#526477}a{color:#076d7a}.footer{font-size:13px}
    @media(max-width:850px){.grid{grid-template-columns:1fr}.shell{padding:16px}h1{font-size:28px}}
    </style></head><body>{%app_entry%}<footer>{%config%}{%scripts%}{%renderer%}</footer></body></html>'''

    def finish(fig, title, n):
        fig.update_layout(template='plotly_white', height=390,
                          title={'text': title + f'<br><sup>Selected designs: n = {n}</sup>', 'font': {'size': 18}},
                          font={'family': 'Arial', 'color': '#183042', 'size': 12},
                          margin={'l': 70, 'r': 30, 't': 85, 'b': 65},
                          legend={'orientation': 'h', 'y': 1.05, 'title': {'text': ''}})
        return fig

    def empty(title):
        fig = finish(go.Figure(), title, 0)
        fig.add_annotation(text='No designs selected. Select a building height.',
                           x=.5, y=.5, xref='paper', yref='paper', showarrow=False)
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)
        return fig

    titles = ['Heating load distribution', 'Heating load by building height',
              'Glazing and heating load', 'Average cooling load by design']

    def update(selected):
        selected = selected or []
        subset = energy.loc[energy['height'].isin(selected)].copy()
        n = len(subset)
        if not n:
            return (*[empty(t) for t in titles], '0 of 768 designs selected. No summary is available.')
        active = [h for h in heights if h in subset['height'].unique()]
        counts, _ = np.histogram(subset['heating'], bins=bins)
        distribution = go.Figure(go.Bar(
            x=((bins[:-1] + bins[1:]) / 2).tolist(), y=counts.tolist(), width=4.8,
            marker_color='#087f8c', customdata=[[int(a), int(b)] for a, b in zip(bins[:-1], bins[1:])],
            hovertemplate='Heating bin: %{customdata[0]} to %{customdata[1]}<br>Designs: %{y}<extra></extra>'))
        distribution.update_xaxes(title='Heating load (source units)', range=[0, 50], dtick=10)
        distribution.update_yaxes(title='Number of simulated designs', rangemode='tozero')
        boxes = go.Figure()
        scatter = go.Figure()
        for height in active:
            group = subset[subset['height'].eq(height)]
            label = f'{height:g} m (n={len(group)})'
            boxes.add_trace(go.Box(y=group['heating'].tolist(), name=label,
                                   marker_color=colors[height], quartilemethod='linear',
                                   boxpoints='outliers', showlegend=False))
            scatter.add_trace(go.Scatter(
                x=group['glazing_pct'].tolist(), y=group['heating'].tolist(), mode='markers', name=label,
                marker={'color': colors[height], 'opacity': .55, 'size': 7},
                customdata=group[['record', 'cooling']].values.tolist(),
                hovertemplate='Record %{customdata[0]}<br>Glazing: %{x}% of floor area<br>Heating: %{y:.2f}<br>Cooling: %{customdata[1]:.2f}<extra>%{fullData.name}</extra>'))
        boxes.update_xaxes(title='Overall building height')
        boxes.update_yaxes(title='Heating load (source units)', range=[0, 50])
        scatter.update_xaxes(title='Glazing area (% of floor area)', tickvals=glazing_levels, range=[-2, 42])
        scatter.update_yaxes(title='Heating load (source units)', range=[0, 50])
        means = subset.pivot_table(index='height', columns='glazing_pct', values='cooling', aggfunc='mean').reindex(index=active, columns=glazing_levels)
        sizes = subset.groupby(['height', 'glazing_pct']).size().unstack().reindex(index=active, columns=glazing_levels)
        labels = [[f'{means.loc[h,g]:.2f}<br>n={int(sizes.loc[h,g])}' for g in glazing_levels] for h in active]
        heatmap = go.Figure(go.Heatmap(
            x=[f'{g}%' for g in glazing_levels], y=[f'{h:g} m' for h in active],
            z=means.values.tolist(), text=labels, texttemplate='%{text}',
            customdata=sizes.values.tolist(), colorscale='Blues',
            zmin=float(full_cooling.min()), zmax=float(full_cooling.max()),
            colorbar={'title': {'text': 'Mean<br>load'}, 'thickness': 12},
            hovertemplate='Height: %{y}<br>Glazing: %{x}<br>Mean cooling: %{z:.4f}<br>n=%{customdata}<extra></extra>'))
        heatmap.update_xaxes(title='Glazing area (% of floor area)', type='category')
        heatmap.update_yaxes(title='Overall building height', type='category')
        figures = [distribution, boxes, scatter, heatmap]
        return (*[finish(f, t, n) for f, t in zip(figures, titles)],
                f'{n} of {len(energy)} designs selected. Mean heating: {subset.heating.mean():.2f}; mean cooling: {subset.cooling.mean():.2f} source units.')

    initial = update(heights)
    full_means = energy.groupby('height')[['heating','cooling']].mean()
    conclusion = (f'Across all {len(energy)} simulated designs, the 7 m group has higher mean heating '
                  f'({full_means.loc[7,"heating"]:.2f} versus {full_means.loc[3.5,"heating"]:.2f}) '
                  f'and cooling ({full_means.loc[7,"cooling"]:.2f} versus {full_means.loc[3.5,"cooling"]:.2f}) '
                  'than the 3.5 m group, in source load units. Average cooling increases across the four glazing levels within both height groups. These are associations among the simulated designs.')
    app.layout = html.Main(className='shell', children=[
        html.Div('BUILDING DESIGN / ENERGY EVIDENCE', className='eyebrow'),
        html.H1('Building energy explorer'),
        html.P('For architecture students comparing early design options: how do building height and glazing area relate to heating and cooling loads?', className='intro'),
        html.Div(className='control', children=[
            html.H2('Compare building heights'),
            dcc.Checklist(id='height-filter', options=[{'label': ' 3.5 m ', 'value': 3.5}, {'label': ' 7 m ', 'value': 7.0}],
                          value=heights, inline=True, labelStyle={'marginRight': '24px', 'cursor': 'pointer'}),
            html.P('This control updates all four figures and the summary. Select both heights for all data; clear both for an empty selection.', className='hint'),
            html.Div(id='selection-summary', children=initial[4], className='status')]),
        html.Div(className='grid', children=[html.Div(className='card', children=dcc.Graph(id=key, figure=fig, config={'displaylogo': False}))
                 for key, fig in zip(['distribution','height-box','glazing-scatter','cooling-heatmap'],initial[:4])]),
        html.Section(className='notes', children=[
            html.H2('What the full dataset shows'), html.P(conclusion),
            html.P('This conclusion uses all 768 records and does not change with the filter.', className='hint'),
            html.H2('How to read the evidence'),
            html.P('Histogram bars count designs in fixed five-unit intervals, left inclusive and right exclusive (the final bin includes 50). Box plots show medians, linear quartiles and 1.5-IQR whiskers. Each scatter mark is one design; overlapping marks can hide records. Heatmap cells show mean cooling and group n. The cooling color scale remains fixed when filtering.'),
            html.P('Load units: the UCI variable table does not specify a physical unit for Y1 or Y2. Values are shown as source units without converting them to kWh or monetary savings. Glazing percentages use floor area as their denominator.'),
            html.H2('Limitations'),
            html.Ol([html.Li('These are Ecotect simulations of 12 building forms under fixed Athens residential assumptions, not measured household energy bills. Results may not generalize to other climates or buildings.'),
                     html.Li('Height is linked to other design features, including roof area and compactness. Group summaries and overlapping scatter points do not isolate a causal height effect or account for every design difference.')]),
            html.Div(className='footer', children=[html.A('Source: Tsanas & Xifara (2012), UCI Energy Efficiency', href='https://archive.ics.uci.edu/dataset/242/energy+efficiency'),
                html.P('768 simulated configurations; 8 design features and 2 load outcomes. CC BY 4.0. Fixed original workbook included with this project. Accessed October 25, 2026.')])])])
    app.callback(Output('distribution','figure'), Output('height-box','figure'),
                 Output('glazing-scatter','figure'), Output('cooling-heatmap','figure'),
                 Output('selection-summary','children'), Input('height-filter','value'))(update)
    # Expose the exact registered calculation for reproducible notebook checks.
    app.lab_update = update
    return app


data = pd.read_excel(Path(__file__).resolve().parent / 'data' / 'ENB2012_data.xlsx')
app = build_dashboard(data)
server = app.server

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8055, debug=False)
