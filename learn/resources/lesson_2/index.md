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

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
  Experiment with using <code>type()</code> on different things. Try doing some
  <strong>mathematical operations</strong> and working out the types of the
  different results. Also see what happens when you mix <code>int</code> and
  <code>float</code> values with maths operators.
  </div>
</div>

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
output information to the [[../definitions/terminal|console]].

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
[[../definitions/terminal|console]]!

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

Like we can change the value of a variable, we can change the values of
individual items in a list.

Lets firstly create a new list:

    >>> a = ["dog", "cat", "fish"]
    >>> a
    ['dog', 'cat', 'fish']

Now lets change the value of `"cat"` which has an index of `1`.

    >>> a[1] = "lion"
    >>> a
    ['dog', 'lion', 'fish']

You can also have items of different types in a single list too!

    >>> a[2] = 3
    >>> a
    ['dog', 'lion', 3]

And just like variables, in an assignment, an item can reference itself, or any
other value!

    >>> a[2] = a[2] * a[2]
    >>> a
    ['dog', 'lion', 9]
    >>> a[0] = a[0] + "s are cool"
    >>> a
    ['dogs are cool', 'lion', 9]

## Creating a Script with Console Output

Now we've reached the part of the lesson where we're going to create a new
python script (a `.py` file) with a particular goal. We're going to use the
techniques we've learned so far, and techniques that will be taught over the
rest of this lesson to create a **"results calculator"**.

The results calculator will request information about our results for a number
of exams, and calculate things like the averages, whether we got a first, a 2-1
etc...

Open your text editor as normal:

* If you are using the **Lab Computers**, press `Alt + F2` and paste in this:
  `/usr/local/practicals/compsoc/sublime` and then hit `Enter`.
* If you are using your **own computer**, open sublime text how you normally
  would.

Create a new empty file and save it as `results_calculator.py` in a folder
called `python` in your [[../definitions/home_directory|home directory]].

### Printing to the [[../definitions/terminal|Console]]

In the last lesson, our scripts were interacting with the `turtle` package
which was drawing on the screen, in this lesson we'll be doing something
different. We'll be interacting with your [[../definitions/terminal|console]]
(your terminal), both writing information to it, and asking for user input from
it.

You may remember that in the last lesson, we were using `raw_input()` to
prevent the program closing as soon as the turtle finished drawing on the
screen. If you recall, `raw_input()` waited until we pressed the `Enter` key
before finishing, what it was actually doing was waiting for user input in the
**terminal**, we just were not using the information that it provides. We will
look more into this shortly.

Firstly, lets output information, in your new python script, write this:

    print "Welcome to the Results Calculator"

`print` is the main way in which we output information to the terminal.

Now save your new file, and run your python code in your terminal by running
this command:

    python python/results_calculator.py

This assumes that you have saved your file in a folder called "python" like in
the last lesson. If you are having trouble running this command, and instead
get something like this:

    python: can't open file 'python/results_calculator.py': [Errno 2] No such file or directory

... then flag up a helper! Make sure that the cases match, most things when it
comes to programming are **case sensitive**!

When you successfully run the script, it should output this:

    Welcome to the Results Calculator

Now lets try and print a few other things, make your python file look like
this:

    print "Welcome to the Results Calculator"

    print "something else"
    print 123
    print 654.321
    print [1, 2, 3]
    list_1 = ["apples", "oranges"]
    print list_1
    print list_1[1]

When you run it, it should output something like this:

    Welcome to the Results Calculator
    something else
    123
    654.321
    [1, 2, 3]
    ['apples', 'oranges']
    oranges

Notice a couple of things:

* `print` was happy to handle a value that has a type `list`, this is handy for
  "debugging", and many other reasons.
* the `str` values don't have quotes around them like they do when we inspect
  the value of something in **interactive mode**. This is because when we're
  printing to the console, we mostly want to be giving text, or converting
  things to text, so quote marks everywhere would be undesireable!

