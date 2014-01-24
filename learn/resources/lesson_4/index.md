[meta title="Lesson 4: OOP (Object Oriented Programming) [INCOMPLETE]" /]

[embed page="/learn/resources/highlight.js/embed" /]

## What is Object Oriented Programming?

Quite often when writing programs, we can think of our code as a collection of
objects that interact with one other. For example, if we were writing a
simulation of a car, we could think of all of the different components of the
car as different objects, e.g. the doors, the engine, the windows, the frames
etc...

Even when we're not representing physical objects in our programs, it is still
useful to think of each of the different components of our program as different
objects. Another example, if you have a graphical interface with lots of
buttons and text boxes and images, each of those could be thought of as an
object.

### A Small Warning

So far in this course, everything we have taught you has been applicable to
pretty much every main programming language. However OOP is a little different,
because each programming language has a different approach. Languages will
either not support OOP, optionally support OOP, or force you to use it.

For Example:

* Languages that don't support OOP:
    * C
    * Pascal
* Languages that allow you to use OOP if you like:
    * Python
    * Ruby
    * JavaScript
    * PHP
* Languages that force you to use OOP:
    * Java
    * C#

You should be weary of this if and when you decide to learn another language.

### Introducing Classes and Objects

One of the main things to learn (and often the most confusing) is what classes
and objects are, and the difference between them.

Lets introduce a class, sticking to the vehicle paradigm. Follow along by
running python in [[../definitions/interactive_mode/|interactive mode]].

    >>> class Vehicle(object):
    ...     pass
    ...

This is a **class definition**, about as simple as you get. A class is
basically a description of how particular objects should look and behave. Every
object is of a particular class, and you can create new objects in python by
**calling** the class like you would a function.

    >>> a = Vehicle()
    >>> b = Vehicle()

We now have two objects, `a` and `b` that both have the class `Vehicle`. You
can check what class an object belongs to by calling `type()` on it:

    >>> type(a)
    <class '__main__.Vehicle'>
    >>> type(b)
    <class '__main__.Vehicle'>

### Properties (or Attributes)

Classes and objects can have **properties** (aka. **attributes**). These are a
bit like variables, except that they belong to a particular object.

    >>> class Person(object):
    ...     name = "No Name"
    ...

We have defined the property `name` for a new class `Person`. The properties
of a class basically describe to python what properties an object can have,
and what their default values are.

We can create a new person, and check their name:

    >>> a = Person()
    >>> a.name
    'No Name'
    >>> b = Person()
    >>> b.name
    'No Name'

And like variables, we can change them:

    >>> a.name = "Alex"
    >>> a.name
    'Alex'
    >>> b.name = "Bob"
    >>> b.name
    'Bob'

Classes and objects can have any number of attributes, all of different types

    >>> class Person(object):
    ...     first_name = None
    ...     last_name = None
    ...     age = 0
    ...     favourite_foods = []
    ...
    >>> c = Person()
    >>> c.first_name = "Clive"
    >>> c.last_name = "Johnson"
    >>> c.age = 30
    >>> c.favourite_foods.append("banana")
    >>> c.first_name
    'Clive'
    >>> c.last_name
    'Johnson'
    >>> c.age
    30
    >>> c.favourite_foods
    ['banana']

### Methods

Lets switch to saving our code as files now!

Methods are functions that work **"on"** a particular object.

    class Person(object):
        first_name = None
        last_name = None

        def set_name(self, fn, ln):
           self.first_name = fn
           self.last_name = ln

        def get_name(self):
            return self.first_name + " " + self.last_name

    a = Person()
    a.set_name("Alex", "Jones")
    b = Person()
    b.set_name("Bob", "Phillips")

    print a.get_name()
    print b.get_name()

Expected Output:

    Alex Jones
    Bob Phillips

In this example, the class `Person` has two properties, `first_name` and
`last_name`, but also two methods `set_name` and `get_name`.

There should be a couple of things that you notice with these two methods:

* They are indented, and so they are part of the class body, this means that
  they belong to the class.
* There is this magic word `self`, what's all that about? It's in the
  parameters of both of these "methods", but not passed as an argument when we
  use them later.

#### All about `self`

Methods are just a **special type of function**, like all other functions, they
have a certain number of **parameters** and have their own **variable scope**.
However, methods almost always need to somehow interact with the object that
we are using them on.

The way python acheives this is by passing the object we are using the method
on as an **argument** to the method, hence the definition of the method needs
to have an extra **parameter** just for itself (`self`). You can name the first
parameter of a method something other than `self` if you so wish.

As with all parameters, when a method gets called, they basically become
variables in the scope of the method, so you are then able to address `self`,
the object you're interacting with, like any other variable.

#### Revealing the Magic

In short, Python is doing a little bit of magic when you use methods on
objects. When we wrote this:

    a.set_name("Alex", "Jones")

What was basically happening was this:

    Person.set_name(a, "Alex", "Jones")

and when we wrote this:

    print a.get_name()

what was really happening was this:

    print Person.get_name(a)

Python does this magic transformation without us having to get involved.

#### What you need to take away from this

You need to put `self` in as a parameter for methods of a class, but you don't
need to add it when calling the method.

<div class="panel panel-danger">
  <div class="panel-heading"><strong>Another Warning</strong></div>
  <div class="panel-body">
    <p>
      What has just been described here regarding <code>self</code> is quite
      unusual behaviour among programming languages. The reason it is like this
      is two-fold:
    </p>
    <ul>
      <li>OOP was added in python as a bit of an after-thought, and the creator
      didn't want to change the language too much.</li>
      <li>The creators of python like you to be <strong>explicit</strong>, when
      writing methods, you can always see where <code>self</code> came from, it
      was a parameter!</li>
    </ul>
    <p>
      In most other programming languages that support OOP, there is a way to
      reference the <strong>"current object"</strong> without having it passed
      as a parameter, keep this in mind if / when you learn them.
    </p>
  </div>
</div>

## What do I do now?

Unfortunately, this lesson you've just read was somewhat rushed, and
incomplete. I (Sam) apologies about that. This lesson will be expanded and
hopefully completed by next session (that's the problem with writing it in
term-time eh?).

The right thing to do now would be to learn more about OOP in python, I would
recommend you take a slightly different tactic at this point to what you
normally would.

Head on over to the [Python Section on
Codecademy](http://www.codecademy.com/tracks/python) and do lessons 19 and 20.
Codecademy allows you to learn, write code and run code all in your web
browser, and they have some pretty cool tutorials.

If you finish that, and are stuck for things to do, either:

* Complete as many python lessons as you can on Codecademy.
* Start learning another language on Codecademy.
* Try and do as many challenges as you can on [Project
  Euler](http://projecteuler.net/problems).
* or ask a TA for things to do!

Next week will be back to normal, I promise! =)
