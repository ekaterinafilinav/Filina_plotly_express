import plotly.express as px


# fig = px.scatter_geo(lat=[51.555051, 55.753215],
#                      lon=[46.013428, 37.622504],
#                      size=[800000, 12000000])
# fig.show()


fig = px.line_geo(lat=[51.555051, 55.753215, 28.613506],
                  lon=[46.013428,37.622504, 77.207917],
                  projection="orthographic")
fig.show()
