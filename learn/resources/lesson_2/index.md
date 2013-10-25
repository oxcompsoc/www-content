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

That is an **[[../definitions/error|error]]**, it looks pretty nasty! Whenever you
have written something that python doesn't know how to handle, it will give you
an error like this.

There are many many things that can cause errors in python, lets have a look at
another example.

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



## Understanding the `for` loop












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
