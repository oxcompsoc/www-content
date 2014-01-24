[meta title="Lesson 3: Doing Useful Things - Processing Data" /]

[embed page="/learn/resources/highlight.js/embed" /]

## Our Progress so Far...

So we've taught you some of the basics behind writing computer programs:

* Creating a python program as a
  [`.py` text file](../lesson_1/#First_Python_File) (with a text editor), and
  running it
* [Variables](../lesson_1/#Variables) (and
  [manipulating them](../lesson_2/#Manipulating_Variables))
* [Mathematical Operations](../lesson_1/#Mathematical_Operations)
* [Types](../lesson_2/#Types)
* [String Manipulation](../lesson_2/#Manipulating_Strings)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop)
* [**while** loops](../lesson_2/#While_Loop)
* [**if** Statements](../lesson_2/#If_Statements) and
  [**booleans**](../lesson_2/#Bool_Type)
* Console [Input](../lesson_2/#Console_Input) and
  [Output](../lesson_2/#Console_Output)

Hopefully at this stage, you should feel quite confident with each of these. If
there is something that you are not 100% sure about, have a quick read over
that section.

## The Goal of This Lesson

This lesson will get you to use these techniques in a number of tasks of
increasing difficulty. The goal is that hopefully, practicing these techniques
over and over again to solve different problems will enable you to work out how
you can approach solving real-life problems you will come accross while coding
in the wild.

Before starting the main tasks, there is one last thing we would like to
introduce to you...

## Functions

Start by typing to following into your text editor, then run it in python:

    def sayhi():
        print "hi"

    sayhi()
    sayhi()

We just defined a "function" called `sayhi`. You can call a function by using
its name followed by parentheses. In this case, it's `sayhi()`.

Just like with loops and if statements, here the indentation is important. The
**"body"** of the function is all the code indented to the right immediately
below the function name.

So what is going on in the above example?

Well, the first two lines are simply **defining** a function. That means that
the `print "hi"` code (the **body** of the function), does not actually run.
Python knows that it should run the code inside the **body** of the function
only when you type `sayhi()` to use the function. *(This is called "calling"
the function).*

The following two `sayhi()`s are where the message actually gets printed.
Every time python sees a function name followed by brackets, it looks for that
function's definition, runs it in the name's position, and then continues
running the code after the function name.

If this seems complicated, just imagine that when python sees a function name,
it puts the code of the function definition in its place and runs that instead.
That is basically what happens, but as you will see in the "Variable Scoping"
section, there are some more things to take into account.

In this example you can see one of the advantages of functions straight away:
We wrote the code once, but we can use it however many times we want. This
means that if that code were to change, and we had used it in multiple places,
rather than tracking down every place it's been used and changing it there, we
need only change it in one place: the function **definition**. Afterwards we
can be sure that everywhere the function is used will now be using the updated
code.

#### Introducing parameters

Lets look at a slightly different function:

    def absolute(x):
        if(x > 0):
            return x
        else:
            return -x

    print absolute(5)
    # => 5

    print absolute(-5)
    # => 5

This function, called `absolute` takes a parameter `x`. When the function is
called, for example with  `absolute(5)`, then `x` is assigned the value `5`,
and the function is run from top to bottom, just like a function with no
parameters.

**Parameters** are basically the same as **variables**, with a few subtle
differences. Parameters are created and assigned when you **call** a function,
and when the function is finished they are disposed of. Other than this they
are the same, you can even change the values of parameters!

#### Return values

This function also introduced the `return` keyword, which lets a function stop
executing immediately, and return a result to the code that initially called
the function.

If python executes `absolute(5)`, then after checking `x > 0`, which is true
(because, remember `x` is `5`), python will see the line `return x`.
This means it will stop executing the function, and return the value of `x`
(which is `5`). So if we write `print absolute(5)` then as `absolute(5)`
returns `5`, we expect python to `print 5`.

The next time we run the `absolute` function, we give it `-5` as the parameter.
Which makes `x > 0` no longer true, resulting in the line `return -x` being
run. Because `x` is `-5`, `-x` is just `5` (positive 5), so we get python
printing `5` again.

#### Defining a function

We write `def functionName(param1, param2, ...):` to define a function, making
sure we include some indented code afterwards that serves as the body.

* You can have zero or more parameters.
* Add in the function code below the definition, remembering to indent it
  further right than the definition (by atleast 4 spaces).

#### Calling a function

To call a function, write `functionName(value1, value2)`.

This has the effect of running the code in the function, with `param1` equal to
the value `value1`, and likewise for any other parameters.

You'll often hear the terms "argument" and "parameter" used when talking about
functions. In this example `param1` is a "parameter" because it is in the
function definition (`def functionName(param1, param2, ...):`).

In the above example of a function call, we call `value1` an "argument" to the
function. When the function is run, we say that "the parameter `param1` will
take the value `value1`". Functions may seem complicated at first, but they
will begin to feel more natural the more you use them.

#### Feeling familiar?

It turns out that functions are in fact not new, you've been using loads of
them! `len`, `raw_input`, `range`, and even `turtle.right` are all functions!
Functions are a really useful way of taking a chunk of code, giving it a name,
and making it reusable.

#### Creating your own function

Here is a function that takes two numbers and returns the maximum of the two:

    def max(x,y):
        if(x > y):
            return x;
        else:
            return y;

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Challenge</strong></div>
  <div class="panel-body">
    Can you create a function called <code>max_list</code> which takes in a
    list of <code>ints</code> as a parameter, and returns the largest
    <code>int</code> in the list.
    <br/>
    <strong>Hint</strong> use a <code>for</code> loop! You may need to look
    over materials in the previous lessons to remind yourself.
  </div>
</div>

#### Variables and their scope

Lastly, we need to talk about using and defining variables inside a function.

When we call a function, like `max(1, 3)`, then as we discussed, the parameters
`x` and `y` (which are also variables) get assigned to the values `1` and `3`.
Now these variables are interesting, because they only exists inside the
function. So from outside the function, there is no way to access the values
`x` or `y`. This actually makes a lot of sense, because they only ever get
assigned values when the function is called. This happens because of something
called **variable scope**. All variables have a scope, but it becomes
particularly noticeable in functions. It's best to see how this works by
examples:

    def print_and_add_one(number):
        print(number)
        return number + 1

    def main():
        x = 1
        print_and_add_one(x)
        x = print_and_add_one(x)
        print(x)

    main()
    # print(number)
    # print(x)

This example shows the important behaviour of scoped variables. What do you
think the output will be? Now run the code, and try uncommenting the lines
`# print(number)` and `# print(x)` to see what happens.

The `print_and_add_one` function only accesses the variable number, and this is
allowed, since number is a paramter to the function. In some cases, functions
can access variables that are not one of their parameters, but this is strongly
discouranged as it can lead to confusion.

Lets go through this example line by line as python would.

* When python runs this code, it firstly sees a function defition for
  `print_and_add_one`. It remembers that its seen the function, and then moves
  on to below the function.
* Now it sees a function definition for `main`, and again moves on.
* Then python sees the function call `main()` so it jumps to the function
  `main` and starts executing the code inside the function.
    * Firstly it assigns the value `1` to `x`, but because python is in a new
      scope (indicated by the fact we are in a new function), it notes tha
      when it leaves this scope, it will forget everything about `x`.
    * Then it moves forwards to the next line, and sees a function call to
      `print_and_add_one(x)` so python remebers the current line (for later),
      and jumps to the function `print_and_add_one`, assigning `number` the
      value of `x` (which is `1`).
        * Inside the body of `print_and_add_one`, it prints the current value
          of `number` (which is `1`).
        * Python then returns the value `number + 1`, which is `2` and notes
          that it has finished this function, so it jumps back to where it was
          before.
    * It was previously at the line `print_and_add_one(x)`, and python sees
      that it can discard the returned value (`2`) from the function, since we
      do not use it here.
    * Now it moves forwards another line, and again sees another function call
      of `print_and_add_one`, so again that function is executed (exactly as
      before).
    * This time, because the line says `x = print_and_add_one(x)`, python
      assigns `x` the returned value of the function (`2`).
    * After executing the function, python will then print the new value of
      `x`.

Now, the line `#print(number)` is commented, so python ignores that. The reason
we cannot print the value `number`, is because that variable is "forgotten"
when python leaves the `print_and_add_one` funtion. Similarly, when python
leaves the `main` function, all new variable assignments are forgotten about,
which is why we cannot `print(x)` after we have left the `main` function.

So when python changes out of a functions scope, any newly introduced variables
(in that function) are forgotten.

If that didn't make sense then try reading it through a few times, and refer
constantly to the code to see how python is moving through the code, and what
is happening to the variables at each line. If it still doesn't make sense,
then ask a helper to explain!

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    Try creating some more functions and experiment with what variables you
    can, and cannot access when the code is inside and outside a function.
  </div>
</div>

## The Tasks

The tasks given in this lesson are the kind of things you will come accross
when trying to write *almost any program*. When you are writing a program,
whether it is a smartphone app, a computer program, something controlling a
radio-controlled hellicopter, or even just a website... you will **need to
process data**.

Being able to come up with code that can process data in a particular way is a
**vital skill** to being a good programmer, and you can only get better with
**more practice and experience**.

All of these tasks come with **Test Code** that checks to see if the final code
of the task works as expected.

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Note</strong></div>
  <div class="panel-body">
    We <strong>strongly recommend</strong> you save your answer to each task as
    a separate file! Create a new folder called <code>lesson_4</code> and save
    each of the tasks in there. For example, use the filename
    <code>001.py</code> for the first task.
  </div>
</div>

Here's a list of the tasks for this lesson, we recommend you **try them in
order** as they have increasing difficulty and less hints as you go on.

#### [Tasks 1-4: Basic `for` Loops](#Tasks_1_to_4)

* [Task 1: Minimum Item of a List](#Task_1)
* [Task 2: Maximum Item of a List](#Task_2)
* [Task 3: Check if inside list](#Task_3)
* [Task 4: Number of Instances in a List](#Task_4)

#### [Tasks 5-8: Basic `while` Loops](#Tasks_5_to_8)

* [Task 5: Minimum Item of a List (Using a `while` Loop)](#Task_5)
* [Task 6: Maximum Item of a List (Using a `while` Loop)](#Task_6)
* [Task 7: Check if inside list (Using a `while` Loop)](#Task_7)
* [Task 8: Number of Instances in a List (Using a `while` Loop)](#Task_8)

#### [Tasks 9-12: More `for` Loops](#Tasks_9_to_12)

* [Task 9: Sum the elements in a list](#Task_9)
* [Task 10: All True?](#Task_10)
* [Task 11: At least one True?](#Task_11)
* [Task 12: Sum the values of lists of lists](#Task_12)

#### [Tasks 13-16: Improving `sum_list_of_lists`](#Tasks_13_to_16)

* [Task 13: Flatten a list of lists](#Task_13)
* [Task 14: Using `sum_list` in `sum_list_of_lists`](#Task_14)
* [Task 15: Using `flatten` in `sum_list_of_lists`](#Task_15)
* [Task 16: Generalising `flatten`](#Task_16)

#### [Tasks 17-20: Sorting lists](#Tasks_17_to_20)

* [Task 17: Removing the smallest element](#Task_17)
* [Task 18: Selection sort](#Task_18)
* [Task 19: Partitioning a list](#Task_19)
* [Task 20: Quicksort](#Task_20)

#### [Advanced Tasks](#Advanced)

<br/><a id="Tasks_1_to_4"></a>
## Tasks 1-4: Basic `for` Loops

Tasks 1-4 will be performing calculations on lists using `for` loops.

<br/><a id="Task_1"></a>
### Task 1: Minimum Item of a List

#### Instructions:

Write a function `min_list` that when given a list of numbers, will find the
minimum number in the list. Do this using a `for` loop.

#### What you need to know:

* [Variables](../lesson_1/#Variables) (and
  [manipulating them](../lesson_2/#Manipulating_Variables))
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop)
* [**if** Statements](../lesson_2/#If_Statements)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def min_list(lst):
        min = ... # What should we set this value to to begin with?

        for item in lst: # iterate over every item in the list
            print item # print statement to show you what's happening
            ... # What needs to go here?

        return min

    # Test Code
    print "Testing..."

    print min_list([5, 2, 7, 1, 9]) # This should be 1
    print min_list([5, 2, -7 ,1 ,9]) # This should be -7
    print min_list([900]) # This should be 900
    print min_list([-900]) # This should be -900

#### Expected Output

    1
    -7
    900
    -900



<br/><a id="Task_2"></a>
### Task 2: Maximum Item of a List

#### Instructions:

Write a function `max_list` that when given a list of numbers, will find the
maximum number in the list. Do this using a `for` loop.

#### What you need to know:

* [Variables](../lesson_1/#Variables) (and
  [manipulating them](../lesson_2/#Manipulating_Variables))
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop)
* [**if** Statements](../lesson_2/#If_Statements)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def max_list(lst):
        ...

    # Test Code
    print "Testing..."

    print max_list([5, 2, 7, 1, 9]) # This should be 9
    print max_list([-7, -3, -8]) # This should be -3
    print max_list([900]) # This should be 900
    print max_list([-900]) # This should be -900

#### Expected Output

    9
    -3
    900
    -900


<br/><a id="Task_3"></a>
### Task 3: Check if inside list

#### Instructions:

Write a function `in_list` that when given a list of values (doesn't need to
be numbers), and a value `x`, returns `True` if the value is inside the list,
otherwise it returns `False`.

**Note: You are not allowed to use the python `in` operator.**

#### What you need to know:

* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop)
* [**if** Statements](../lesson_2/#If_Statements)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def in_list(lst, x):
        ...

    # Test Code
    print "Testing..."

    print in_list([1, 2, 2, 6, 2, 9], 2) # This should be True
    print in_list([1, 2, 2, 6, 2, 9], 1) # True
    print in_list([1, 2, 2, 6, 2, 9], 9) # True
    print in_list([1, 2, 2, 6, 2, 9], 10) # False
    print in_list([1, 2, 2, 6, 2, 9], "cat") # False
    print in_list([1, 2, 2, 6, 2, 9, "cat"], "cat") # True
    print in_list(["cat"], "cat") # True
    print in_list(["cat", [1], [2, 3]], [1]) # True
    print in_list(["cat", [1], [2, 3]], [2]) # False

#### Expected Output

    True
    True
    True
    False
    False
    True
    True
    True
    False



<br/><a id="Task_4"></a>
### Task 4: Number of Instances in a List

#### Instructions:

Write a function `instances` that when given a list of values (doesn't need to
be numbers), and a value `x`, returns the number of times that `x` appears in
the list. Do this using a `for` loop.

#### What you need to know:

* [Variables](../lesson_1/#Variables) (and
  [manipulating them](../lesson_2/#Manipulating_Variables))
* [Mathematical Operations](../lesson_1/#Mathematical_Operations)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop)
* [**if** Statements](../lesson_2/#If_Statements)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def instances(lst, x):
        ...

    # Test Code
    print "Testing..."

    print instances([1, 2, 2, 6, 2, 9], 2) # This should be 3
    print instances([1, 2, 2, 6, 2, 9], 1) # 1
    print instances([1, 2, 2, 6, 2, 9], 9) # 1
    print instances([1, 2, 2, 6, 2, 9], 10) # 0
    print instances([], 1) # 0
    print instances(["dog", "cat", "cat", 1, 2, 3, "horse"], "cat") # 2
    print instances([[1], [2], [2, 3], [1]], [1]) # 2
    print instances([[1], [2], [2, 3], [1]], [2]) # 1
    print instances([[1], [2], [2, 3], [1]], [3]) # 0

#### Expected Output

    3
    1
    1
    0
    0
    2
    2
    1
    0



<br/><a id="Tasks_5_to_8"></a>
## Tasks 5-8: Basic `while` Loops

Tasks 5-8 will be doing tasks 1-4 but using `while` loops instead of `for`
loops.

Whenever you write a `for` loop, you can convert your code to use a `while`
loop instead!

**Example:**

    for item in my_list:
        print item

Is the same as

    index = 0
    while index < len(my_list):
        item = my_list[index]
        print item

        index += 1

Basically, a `for` loop is a special kind of `while` loop that makes writing
some code look much nicer. For the following exercises, we want you to use the
technique given in the example above to try and understand what the `for` loop
is doing, and convert it to a more complicated `while` loop.



<br/><a id="Task_5"></a>
### Task 5: Minimum Item of a List (Using a `while` Loop)

#### Instructions:

Do the same as [Task 1](#Task_1), except using a `while` loop instead of a
`for` loop.

#### What you need to know:

* Everything for [Task 1](#Task_1)
* [**while** loops](../lesson_2/#While_Loop)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def min_list(lst):
        min = ... # What should we set this value to to begin with?

        index = 0
        while index < len(lst):
            item = lst[index]
            print item

            ... # What goes here?

            index += 1

        return min

    # Test Code
    print "Testing..."

    print min_list([5, 2, 7, 1, 9]) # This should be 1
    print min_list([5, 2, -7 ,1 ,9]) # This should be -7
    print min_list([900]) # This should be 900
    print min_list([-900]) # This should be -900

#### Expected Output

Same as [Task 1](#Task_1)



<br/><a id="Task_6"></a>
### Task 6: Maximum Item of a List (Using a `while` Loop)

#### Instructions:

Do the same as [Task 2](#Task_2), except using a `while` loop instead of a
`for` loop.

#### What you need to know:

* Everything for [Task 2](#Task_2)
* [**while** loops](../lesson_2/#While_Loop)

#### Boilerplate Code and Expected Output:

Same as [Task 2](#Task_2)



<br/><a id="Task_7"></a>
### Task 7: Check if inside list (Using a `while` Loop)

#### Instructions:

Do the same as [Task 3](#Task_3), except using a `while` loop instead of a
`for` loop.

#### What you need to know:

* Everything for [Task 3](#Task_3)
* [**while** loops](../lesson_2/#While_Loop)

#### Boilerplate Code and Expected Output:

Same as [Task 3](#Task_3)



<br/><a id="Task_8"></a>
### Task 8: Number of Instances in a List (Using a `while` Loop)

#### Instructions:

Do the same as [Task 4](#Task_4), except using a `while` loop instead of a
`for` loop.

#### What you need to know:

* Everything for [Task 4](#Task_4)
* [**while** loops](../lesson_2/#While_Loop)

#### Boilerplate Code and Expected Output:

Same as [Task 4](#Task_4)



<br/><a id="Tasks_9_to_12"></a>
## Tasks 9-12: More `for` Loops



<br/><a id="Task_9"></a>
### Task 9: Sum the elements in a list

#### Instructions:

Create a function `sum_list` that, when given a list of numbers, will return
the sum of all of the numbers in that list

#### What you need to know:

* [Variables](../lesson_1/#Variables) (and
  [manipulating them](../lesson_2/#Manipulating_Variables))
* [Mathematical Operations](../lesson_1/#Mathematical_Operations)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop) or
  [**while** loops](../lesson_2/#While_Loop)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def sum_list(lst):
        ...

    # Test Code
    print "Testing..."

    print sum_list([]) # 0
    print sum_list([1]) # 1
    print sum_list([-1]) # -1
    print sum_list([1, 2, 3, 4, 5]) # 15
    print sum_list([1, 2, 3, 4, 5, -4, -3, -2, -1]) # 5

#### Expected Output

    0
    1
    -1
    15
    5



<br/><a id="Task_10"></a>
### Task 10: All True?

#### Instructions:

Create a function `all_true` that, when given a list of values, will return
`False` if there are any values in the list that are `False`, otherwise it
should return `True`.

#### What you need to know:

* [Variables](../lesson_1/#Variables)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop) or
  [**while** loops](../lesson_2/#While_Loop)
* [**if** Statements](../lesson_2/#If_Statements) and
  [**booleans**](../lesson_2/#Bool_Type)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def all_true(lst):
        ...

    # Test Code
    print "Testing..."

    print all_true([]) # True
    print all_true([True]) # True
    print all_true([False]) # False
    print all_true([True, False]) # False
    print all_true([False, True]) # False
    print all_true([True, True]) # True

#### Expected Output

    True
    True
    False
    False
    False
    True






<br/><a id="Task_11"></a>
### Task 11: At least one True?

#### Instructions:

Create a function `one_true` that, when given a list of values, will return
`True` only if there is at least one value in the list that is `True`.

#### What you need to know:

* [Variables](../lesson_1/#Variables)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop) or
  [**while** loops](../lesson_2/#While_Loop)
* [**if** Statements](../lesson_2/#If_Statements) and
  [**booleans**](../lesson_2/#Bool_Type)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def one_true(lst):
        ...

    # Test Code
    print "Testing..."

    print one_true([]) # False
    print one_true([True]) # True
    print one_true([False]) # False
    print one_true([True, False]) # True
    print one_true([False, False]) # False
    print one_true([False, True]) # True
    print one_true([True, True]) # True

#### Expected Output

    False
    True
    False
    True
    False
    True
    True


<br/><a id="Task_12"></a>
### Task 12: Sum the values of lists of lists

#### Instructions:

Create a function `sum_list_of_lists`, that, when given a list of lists, will
sum all of the values inside all of the lists together, and return the value.

**Hint:** You will probably want to have a `for` loop inside a `for` loop for
this task.

#### What you need to know:

* [Variables](../lesson_1/#Variables)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop) or
  [**while** loops](../lesson_2/#While_Loop)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`).

    def sum_list_of_lists(lst):
        ...

    # Test Code
    print "Testing..."

    print sum_list_of_lists([]) # 0
    print sum_list_of_lists([[], []]) # 0
    print sum_list_of_lists([[1], [2]]) # 3
    print sum_list_of_lists([[1, 2], [3]]) # 6
    print sum_list_of_lists([[1, 2], [3], [], [4, 5]]) # 15
    print sum_list_of_lists([[1, 2], [3], [-5], [4, 5]]) # 10

#### Expected Output

    0
    0
    3
    6
    15
    10

<br/><a id="Tasks_13_to_16"></a>

## Tasks 13-16: Improving `sum_list_of_lists`

<br/><a id="Task_13"></a>
### Task 13: Flattening a list of lists

#### Instructions:

Create a function `flatten`, that, when given a list of lists, produces
a list containing the same elements, all in one list.

i.e. `[[1, 2], [3]]` becomes `[1, 2, 3]`

#### What you need to know:

* [Variables](../lesson_1/#Variables)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop) or
  [**while** loops](../lesson_2/#While_Loop)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`)

    def flatten(lst):
        acc = [] # The accumulating list
        ...
        return acc

    # Test Code
    print "Testing"

    print flatten([]) # []
    print flatten([[], []]) # []
    print flatten([[1], [2]]) # [1, 2]
    print flatten([[1, 2], [3]]) # [1, 2, 3]
    print flatten([[1, 2], [3], [], [4, 5]]) # [1, 2, 3, 4, 5]

<br/><a id="Task_14"></a>
### Task 14: Using `sum_list` in `sum_list_of_lists`

#### Instructions:

When writing your first implementation of `sum_list_of_lists` you may have
written the function using nested loops (one `for` or `while` loop inside
another). However, your inside for loop, looks suspiciously similar to the loop
inside `sum_list`.

Why is that? It's because they are both doing the same thing: Summing a list to
produce a number. This means your inner loop can be replaced with `sum_list`.

Perform the replacement in your version of `sum_list_of_lists` and make sure the
behaviour remains unchanged.

#### What you need to know:

 * [Functions](../lesson_3/#Functions)

#### Boilerplate Code and Expected Output

Same as for [Task 12](#Task_12)

<br/><a id="Task_15"></a>
### Task 15: Using `flatten` in `sum_list_of_lists`

#### Instructions:

If you compare the outputs of `flatten` and `sum_list_of_lists` on the same
lists, you may notice a pattern: If you sum the result of `flatten` you get
the result of `sum_list_of_lists`. This happens to always be true, and we can
take advantage of this fact to make `sum_list_of_lists` **even** shorter.

Replace the definition of `sum_list_of_lists` with calls to `flatten` and
`sum_list`, making sure the behaviour stays the same once again.

#### What you need to know:

 * [Functions](../lesson_3/#Functions)

#### Boilerplate code and Expected Output:

Same as for [Task 12](#Task_12)

<br/><a id="Task_16"></a>
### Task 16: Generalising `flatten`

#### Instructions:

What if you wanted to define a function called `sum_nested_lists`, which sums
the elements of a list, no matter how deeply they are nested, (even if they
aren't nested to the same level)?

We can simplify this problem into one we understand: summing a single list. We
do this by once again flattening the inputted list so it has no nested lists,
but still contains the same elements.

But if we give our current flatten function a list like `[[1, 2], 3]`, it would
complain, because the outer list doesn't contain all lists. And furthermore, if
we tried to give it a list like `[[[1, 2], [3]], [[4, 5], [6]]]` then it would
also break because the lists are nested more deeply than it is designed to deal
with.

We need to create a function that checks the types of all the elements that it
sees, before adding them  to `acc`. And if the item is a list, we should
flatten it too, before adding its elements.

#### What you need to know:

* [Variables](../lesson_1/#Variables)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop) or
  [**while** loops](../lesson_2/#While_Loop)
* [Functions](../lesson_3/#Functions)

#### Boilerplate:

Replace all of the ellipses (`...`)

    def flatten(lst):
        acc = [] # The accumulating list
        for x in lst:
            if type(x) == list:
                ... # Flatten it before adding
            else:
                ... # Append the element

        return acc

    def sum_nested_lists(lst):
        ... # Same as for `sum_list_of_lists` after task 15.

    # Test Code
    print "Testing"

    print sum_nested_lists([]) # 0
    print sum_nested_lists([[], []]) # 0
    print sum_nested_lists([1, 2, 3]) # 6
    print sum_nested_lists([[[]], []]) # 0
    print sum_nested_lists([[1, 2], 3]) # 6
    print sum_nested_lists([[1, 2], [3, []], [[[4]]]]) # 10

#### Expected Output:

    0
    0
    6
    0
    6
    10

<br/><a id="Tasks_17_to_20"></a>
## Tasks 17-20: Sorting lists

Sorting lists is a task that a lot of time has been spent trying to master, in
the computing world. There are several ways to sort lists, but we are going
to look at some simple options here that are easy to understand.

Neither of the implementations you reach will be perfect or very efficient, but
they will capture the essence of the task (the *algorithm*) and they will work.
The first algorithm is rarely used in the real world, although the second is
very popular, in some of its other forms.

<br/><a id="Task_17"></a>
### Task 17: Removing the smallest element

#### Instructions:

Create a function called `remove_min` that, when given a list, finds its minimal
element and deletes it from the list, returning the element it deleted.

You will find that this function is very similar to your previous function,
`min_list`, and you can use this fact to guide you in the implementation of
`remove_min`.

We will use this function later on, in a sorting algorithm called *selection
sort*.

#### What you need to know:

 * [Variables](../lesson_1/#Variables)
 * [Lists](../lesson_2/#Lists)
 * [**while** loops](../lesson_2/#While_Loop)
 * [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all of the ellipses (`...`)

**Note:** the `del` command, introduced for dictionaries, also works for lists
in the natural way: `del lst[2]` will remove the element at index 2.

**Note:** you may find it helpful to use a `while` loop in this task because you
will need to keep track of the index of the minimal element as well as the
element itself, so you can delete it.

    def remove_min(lst):
        if len(lst) == 0: return # Nothing to remove for empty lists

        min_i = 0
        min   = lst[0]
        i     = 1

        ... # Loop through the list, finding the smallest element
        ... # Delete the minimal element
        return min

    # Test Code
    print "Testing"

    test = [3,4,8,9,7]
    print remove_min(test), test # 3 [4, 8, 9, 7]
    print remove_min(test), test # 4 [8, 9, 7]
    print remove_min(test), test # 7 [8, 9]
    print remove_min(test), test # 8 [9]
    print remove_min(test), test # 9 []

<br/><a id="Task_18"></a>
### Task 18: Selection sort

#### Instructions:

If you look at the output from the testing of `remove_min` you will see
that succesive calls to `remove_min` return the elements of list in
increasing order. We can exploit this in our sorting algorithm: We remove the
minimal element from the list, until there are no elements left, appending each
in turn to the end of a new list.

#### What you need to know:

 * [Variables](../lesson_1/#Variables)
 * [Lists](../lesson_2/#Lists)
 * [**while** loops](../lesson_2/#While_Loop)
 * [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all the ellipses (`...`)

    def selection_sort(lst):
        sorted = []
        list_len = len(lst) # Store this now because our loop will make it
                            # smaller

        ... # Loop through the list removing minimal elements from `lst` and
            # appending them to `sorted`.

        return sorted

    # Test Code
    print "Testing"

    selection_sort([]) # []
    selection_sort([1, 2, 3]) # [1, 2, 3]
    selection_sort([3, 4, 8, 9, 7]) # [3, 4, 7, 8, 9]
    selection_sort([-8, 8, 4, -4, -2, 2]) # [-8, -4, -2, 2, 4, 8]

#### Expected Output:

    []
    [1, 2, 3]
    [3, 4, 7, 8, 9]
    [-8, -4, -2, 2, 4, 8]

<br/><a id="Task_19"></a>
### Task 19: Partitioning a list

#### Instructions:

Partitioning involves taking a list, and producing two lists that together
contain all the elements of the original in such a way that all the elements in
one list are the elements less than some provided value (which we will call the
`pivot`) and all the elements in the other list are greater than or equal to the
`pivot`.

#### What you need to know:

* [Variables](../lesson_1/#Variables)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop) or
  [**while** loops](../lesson_2/#While_Loop)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace all the ellipses (`...`)

    def partition(pivot, lst):
        lt, gte = [], [] # Less than, and greater than or equal to lists

        ... # Loop through lst, filling `lt` and `gte`

        return lt, gte

    # Test Code
    print "Testing"

    print partition(0, []) # ([], [])
    print partition(1, [1, 2, 3]) # ([], [1, 2, 3])
    print partition(2, [1, 2, 3]) # ([1], [2, 3])
    print partition(4, [1, 2, 3]) # ([1, 2, 3], [])

#### Expected Output:

    ([], [])
    ([], [1, 2, 3])
    ([1], [2, 3])
    ([1, 2, 3], [])

<br/><a id="Task_20"></a>
### Task 20: Quicksort

#### Instructions:

Quicksort is a popular sorting algorithm that relies upon the principle of
partitioning lists.

 * Given a particular pivot element in the list (for convenience, let us just
   use the first element) partition the **rest** of the list according to the
   pivot.
 * Now if we slot the pivot element in between the elements less than it and
   greater than or equal to it, we find the pivot is in the *right place in the
   list*.
 * But the two lists provided by partition are not in sorted order, so how do we
   deal with them? Well, we use our `quicksort` function to sort those too.
 * Additionally, we say that lists with one or fewer elements are trivially
   sorted, so we can just return them without doing any work.

Use the hints above to define a function `quicksort` that uses partition to sort
the list provided to it.

#### What you need to know:

* [Variables](../lesson_1/#Variables)
* [Lists](../lesson_2/#Lists)
* [**for** loops](../lesson_2/#For_Loop) or
  [**while** loops](../lesson_2/#While_Loop)
* [Functions](../lesson_3/#Functions)

#### Boilerplate Code:

Replace the ellipses (`...`)

**Note:** It may be useful to know that python has a feature that allows you to
access a part of a list, i.e. `lst[n:]` means the elements from index
`n` onwards. This may be useful when trying to get all the elements bar the
first (which we use as the pivot).

    def quicksort(lst):
        # Lists of length 1 or 0 are already sorted, just return them
        if len(lst) <= 1: return lst

        pivot = ... # The first element
        left, right = partition(pivot, ...) # Partition the rest of the list

         # Sandwich the pivot between the sorted left and right sides
        return ... + [pivot] + ...

    # Test Code
    print "Testing"

    quicksort([]) # []
    quicksort([1, 2, 3]) # [1, 2, 3]
    quicksort([3, 4, 8, 9, 7]) # [3, 4, 7, 8, 9]
    quicksort([-8, 8, 4, -4, -2, 2]) # [-8, -4, -2, 2, 4, 8]

#### Expected Output:

Same as for [Task 18](#Task_18)


<br/><a id="Advanced"></a>
## Advanced Tasks

Congratulations if you have got this far and completed all of the tasks, we
have not actually added any more of our own tasks, but you are probably ready
to have a go at some challenges from [Project
Euler](http://projecteuler.net/problems). There will be plenty to keep you
going there!
