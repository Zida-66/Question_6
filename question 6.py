import pandas as pd
import numpy as np

polygon_data1 = pd.read_csv("input_question_6_polygon.txt", sep=' ', header=None)
polygon_data2 = pd.read_csv("input_question_6_points.txt", sep=' ', header=None)
outputs = pd.read_csv("output_question_6.txt", sep=',', header=None)


def rayCasting(p, poly):
    px = p['x']
    py = p['y']
    flag = False

    i = 0
    l = len(poly)
    j = l - 1
    while i < l:
        sx = poly[i]['x']
        sy = poly[i]['y']
        tx = poly[j]['x']
        ty = poly[j]['y']

        # the point coincides with the vertex of polygon
        if (sx == px and sy == py) or (tx == px and ty == py):
            return (px, py)

        # judge whether the two terminals of the line segment are on different sides of the ray
        if (sy < py and ty >= py) or (sy >= py and ty < py):
            # the x-coordinate of the point on the line segment which has the same y-coordinate with the terminal of the ray
            x = sx + (py - sy) * (tx - sx) / (ty - sy)
            # on the edge of the polygon
            if x == px:
                return (px, py)
            # the ray shoots across the edge of the polygon
            if x > px:
                flag = not flag
        j = i
        i += 1
    # the ray shoots through the edges of the polygon odd number times: the point is inside.
    return (px, py) if flag else 'out'


# get the coordinate of the point
def getpoint(a):
    i = 0
    pointtojudge = []
    while i < len(a.split(',')[1::2]):
        pointtojudge.append({'x': float(a.split(',')[::2][i]), 'y': float(a.split(',')[1::2][i])})
        i += 1
    return pointtojudge


def rs(pointtojudge, polygon):
    ptj = getpoint(pointtojudge)
    plg = getpoint(polygon)
    count = 0
    x = []
    for point in ptj:
        rs = rayCasting(point, plg)
        if rs == 'out':
            x.append('outside')
        else:
            x.append('inside')
    return x


out = ''
for i in np.array(outputs.iloc[:, :2]).reshape((-1)):
    out = out + str(i) + ','
out = out[:-1]
inp1 = ''
for i in np.array(polygon_data1).reshape((-1)):
    inp1 = inp1 + str(i) + ','
inp1 = inp1[:-1]
inp2 = ''
for i in np.array(polygon_data2).reshape((-1)):
    inp2 = inp2 + str(i) + ','
inp2 = inp2[:-1]

inp1_list = rs(out, inp1)
data = outputs.iloc[:, :2]
data['yesorno'] = inp1_list
data.to_csv('output_question_6.txt', index=False, header=None)