Lets try concatenating some `str` values together like we did earlier!

    print "Welcome to the Results Calculator"

    print "some text " + "joined together!"

    # Remember, we need to change anything that is not a `str` into a `str`
    # before we can concatenate them together!
    print "here is an int value: " + str(123)
    print "and here is a float: " + str(543.21)

Running the code should result in this:

    Welcome to the Results Calculator
    some text joined together!
    here is an int value: 123
    and here is a float: 543.21

Now we have a good way to output values and text to the terminal, lets start
using it to build our results calculator.

## Understanding the `for` loop

In the [[../lesson_1|last lesson]], we used a `for` loop to repeat things a
fixed number of times, lets use the same code here to print something a few
times:

    print "Welcome to the Results Calculator"

    for count in range(6):
        print "running code inside loop"

Running the code should result in this:

    Welcome to the Results Calculator
    running code inside loop
    running code inside loop
    running code inside loop
    running code inside loop
    running code inside loop
    running code inside loop

Now as you expect, it outputs the line `running code inside loop` 6 times.

What we're yet to tell you is that the above `for` loop is actually doing quite
a bit of useful things...

* The command `range(6)` is actually creating a `list` with the numbers `0` to
  `5`. I.E: `[0, 1, 2, 3, 4, 5]`, a list with `6` items, starting from `0`.
* The `for` loop is running the code inside of it once for every item in the
  list given by `range(6)`.
* At the start of each `iteration` of the loop, python is setting a variable
  called `count` to be the next value inside the list that it has been given.

*(an **iteration** is running the code inside the loop **a single time**, in
the example above, the loop had `6` iterations)*

Lets inspect this behaviour by changing the code:

    print "Welcome to the Results Calculator"

    print range(6)
    print type(range(6))

    for count in range(6):
        print count

Running the code will output the following:

    Welcome to the Results Calculator
    [0, 1, 2, 3, 4, 5]
    <type 'list'>
    0
    1
    2
    3
    4
    5

We can use a variable to store the value that `range(6)` produces:

    print "Welcome to the Results Calculator"

    # We now know that range(6) creates a list, lets set a variable to the value that it creates
    my_list = range(6)

    print my_list
    print type(my_list)

    for count in my_list:
        print count

And if we run the code it should output the same!

We can also use a different variable name inside of the `for` loop instead of
`count`:

    for blah in my_list:
        print blah

### The Take-Home Message:

A `for` loop in python can be given a list, and it will run once for every item
in the list, while also making a variable with a name we choose equal to the
current item in the list.

### Making the `for` loop Useful

We currently have a list `[0, 1, 2, 3, 4, 5]` stored as the variable `my_list`,
but we dont have to iterate over a list of just numbers, we could iterate over
a list of `str` values!

    print "Welcome to the Results Calculator"

    my_list = ["apple", "orange", "banana"]

    for fruit in my_list:
        print fruit

This should result in this:

    Welcome to the Results Calculator
    apple
    orange
    banana

In our results calculator, we want to collect information about the results of
**each course we are interested in**, so how about we **create a list of all of
these courses**. Because the course names can be quite long, we can use the
fact that python allows us to **spread lists over multiple lines** to help us!

Write something along the lines of this (use your own courses, or made up
courses if you prefer)

    print "Welcome to the Results Calculator"

    print "" # Print a blank line to space out the output

    courses = ["Learn to Cook",
               "Learn to Code",
               "Learn to Dance"
               ]

    for course in courses:
        print course

Resulting in something like this:

    Welcome to the Results Calculator

    Learn to Cook
    Learn to Code
    Learn to Dance


## User Input

Last lesson we wrote `raw_input()` to prevent our programs from terminating 
immediately. It turns out that it is also possible to write:

    yourname = raw_input("What is your name?")
    print "Hi " + yourname

What do you think will happen here?

