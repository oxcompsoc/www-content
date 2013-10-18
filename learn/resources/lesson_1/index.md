[meta header="Lesson 1: Introduction with turtle" /]

[embed page="/learn/resources/highlight.js/embed" /]


To get started, we'll be using something called **`turtle`**.

**Turtle** is a python **[[../definitions/package|package]]** (A collection
of python code that provides a certain bit of functionality). It creates a
window with a **"cursor"** that allows us to draw lines and shapes on it, like
this pentagon example:

<img class="img-thumbnail" src="turtle_1.png" alt="Turtle Example" style="display: block; margin: 0 auto;" />

## Getting Started

Firstly, open up your python [[../definitions/interpreter|interpreter]]. The
python interpreter allows you to write code line-by-line without having to save
it anywhere (this is called
[[../definitions/interactive_mode|interactive mode]]).

You should see something like this:

    Python 2.7.5 (default, Sep  6 2013, 09:55:21)
    [GCC 4.8.1 20130725 (prerelease)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

The interpreter is waiting for you to type in your first line of code.

We're going to tell python that we want to use the `turtle` package. Write this
text into the interpreter and hit `Enter` (which we will be doing with every
command we write).

**Note: Make sure you don't write the "`>>>`"**

    >>> import turtle

Now the package is ready for us to use, but a window has not yet appeared
because we have not told it to do anything. Let's tell it do do something!

    >>> turtle.forward(200)

A window should appear with an arrow that moved 200 pixels to the right.

We can also move the cursor backwards

    >>> turtle.backward(100)

And rotate it clockwise...

    >>> turtle.right(90)

...and anticlockwise

    >>> turtle.left(180)

*Note: The numbers that we tell it to rotate with are in degrees*

Have a play around with these commands, and try experimenting with the numbers.

There are also these other commands you can try:

    # Imprint the image of the cursor on the drawing area
    >>> turtle.stamp()

    # Change the shape of the cursor, you have a choice of “arrow”, “turtle”, “circle”, “square”, “triangle” or “classic”
    >>> turtle.shape("turtle")

    # Change the thickness of the line you are drawing
    >>> turtle.width(5)

    # Stop drawing lines when you move
    >>> turtle.penup()

    # ...and resume drawing lines
    >>> turtle.pendown()



## Your first Python file

There is of course a way of writing code which does require you to enter it
line-by-line in [[../definitions/interactive_mode|interactive mode]], we can
save a large amount of code in a single `.py` file and ask the
[[../definitions/interpreter|interpreter]] to run that instead.

*Note: This doesn't make [[../definitions/interpreter|interpreter]] useless, it
can be very handy when you just need to quickly test your ideas by writing one
or two lines of code*

