Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
>>> 
>>> 
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> import turtle as t
>>> help(t.forward)
Help on function forward in module turtle:

forward(distance)
    Move the turtle forward by the specified distance.
    
    Aliases: forward | fd
    
    Argument:
    distance -- a number (integer or float)
    
    Move the turtle forward by the specified distance, in the direction
    the turtle is headed.
    
    Example:
    >>> position()
    (0.00, 0.00)
    >>> forward(25)
    >>> position()
    (25.00,0.00)
    >>> forward(-75)
    >>> position()
    (-50.00,0.00)

>>> help(t.right)
Help on function right in module turtle:

right(angle)
    Turn turtle right by angle units.
    
    Aliases: right | rt
    
    Argument:
    angle -- a number (integer or float)
    
    Turn turtle right by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)
    
    Example:
    >>> heading()
    22.0
    >>> right(45)
    >>> heading()
    337.0

>>> help(t.cicle)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    help(t.cicle)
AttributeError: module 'turtle' has no attribute 'cicle'
>>> help(t.circle)
Help on function circle in module turtle:

circle(radius, extent=None, steps=None)
    Draw a circle with given radius.
    
    Arguments:
    radius -- a number
    extent (optional) -- a number
    steps (optional) -- an integer
    
    Draw a circle with given radius. The center is radius units left
    of the turtle; extent - an angle - determines which part of the
    circle is drawn. If extent is not given, draw the entire circle.
    If extent is not a full circle, one endpoint of the arc is the
    current pen position. Draw the arc in counterclockwise direction
    if radius is positive, otherwise in clockwise direction. Finally
    the direction of the turtle is changed by the amount of extent.
    
    As the circle is approximated by an inscribed regular polygon,
    steps determines the number of steps to use. If not given,
    it will be calculated automatically. Maybe used to draw regular
    polygons.
    
    call: circle(radius)                  # full circle
    --or: circle(radius, extent)          # arc
    --or: circle(radius, extent, steps)
    --or: circle(radius, steps=6)         # 6-sided polygon
    
    Example:
    >>> circle(50)
    >>> circle(120, 180)  # semicircle

>>> t.circle(50)
>>> t.circle(50,extent,steps)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.circle(50,extent,steps)
NameError: name 'extent' is not defined
>>> t.circle(50,extent=5,steps=6)
>>> t.circle(50)
>>> 