You should find that when you run your code, the program will pause at the `raw_input` 
line, waiting for user input. If you type in some text and then hit `Enter`, 
you'll see that the program will greet you!

Basically, raw_input is able to take a string as a parameter which will be used 
to prompt the user, and then it returns a string which we can assign to a variable.

But watch out! What is wrong with the following code?

    number = raw_input("Please enter a number")
    new_number = number + 5
    print new_number

So because raw_input returns a string, we can't just start treating it like a 
int! We'll need to convert it, do you remeber how to do that? Yup, you'd need
to write:

    number = int(raw_input("Please enter a number"))
    new_number = number + 5
    print new_number


This is good, but have you noticed how there is no space after the prompt 
for you to then enter the number? We can fix that by adding a final space 
to the string we put into raw_input. So rather than `"Please enter a number"`, put `"Please enter a number "`.

Great, now lets put this together and make our program ask the user for some 
module scores between 0 and 100, then we can tell them what their average was.
Try writing the code youself, but if you get stuck then use the copy below 
for reference.

    print "Welcome to the Results Calculator"
    scores = ["first","second","third"]
    total = 0
    for number in scores:
        score = int(raw_input("Please enter the " + str(number) + " module score between 0 and 100: "))
        total = total + score

avg_percent = total / len(scores)
print "Your average was " + str(avg_percent)


Awesome, now try out your program a few times. What happens if you don't enter a number?
Now you might be a bit confused by the line `total = total + score`. Have we broken mathematics?
Actually no! This simply says "add the value of score to total", and so by doing this, we keep a 
running total of the module scores.

## If Statements

### Making Decisions

After you've calculated the average percentage, what if you want to tell the
user of your script whether they've passed or failed?

To do this, you're going to need some way of changing the code that runs, based
on the value of `avg_percent`. If `avg_percent >= 40` then they've passed
(Hooray), otherwise, better luck next time.

Luckily, python's got you covered with an `if` statement, and it looks something
like this:

    if this_is_true:
        do_this()
    else:
        do_this_other_thing()

Pretty simple, right?

