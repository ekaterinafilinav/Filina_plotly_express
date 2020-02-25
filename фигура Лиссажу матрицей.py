import plotly.express as px
from math import pi, cos, sin

df = {'x': [], 'y': [], 'omega': [], 'f': []}
for omegai in [(1, 1), (1, 2), (1, 3), (2, 3), (3, 4)]:
    for fi in [0, pi / 4, pi / 2, 3 * pi / 4, pi]:
        for ai in range(0, 360, 1):
            df['x'].append(10 * sin(omegai[0] * ai * pi / 180))
            df['y'].append(10 * sin(omegai[1] * ai * pi / 180 + fi))
            df['omega'].append(str(omegai[0]) + '/' + str(omegai[1]))
            df['f'].append(round(fi, 2))

fig = px.line(
    df,
    x='x',
    y='y',
    facet_col='omega',
    facet_row='f',
)
fig.show()
