from turtle import *

tom=Turtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.setup(400,400)
ts.screensize(canvwidth=400, canvheight=400, bg=None)
ts.getcanvas().postscript(file="turtle_doing_nothing.eps")


tom.getscreen()._root.mainloop()