So, for us to tell people whether they've passed or failed, we need to check
whether their average percent (`avg_percent`) is *greater than or equal to 40*.
If it is, we shall `print "Pass! :)"`, otherwise we will `print "Fail. :(".

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    Using the hints above, construct an <code>if</code> statement that prints
    "Pass! :)" when their <code>avg_percent</code> is 40 or more, and "Fail. :("
    otherwise.
  </div>
</div>

### Multiple Choice: `elif`

But what if we want to go into a bit more detail? Our users probably want to
know whether or not they got a 3rd, 2nd, 2-1, or 1st.

To do this, we will need to branch more than once, which you can do like this,
by putting an `if` inside another `if`'s `else` block:

    if condition1:
        do_this()
    else:
        if condition2:
            do_something_else()
        else:
            do_this_other_thing()

But that's a bit cumbersome, especially when you have to branch 3 times, like we
will have to. So, python has something called `elif`, which is short for the
`else` and `if` in the previous example. So if we were to rewrite the previous
example using `elif` we would get:

    if condition1:
        do_this()
    elif condition2:
        do_something_else()
    else:
        do_this_other_thing()

Much neater! And now, the more conditions you have, we won't end up with our
code drifting towards the right side of the screen.

So, if our user has an `avg_percent` that is *greater than or equal to 70* we
will `print "1st"` *el*se *if* their `avg_percent` is *greater than or equal
to 60* we `print "2-1"` (...and so on for `50` and `"2nd"` and `40` and
`"3rd"`). Finally, if their `avg_percent` doesn't pass any of the previous
conditions, they must have failed, so you must `print "Fail."` as before.

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    Modify your <code>if</code> statement from before to print out the grade
    according to the percent, as described above.
  </div>
</div>

## While Statements

We have met the `for` loop before, and seen that it is useful for traversing
lists of things.

The `while` statement is also similar: it is a kind of loop, and it looks a bit
like this:

    while this_is_true:
        keep_doing_this()

So it keeps looping through its body, until its condition (`this_is_true`) no
longer holds.

As you may have guessed, this means that `keep_doing_this()` should probably
change something to make sure that `this_is_true` stops being true, otherwise,
the loop will go on forever (in general, not good...).

As a concrete example, here is the `for` loop from earlier, that prints out the
numbers from 0 to 5, but this time as a `while` loop:

    count = 0
    while count < 6:
        print count
        count = count + 1

Which outputs the following when run (same as before):

    0
    1
    2
    3
    4
    5

**Note:** You may not have seen the notation `count = count + 1` before, but it
is fairly common in programming, and it means "count *becomes* count + 1", as
opposed to being an equivalence (like in maths), because obviously, if the
latter were the case, we could subtract `count` from both sides and be left with
`0 = 1`.

As you can see, the body of the `while` loop does something to bring the
condition (in this case `count < 6`) closer to being false at every iteration,
by increasing the value of `count` by 1 (also called incremeneting `count`).

So if `while` loops are the same as `for` loops, except with the added pain that
you have to watch that they don't go on forever, then what's the point of them?

Well, consider this: What if you are creating a list, and you don't know how
many items are going to go in it? You couldn't use a `for` loop because you
don't know what to give it as the range, but you could use a `while` loop
instead, and check whether the user has typed in `"STOP"` last time.

To illustrate this, let us allow the user to input which courses they wish to
calculate their grades for, rather than using the preset list we have been using
so far.

In your `results_calculator.py` script, replace:

    courses = ["Learn to Cook",
               "Learn to Code",
               "Learn to Dance"
              ]

With this:

    courses    = []
    prev_input = BLANK_1

    while prev_input != BLANK_2:
        prev_input = raw_input()
        courses.append(prev_input)


<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
    Fill in the blanks in the code listing above to make the while loop work
    as described. Then, print the <code>courses</code> list at the end to ensure
    that it contains exactly the elements you expected.
    </p>
    <p>
    <strong>Hint 1</strong> we need to fill <code>prev_input</code> with
    something to begin with, so that when the <code>while</code> loop starts,
    it has something to check its condition with.
    </p>
    <p>
    <strong>Hint 2</strong> we had decided that if the user inputted
    <code>"STOP"</code>, then we would stop the loop.
  </div>
</div>

Practically speaking, `while` loops can do everything that `for` loops can do
and vice versa too, but you don't need to know the ins and outs of them just
yet. It's a fairly good rule of thumb that if you want to go through the items
of some collection (a range of numbers, a list and later on dictionaries), then
you want a `for` loop, and otherwise, you may want to consider a `while` loop.

## The `bool` Type

(explaining that they've already been using booleans)

## Functions

Start by typing to following into your text editor:

    def sayhi():
        print "hi"

    sayhi()
    sayhi()

Interesting! We just defined a "function" called "sayhi", 
you can call a function by using its name followed by 
parantheses, in this case `sayhi()`
Lets try another!

    def absolute(x):
        if(x>0):
            return x
        else:
            return -x

    print absolute(5)
    print absolute(-5)

This function, called "absolute" takes a parameter x.
When the function is called, e.g. `absolute(5)` then 
the occurence of x in replaced by the value 5, and the 
function is executed.
It turns out that functions are in fact not new, you've 
been using loads of them! `print`, `len`, `raw_input`, 
`range`, and even `turtle.right` are all functions!
Functions are a really useful way of taking a chunk of 
code, giving it a name, and making it re-useable.
Lets finish with one more function, try this one:

    def max(x,y):
        if(x>y):
            return x;
        else:
            return y;

    print max(5,6)

As an extra challenge, can you create a function called 
max_array which takes in an array of ints, and returns the 
largest int in the array. Hint: use a for loop!