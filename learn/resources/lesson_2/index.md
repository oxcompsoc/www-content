[meta title="Lesson 2: Getting more in Depth" /]

[embed page="/learn/resources/highlight.js/embed" /]

Personal note of things that need to be covered:

* types
* conditionals (`if`, `while`)
* user input (in particular the `raw_input()` function

Now that you have had some exposure to python, and have got a feel for what a
program might look like (after writing your own `.py` scripts), we're going to
look in more detail at some of the things we have written, and introduce some
new techniques.

We're going to begin again by using the python interpreter in
[[../definitions/interactive_mode|interactive mode]]; start your terminal
application, and type in the command `python`.

You may have noticed that when we were writing variables in the last lesson,
and when we were using turtle, there was a difference with how we were using
numbers, and things that were not numbers, for example: *(you don't need to type
this in)*

    variable_1 = 123
    variable_2 = "something"

The first variable value is just a number, however the second one is surrounded
with quotation marks (`" "`). This is because the values that we have set the
variables to have different [[../definitions/types|types]].

## Introducing Types

Most programming languages have a concept of [[../definitions/types|types]],
there are lots of different kinds of data that we might want to store in our
programs, and we might want different bits of data to behave in different ways.

Python allows us to inspect the type of anything within our programs, in your
python interpreter (which needs to be in
[[../definitions/interactive_mode|interactive mode]]), go ahead and write this:
`type(123)`. You should see this:

    >>> type(123)
    <type 'int'>

### The `int` type

`int` values are integer numbers (i.e. no decimals / fractions). It is one of
the most used types of value. However, there is also another type of value for
when we want to be able to handle decimal places.

### The `float` type

    >>>> type(1.5)
    <type 'float'>

    >>> type(0.000000000004)
    <type 'float'>

`float` values (Floating Point Numbers) are numbers that can have a decimal
places.

One of the reasons that there are two different **types** for number values
(and the reason we don't just allow decimal places for all numbers) is because
the processor needs to handle these numbers differently. Also `ints` and
`floats` have different behaviour that we might want to use in our programs,
for example, you can always guarantee that an `int` will be a whole number,
which a lot of the time is important! *(There will be an example of this
later)*

### The `str` type

    >>> type("hello!")
    <type 'str'>

`str` is short for **string**, a "sequence of characters", in other words,
**text**. Text is useful in programs for many reasons, for example, in
[[../lesson_1|lesson 1]], we wrote this:

    turtle.shape("turtle")

So the turtle package allowed us to choose a shape by giving it's name, which
is a lot nicer than, for example, giving it an `int` instead.

A very common use for **strings** is for interacting with the user, e.g. giving
the user a message, or asking the user to input information on the keyboard,
and receiving a **string**.

We will go on to creating applications that interact with the user later on
in this lesson.

**Note: You are allowed to use both double quotes (`" "`) and single quotes
(`' '`) to give python `str` values, however it has to be the same for both
the start and the end!**

**E.G:**

    >>> type('hello!')
    <type 'str'>

## Manipulating Values and Variables

When writing programs, you will come accross the need to manipulate and combine
different values and variables. In [[../lesson_1|Lesson 1]], we introduced some
mathematical operations that we could use to perform calculations, but there is
much more you can do with variables and values.

### Assigning New Values

Up until now, we have only created variables, and used them... however there is
one more fundamental thing that we can do with them, and that is change their
value!

Let's start by creating a new variable

    >>> a = 123

And we can type in the name of a variable into the python interpreter to see
what it's value is:

    >>> a
    123

Lets change the value of `a`:

    >>> a = 54321
    >>> a
    54321

...and make a new variable that uses `a` and a bit of maths:

    >>> b = a * a
    >>> b
    2950771041

and now lets add `9` to a:

    >>> a = a + 9
    >>> a
    54330

In that last one, we used the **current** value of a to calculate a **new**
value for a. This type of pattern is quite common, where we use the existing
value of a variable to calculate a new value.

What python does in this case is work out the value of everything on the right
of the equals `=`, and then changes the value of a.

#### Types Don't Matter!

When it comes to changing a value in python, it is perfectly happy for you to
assign it a value that is of a different **type** to it's current value:

    >>> type(a)
    <type 'int'>

The type of a is currently `int`, so lets give it a `float` value...

    >>> a = 1.6
    >>> a
    1.6
    >>> type(a)
    <type 'float'>

How about `string`?

    >>> a = "hello"
    >>> a
    'hello'
    >>> type(a)
    <type 'str'>

This is called [[../definitions/dynamic_typing|dynamic typing]], and we'll be
talking a bit more about this later.

### Changing something from one type to another

It can sometimes be desireable to change something from one type to another,
for example, you might want to ask the user to type in an `int` on the keyboard
however as they are inputting the information using a keyboard, you will
probably be getting a `string`. How can you convert this `string` into an
`int`?

#### Converting things to `int`:

Python allows you to use `int()` to convert something that isn't an `int` into
a value of type `int`.

**`string` to `int`:**

    >>> s = "1234"
    >>> i = int(s)

Inspecting the types:

    >>> type(s)
    <type 'str'>
    >>> type(i)
    <type 'int'>

However, sometimes, python might not be able to work out how to change a
particular `string` to an `int`, for example:

    >>> i = int("hello")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'hello'

This gives you an **[[../definitions/error|error]]**. Whenever you have written
something that python doesn't know how to handle, it will give you an error
like this.

There are many many things that can cause errors in python, there will be many
examples throughout this lesson.

**`float` to `int`:**

When you convert a `float` to an `int`, python will round-down the number to
make it a whole number:

    >>> i = int(123.456)
    >>> i
    123
    >>> type(i)
    <type 'int'>

#### Converting things to `float`:

Like `int`, python allows you to do a similar thing with `float`:

**`string` to `float`:**

    >>> s = "1234"
    >>> f = float(s)
    >>> f
    1234.0
    >>> type(f)
    <type 'float'>
    >>> type(s)
    <type 'str'>

And an example with decimals...

    >>> f = float("123.456")
    >>> f
    123.456
    >>> type(f)
    <type 'float'>

And something that will produce an error:

    >>> f = float("pong")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: could not convert string to float: pong

**`int` to `float`:**

    >>> float(123)
    123.0

#### Converting things to `str`:

Again, you can do the same thing with `str`:

    >>> str(123)
    '123'
    >>> str(54.321)
    '54.321'

Notice how the values are surrounded in quotes (`' '`).

### Playing around with strings

Something that you'll find that you'll be doing quite often is building large
strings by combining lots of values together. We'll be using this later on to
output information to the [[../definitions/console|console]].

Joining strings together ent-to-end is called **concatenating**, and in python
you do this by using the `+` operator (the same one for mathematical addition).

Example:

    >>> "Hello" + "World"
    'HelloWorld'

You'll notice that there is no space betweein `"Hello"` and `"World"` in the
final string, we need to put one in one of the two parts for it to appear!
Python will not automatically add spaces when **concatenating** strings
together, because sometimes this might not be desireable!

    >>> "Hello " + "World"
    'Hello World'
    >>> "Hello" + " World"
    'Hello World'
    >>> "Hello " + " World"
    'Hello  World'

How about making a string with some useful information? Lets print out a number
along with some text, and have that number come from a variable:

    >>> favourite_number = 12
    >>> "Your favourite number is: " + favourite_number
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: cannot concatenate 'str' and 'int' objects


**We got an error!**

This is telling us that we cannot concatenate a `str` and an `int` together,
i.e, for concatenation to work, both values need to have type `str`. This is
fine because we know how to convert an `int` to a `str`!

    >>> favourite_number = 12
    >>> "Your favourite number is: " + str(favourite_number)
    'Your favourite number is: 12'

And of course, concatenating lots of strings together works as we'd expect:

    >>> "this " + "is " + "a " + "really " + "long " + "string " + "concatenation"
    'this is a really long string concatenation'

We'll be coming back to this later on when we start to use the
[[../definitions/console|console]]!

## A More Interesting Type: `list`

Lists are a very useful type of value, they allow you to store a sequence of
different values in a single location, write this in your interpreter:

    >>> my_list = ['apple', 'pear', 'bannana']

You have now created a list, and stored it in a variable called `my_list`.

If you inspect the type, you will see it is a list:

    >>> type(my_list)
    <type 'list'>

And you can inspect the current value of `my_list` in the interpreter (like
you can with any **variable**):

    >>> my_list
    ['apple', 'pear', 'bannana']

You can check the length of the list:

    >>> len(my_list)
    3

You can add items to the list:

    >>> my_list.append('berry')
    >>> my_list
    ['apple', 'pear', 'bannana', 'berry']

### Accessing Items in a `list`

Python allows you to access individual items in a list by specifying an
`index`, the number of the **item** within a list.

**Note: The first item in the list is item `0`, and the second item is `1`
etc... It might not be obvious right now why that is the case, but there are
many mathematical reasons why starting from `0` makes everything a lot nicer.**

    >>> my_list[0]
    'apple'
    >>> my_list[1]
    'pear'
    >>> my_list[3]
    'berry'

And of course, python will only allow you to use `indexes` representing items
that are actually in the list:

    >>> my_list[4]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

This is another **[[../definitions/error|error]]**, Lets have a look at a
different example of one.

Remember how we said earlier that difference in behaviour between `int` and
`float`, in particular that `int` is **ALWAYS** a whole number, can be useful?
Well, list `indices` always need to be whole numbers, because saying "I want
the 1.5th item in a list" doesn't make any sense. So of course python will give
an error:

    >>> my_list[1.5]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: list indices must be integers, not float

And you get a similar error if you try and specify a `string` index:

    >>> my_list["foo"]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: list indices must be integers, not str

or even if you try a `list` as an index!

    >>> list_index = [1, 2, 3, 4]
    >>> my_list[list_index]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: list indices must be integers, not list

### Changing Items in a `list`




## Creating a Script with Console Output





## Understanding the `for` loop





## Introduction to Booleans

### The `bool` type



### Using Booleans to Make Desicions



### Using Booleans in Loops









## LEAVE TIL LAST!

## How Different Programming Languages Handle Types and Variables

Although this course uses python, it's aim is to teach you **general
programming skills**, so that you will be able to much more easily go and learn
another programming language or two, and understand the basic concepts needed
to **get started very quickly**. Of course after the course has finished, you
can learn more python if you prefer.

Different programming languages do many things in many different ways, and
throughout this course, we will try and point out differences that you may come
accross with different programming languages. This will hopefully prepare you
well for any language you wish to learn afterwards.

### How Python Handles Types

Python allows as to make a variable any type of value at any time, eg:

    >>>
