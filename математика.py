import plotly.express as px
x = list(range(-10, 10, 2))
y = {'x':[], 'y':[], 'k':[], 'm':[]}
for ki in range(-10,11):
    for mi in range(-50, 51,10):
        for xi in x:
            y['x'].append(xi)
            y['k'].append(ki)
            y['m'].append(mi)
            y['y'].append(ki * xi**2 + mi*xi)

y['c'] = [1 for i in range(len(y['x']))]
# print(y['x'])
# print(y['y'])
# print(y['k'])
# print(y['m'])

fig = px.scatter(y,
                 x="x",
                 y="y",
                 animation_frame="k",
                 animation_group="y",
                 symbol='m',
                 #size="c",
                 render_mode='lines',
                trendline='lowess',
                 trendline_color_override='#00ff00'
                 )

fig.show()