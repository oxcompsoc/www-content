[meta title="Lesson 4: Doing Useful Things - Processing Data" /]

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
* [Dictionaries](../lesson_3/#Dictionaries)
* [Functions](../lesson_3/#Functions)

And we've asked you to write a small game using these skills, giving you less
guidance throughout that task.

Hopefully at this stage, you should feel quite confident with each of these. If
there is something that you are not 100% sure about, have a quick read over
that section.

## The Goal of This Lesson

This lesson will get you to use these techniques in a number of tasks of
increasing difficulty. The goal is that hopefully, practicing these techniques
over and over again to solve different problems will enable you to work out how
you can approach solving real-life problems you will come accross while coding
in the wild.

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

* #### [Task 1: Minimum Item of a List](#Task_1)
* #### [Task 2: Maximum Item of a List](#Task_2)



<a id="Task_1"></a>
## Task 1: Minimum Item of a List

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



<a id="Task_2"></a>
## Task 2: Maximum Item of a List

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


<a id="Task_3"></a>
## Task 3: Check if inside list

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



<a id="Task_4"></a>
## Task 4: Number of Instances in a List

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
