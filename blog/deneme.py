import math
from turtle import *


def a(k):
    return 15*math.sin(k)**3
def b(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)

speed(10000)
bgcolor('black')
for i in range(6000):
    goto(a(i)*20,b(i)*20)
    for j in range(5):
        color('red')
    goto(0,0)
done()