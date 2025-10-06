import random
import math

def createRandomWkt(startX, startY, delta=0.07, hasPoints = True, hasLines=True, hasPoly = True, LatLon = True):
    startWkt= "GEOMETRYCOLLECTION("
    points=""
    if hasPoints:
        points_count = 1 + round(10*random.random())
        i = 0
        while i < points_count:
            ra = math.pi*random.random()
            ok = delta*random.random()
            lat = str(startX+ok*math.cos(ra))
            lon = str(startY+ok*math.sin(ra))
            if LatLon:
                points = points + "POINT ("+lat+" "+lon+")"
            else:
                points = points + "POINT ("+lon+" "+lat+")"
            if (i<points_count - 1):
                points=points +", "
            i = i+1
    lines=""
    if hasLines:
        lines_count = 1 + round(5*random.random())
        i = 0
        if hasPoints:
            lines = ", "
        while i < lines_count:
            cur_line = "LINESTRING ("
            j = 0
            i = i+1
            count_p = 2 + round(3*random.random())
            while j < count_p:
                ra = math.pi*random.random()
                ok = delta*random.random()
                lat = str(startX+ok*math.cos(ra))
                lon = str(startY+ok*math.sin(ra))
                if LatLon:
                    cur_line = cur_line + lat +" "+ lon
                else:
                    cur_line = cur_line + lon +" "+ lat
                if (j<count_p - 1):
                    cur_line=cur_line +", "
                j = j+1
            cur_line = cur_line+")"
            lines = lines + cur_line
            if i < lines_count:
                lines=lines +", "
    polys=""
    if hasPoly:
        poly_count =  1 + round(5*random.random())
        if hasPoints or hasLines:
            polys = ", "
        i = 0
        while i < poly_count:
            cur_poly = "POLYGON (("
            j = 1
            i = i+1
            count_p = 3 + round(7*random.random())
            center_x = startX+0.5*delta*math.cos(math.pi*random.random())
            center_y = startY+0.5*delta*math.sin(math.pi*random.random())
            str_first=""
            while j < count_p:
                radius = delta*0.3*(0.1+random.random())
                angle = j*2*math.pi/count_p
                lat = str(center_x+radius*math.cos(angle))
                lon = str(center_y+radius*math.sin(angle))
                if LatLon:
                    if j == 1:
                        str_first = lat+" "+lon
                    cur_poly = cur_poly +lat +" "+ lon
                else:
                    if j == 1:
                        str_first = lon+" "+lat
                    cur_poly = cur_poly +lon +" "+ lat
                cur_poly=cur_poly +", "
                j = j+1
            cur_poly = cur_poly+str_first+"))"
            polys = polys + cur_poly
            if i < poly_count:
                polys=polys +", "
    finishWkt = ")"
    return startWkt+points+lines+polys+finishWkt
f = open('geom.wkt', 'w')
f.write(createRandomWkt(37.972443,55.826433, LatLon = False))
