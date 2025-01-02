from solid2 import *
import math

def star(points=5, outer_radius=5, inner_radius=2):
    points *= 2
    angle = 360/points
    def pos(i):
        r = outer_radius if i % 2 == 0 else inner_radius
        rad = math.radians(i*angle)
        return r*math.cos(rad), r*math.sin(rad)

    return polygon([pos(i) for i in range(points)])

set_global_fn(100)

happa = linear_extrude(height=1)(star())
heta = scale((1, 1, 0.2))(sphere(1)).translateZ(1)
kashokubu = scale((1, 1, 0.85))(sphere(15))

mikan = kashokubu + (heta + happa).translateZ(15*.8)
mikan.save_as_scad('mikan.scad')
mikan.save_as_stl('mikan.stl')
