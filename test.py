import plotly.figure_factory as ff
import plotly as plotly

z = [[0, 0, 0, 0, 0, 0, 41], [67, 290, 226, 172, 181, 51,
                    67], [172, 324, 216, 135, 169, 75, 79], [296, 461, 316, 265,
                    256, 238, 249], [362, 419, 246, 169, 140, 61, 64], [168, 0,
                    0, 0, 0, 0, 0]]

fig = ff.create_annotated_heatmap(z,zmin=1, zmax=500, colorscale='Viridis')
plotly.offline.plot(fig)