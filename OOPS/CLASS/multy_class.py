# A user can create and view 2D coordinates
# A user can find out the distance b\w 2 coordinates
# A user can find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance b\w a given 2D point and a given line

class Point:
    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod, self.y_cod)
    
    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        # return (self.x_cod**2 + self.y_cod**2)**0.5
        return self.euclidean_distance(Point(0, 0))
    

class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)
    
    def point_on_line(line, point):
        if line.A * point.x_cod + line.B * point.y_cod + line.C == 0:
            return 'point lies on the line'
        else:
            return 'point does not lie on the line'

    def shortest_distance(line, point):
        return (abs(line.A * point.x_cod + line.B * point.y_cod + line.C)/((line.A**2 + line.B**2)**0.5))

p1 = Point(0, 4)
p2 = Point(3, 0)
print(p1)
print(p1.euclidean_distance(p2))
print(p1.distance_from_origin())

p3 = Point(-1, -2)
L1 = Line(2,3,8)
print(L1)
print(L1.point_on_line(p1))
print(L1.point_on_line(p3))
print(L1.shortest_distance(p1))
print(L1.shortest_distance(p3))                 # this point is already on line so ditance = 0