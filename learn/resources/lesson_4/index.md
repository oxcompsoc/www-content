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

**Hint:** You will probably want to have a `for` loop inside a `for` loop fo
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

Create a function `flatten_list`, that, when given a list of lists, produces
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

<br/><a id="Task_17"></a>
### Task 17: Removing the smallest element

<br/><a id="Task_18"></a>
### Task 18: Selection sort

<br/><a id="Task_19"></a>
### Task 19: Partitioning a list

<br/><a id="Task_20"></a>
### Task 20: Quicksort
