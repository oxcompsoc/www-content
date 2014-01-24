[meta title="Lesson 5: A Text-Based Adventure Game" /]

[embed page="/learn/resources/highlight.js/embed" /]

## The Goal of This Lesson

In this lesson, we will be taking a little bit of a different approach. We will
be working towards the goal of creating a text based adventure game. There will
be less guidance, so that you can try and use the skills that you have learned
in the lessons so far.

We will give you tasks to complete, and tips, and helpers will be available to
answer any questions during the lesson.

## Before we Start

There are a couple more interesting things that we would like to teach you
before getting started...

<a id="Dictionaries"></a>
### Introducing dictionaries

Try finding the type of `{'name': 'James', 'level':9001 }`. You'll see it's
something new, a `dict`.

The `dict` type is also referred to as a "dictionary" or "hashtable". They are a
comma separated list of keys and values in the form `key1:value1, key2:value2,
key3:value3, ...` surrounded by a pair of curly braces `{ ... }`.

#### Looking up values

Lets take a look at a larger example:

    mydict = {'name': 'James', 'level':9001}
    print(mydict['name'])
    print(mydict)

Can you see what's happening here?

Like lists, we can use square brackets to *index* a dictionary, so, just like
`elems[0]` will return the first element of the `elems` list, if we write
`mydict['name']` it means "Look inside `mydict`, access the key `'name'` and
give me its corresponding value". Similarly, we can replace the value
corresponding to the key `'name'` with `mydict['name'] = 'newvalue'`.

What happens if you try to access the value of a key that does not exist? Can
you use `=` to assign a value to a key the does not exist in the dictionary?

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
  What happens if you try to access the value of a key that does not exist?
  Can you use <code>=</code> to assign a value to a key the does not exist in the dictionary?
  </div>
</div>

As you saw in the task, we get a `KeyError` when we try to access a key that
doesn't exist.

#### Checking values exist

To get around this there is the `in` keyword. You can use `in` to tell you
whether a given key has a value in the dictionary and you can use `not in` to
do the opposite:

    mydict = { 'name': 'James', 'level': 9001 }

    'name'     in     mydict # => True
    'name'     not in mydict # => False
    'lastName' in     mydict # => False
    'lastName' not in mydict # => True

#### Adding values

As you saw in the task, it is however possible to assign a value to a key that
was not previously in the dictionary using `=`, for example:

    mydict = { } # The empty dictionary
    mydict['name'] = 'james'

    print(mydict)
    print(mydict['name'])

When the above is run, it should print the following:

    {'name': 'James'}
    James

The values can actually be any object, and in the example we mapped the `'name'`
key to a string and the `'level'` key to an integer. You can also have duplicate
values, so multiple keys can map to the same value. However you may not have
duplicate keys (E.g. Each key maps only to one value at a time):

    # Multiple keys with the same value (allowed)
    mydict = {'a': 1, 'b': 1}

    print mydict
    # => {'a': 1, 'b': 1}

    # Multiple values for the same key (not allowed)
    mydict = { 'a':1, 'a': 2}
    print mydict
    # => {'a': 2}

#### Modifying values

As you can see, python decided to automatically choose the last value assigned
to the `'a'` key, which was `2`. This behaviour is what allows you to
*overwrite* existing values in a dictionary, if you assign a value to a key that
already exists in the dictionary:

    mydict = {'name': 'Joe'}

    print mydict
    # => {'name': 'Joe'}

    mydict['name'] = 'James'

    print mydict
    # => {'name': 'James'}

#### Key value types

You can use more than just strings as keys in dictionaries, experiment with
other values as key types and see which ones work and which ones don't.

<div class="panel panel-primary">
    <div class="panel- heading"><strong>Task</strong></div>
    <div class="panel-body">
      <p>
        Find one type other than string that can be used for keys, and one type
        that cannot.
      </p>
      <p>
        <strong>Hint</strong> If you choose a key type that is not allowed you
        will get an error that begins <code>TypeError: unhashable type</code>
        and tells you the name of the type you tried to use.
    </div>
</div>

#### Deleting values

You can remove an entry from the dictionary using the `del` keyword:

    mydict = {'name': 'James', 'level': 9001}

    del mydict['name']

    print mydict
    # => {'level': 9001}

Watch out though! You'll get a `KeyError` if the key wan't in the dictionary
to begin with.

#### Uses of dictionaries

So why might we want to use a dictionary? In the game we'll be creating later,
we're going to need some way of keeping track of information regarding the
player. A dictionary is an ideal type for containing all information relevant to
the player in one place. We could have several separate variables, but that
rapidly gets tedious, especially when we throw functions into the mix.

<a id="Functions"></a>
### Functions

Start by typing to following into your text editor, then run it in python:

    def sayhi():
        print "hi"

    sayhi()
    sayhi()

We just defined a "function" called `sayhi`. You can call a function by using
its name followed by parentheses. In this case, it's `sayhi()`.

Just like with loops, here the indentation is important. The "body" of the
function is all the code indented to the right immediately below the function
name.

So what is going on in the above example?

Well, the first two lines are simply *defining* a function. That means that the
`print "hi"` does not actually happen. Python just knows that when you type
`sayhi()` then, it should print the message `"hi"`.

Then the following two `sayhi()`s are where the message actually gets printed.
Every time python sees a function name followed by brackets, it looks for that
function's definition, runs it in the name's position, and then continues
running the code after the function name.

If this seems complicated, just imagine that when python sees a function name,
it puts the code of the function definition in its place and runs that instead.
That is basically what happens, but as you will see in the "Variable Scoping"
section, there are some more things to take into account.

In this example you can see one of the advantages of functions straight away: We
wrote the code once, but we can use it however many times we want. This means if
that code were to change, and we had used it in multiple places, rather than
tracking down every place it's been used and changing it there, we need only
change it in one place: the function and we can be sure in the knowledge that
everywhere the function is used will now be using the changed code.

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
called, for example with  `absolute(5)`, then `x` is assigned the value `5`, and
the function is run from top to bottom, just like a function with no parameters.

#### Return values

This function also introduced the `return` keyword, which lets a function stop
executing immediately, and return a result to the code that initially called the
function.

If python executes `absolute(5)`, then after checking `x > 0`,
which is true (because, remember `x` is 5), python will see the line `return x`,
so it will stop executing the function, and return the value of `x` (which is
5). So if we write `print absolute(5)` then as `absolute(5)` returns `5`, we
expect python to `print 5`.

The next time we run the `absolute` function, we give it `-5` as the parameter.
Which makes `x > 0` no longer true, resulting in the line `return -x` being
called. Because `x` is -5, this makes `-x` +5 (or just 5), so we get python
printing `5` again.

#### Defining a function

We write `def functionName(param1, param2, ...):` to define a function.

 * You can have zero or more parameters.
 * Add in the function code below the definition, remembering to indent it
   further right than the definition (by atleast 4 spaces).

#### Calling a function

To call a function, write `functionName(value1, value2)`.

This has the effect of running the code in the function, with `param1` equal to
the value `value1`, and analogously for any other parameters.

You'll often hear the terms "argument" and "parameter" used when talking about
functions. In this example `param1` is a "parameter" because it is in the
function definition (`def functionName(param1, param2, ...):`).

In the above example of a function call, we call `value1` an "argument" to the
function. When the function is run, we say that "the parameter `param1` will
take the value `value1`". Functions may see complicated at first, but they will
make more sense when you begin to use them

#### Feeling familiar?

It turns out that functions are in fact not new, you've been using loads of
them! `print`, `len`, `raw_input`, `range`, and even `turtle.right` are all
functions! Functions are a really useful way of taking a chunk of code, giving
it a name, and making it reusable.

#### Uses of functions

Clearly functions are useful to prevent us writing the same code time and time
again. But, because functions have parameters, they enable something much more
powerful, the generalisation of code. Suppose we write the following:


    james = {'name': 'James', 'dob':1993 }
    sam = {'name': 'Sam', 'dob':1992 }
    print(james['name'] + ' - ' + str(james['dob']))
    print(sam['name'] + ' - ' + str(sam['dob']))


With a function, we can generalise this as follows:


    def printPerson(person):
        print(person['name'] + ' - ' + str(person['dob']))

    james = {'name': 'James', 'dob':1993 }
    sam = {'name': 'Sam', 'dob':1992 }
    printPerson(james)
    printPerson(sam)


Yes, in this example we did write more code, but now suppose we want to actually
print the date of birth first and then the name. We can simply change the code
in the printPerson function, and reap the rewards everywhere we use the
function. You'll see that we defined the function before we used it in the code.
Check what happens if you run the same example as above, but instead with the
function printPerson below the line `printPerson(sam)`. Hopefully you got an
error, because python hadn't yet seen the function definition for printPerson,
so it didn't know what to do when it got to the line `printPerson(sam)`. So make
sure you always define your functions before any code that calls the function.

Use the function below to complete the challenge:

    def max(x,y):
        if(x > y):
            return x;
        else:
            return y;

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Challenge</strong></div>
  <div class="panel-body">
   Can you create a function called max_list which takes in an list of ints as a parameter, and returns the largest int in the list.
   <br/>
   <strong>Hint</strong> use a for loop! You may need to look over materials in the previous lessons.
  </div>
</div>

#### Variables and their scope

Lastly, we need to talk about using and defining variables inside a function.
When we call a function, like `printPerson(james)`, then as we discussed, the
parameter `person` (which is a variable) gets assigned to the same value as the
argument `james`. Now this `person` variable is interesting, because it only
exists inside the function. So from outside the function, there is no way to
access the value `person`. This actually makes a lot of sense, because the
variable `person` only ever gets a value when the function is called. This
happens because of "scope". All variables have a scope, but it becomes
particularly noticeable in functions. It's best to see how this works by
examples:

    def printAndAddOne(number):
        print(number)
        return number + 1

    def main():
        x = 1
        printAndAddOne(x)
        x = printAndAddOne(x)
        print(x)

    # print(number)

    main()
    # print(x)

This example shows the important behaviour of scoped variables. What do you
think the output will be? Now run the code, and try uncommenting the lines
`#print(number)` and `#print(x)` to see what happens.

The `printAndAddOne`
function only accesses the variable number, and this is allowed, since number is
a paramter to the function. In some cases, functions can access variables that
are not one of their parameters, but this is strongly discouranged as it can
lead to confusion.

Lets go through this example line by line as python would.
When python runs this code, it firstly sees a function defition for
`printAndAddOne`. It remembers that its seen the function, and then moves on to
below the function. Now it sees a function definition for `main`, and again
moves on. Then python sees the function call `main()` so it jumps to the
function `main` and starts executing the code inside the function. Firstly it
assigns the value `1` to `x`, but because python is in a new scope (indicated by
the fact we are in a new function), it notes that when it leaves this scope, it
will forget everything about this assignment. Then it moves forwards to the next
line, and sees a function call `printAndAddOne(x)` so python remebers the
current line (for later), and jumps to the function `printAndAddOne`, assigning
`number` the value of `x` (which is `1`). Next it prints the current value of
`number` (which is `1`), and returns the value `number + 1`. Python notes that
its finished this function, so it jumps back to where it was before. It was
previously at the line `printAndAddOne(x)`, and python sees that it can discard
the returned value from the function, since we do not use it at this line. Now
it moves forwards another line, and again sees another function call of
`printAndAddOne`, so again that function is executed (exactly as before). This
time, because the line says `x = printAndAddOne(x)`, python assigns `x` the
returned value of the function. After executing the function, python will then
print the new value of `x`. Now, the line `#print(number)` is commented, so
python ignores that. The reason we cannot print the value `number`, is because
that variable is "forgotten" when python leaves the `printAndAddOne` funtion.
Similarly, when python leaves the `main` function, all new variable assignments
are forgotten about, which is why we cannot `print(x)` after we have left the
`main` function. So when python changes out of a functions scope, then any newly
introduced variables (in that function) are forgotten.

If that didn't make sense
then try reading it through a few times, and refer constantly to the code to see
how python is moving through the code, and what is happening to the variables at
each line. If it still doesn't make sense, then ask a helper to explain!

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
  Try creating some more functions and experiment with what variables you can, and cannot access when the code is inside and outside a function.
  </div>
</div>


## Let's Start Making a Game

From this point onwards we want you to experiment as much as possible! Make
the game your own, create your own world and allow the user to interact with it
exactly as you like!

We will be making suggestions and giving ideas for you to try and implement,
but we encourage you to think of completely unique ideas and use your knowledge
so far to try and do them.

Lets create your first text-based adventure game!

### What is a Text-Based Adventure Game?

Back in the days when people only had terminals (like what you type `python` in
to, to run your programs), games required a bit more imagination. They were
essentially an interactive story, in which the areas were described to you, and
you typed in instructions like `go N`, `pickup coins` or `describe` to interact
with the game and change the path of the story.

To solidify the concepts you've been learning in this course so far, we'll make
a small text-based adventure of our own. We'll walk you through creating some
bits, but towards the end, we'll just give you some suggestions and leave you to
it!

### Structuring the Game

#### Data Structures

It's important when writing a program, to design it first, and deciding upon
its structure is a key aspect of this. Firstly, let us think about the
information we'll need to store:

 * A map of locations
    - the location name
    - its description
    - its neighbours
 * Information about the player
    - their name
    - how much health they have
    - where they currently are

Dictionaries, which you have just learnt about, are perfect for both these
usecases. We will have a dictionary of `locations` that store the description
and neighbours for a location. We can access the location with its name as a
key. We will also keep a dictionary of the player's name, health and current
location, called `players`.

#### Control Flow

Another consideration is the control flow of the program. The basic setup will
be that we print the description of the current location, request an input from
the user, process the input as a command, update the player's location/health
etc and repeat until the player has died or decided to quit.

The "...and repeat" part should give us a clue as to what we'll be using. We'll
use `while` loop, like so:

    while player['health'] > 0:
        describe_location()
        get_input()
        process_input()

we'll replace the body of the loop with something more concrete a bit later on,
but for now these placeholders will do.

#### User Input

Something that isn't necessarily a concern for every program but is for this one
is how we are going to deal with user input. For simplicity's sake, we'll split
a valid user input in to two bits: the command, and some arguments, e.g.:

 * `describe` will print the description for the current location again.
 * `quit` will exit the game.
 * `go N`, `go E`, `go S` and `go W` will move the player in the appropriate
      compass direction.

So `describe` and `quit` are just commands with no argument, and `go` is a
command that takes a single argument, which is the direction to go in.

When we add further commands later, we will follow this same pattern, so we can
avoid code repetition, and use the same code to process every user input.

### A Starting Point

Bearing the above section in mind, here is a template to start your game
with. There are some blank sections that need filling in, and some
explanations of what should go there below it.

    # Functions

    def quit():
        "Goodbye. Thanks for playing!"
        exit()

    # Initialisation

    # Our Map of Locations
    locations = {
         'Large Gate': {
            'description': "An ominous gate stands before you.",
            'neighbours': {}
        }
    }

    # Player Information
    player = {
        'name': '',
        'health': 100,
        'location': BLANK_1
    }

    print "My Amazing Text Adventure"
    print "========================="
    print ""

    # Get the player's name
    BLANK_2

    # Main Loop
    while player['health'] > 0:
        input = raw_input("What do you do? ")
        command = BLANK_3

        if command[0] == 'quit':
            quit()
        else
            print "I don't know how to do that."

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      Replace <code>BLANK_1</code>, <code>BLANK_2</code> and
      <code>BLANK_3</code> according to the hints below.
    </p>
    <p>
      <strong>Hint 1</strong> we want the player to start by the <code>'Large
      Gate'</code>, so the player information held in the <code>player</code>
      variable should reflect that to begin with.
    </p>
    <p>
      <strong>Hint 2</strong> currently the player name is empty. Add some
      code at <code>BLANK_2</code> to ask the player for their name, and store
      it under the <code>'name'</code> key of the <code>player</code>
      dictionary.
    </p>
    <p>
      <strong>Hint 3</strong> this one is a bit more difficult. We want to
      split the <code>input</code> string across every space character, so
      that the first item in the resulting list is the action, and the rest of
      the list consists of the arguments for the action (should there be any).
      <br/>
      The function you want for this task is called
      <code>str.split(...)</code>, and it is defined for any string
      <code>str</code>. But we have left out the specific details of the
      function (like what the arguments are and what they do), so you have to
      look at the documentation to find out yourself. The documentation can be
      found
      <a href='http://docs.python.org/2/library/stdtypes.html#str.split'>
          here
      </a>.
    </p>
    <p>
      In future, when you are unsure about whether a particular function
      exists or how to use it, try having a look at this documentation to
      figure it out. Learning to use documentation whilst programming is an
      invaluable skill that comes with practise.
    </p>
  </div>
</div>

**Note:** our command system is currently case sensitive, which means that, for
example, the game will only quit if we ask it to `'quit'` as opposed to `'Quit'`
or `'qUiT'`. This is something to bear in mind and possibly improve upon in the
future (Maybe we shouldn't have case sensitive commands, and if we don't want
them, how do we go about accepting all possible combinations of case in a neat
way?).

### Improving your Game

Your game is up and running now, but not really playable. You can't really do
anything other than quit, so we should change that by adding some nice features.

#### The `describe` command

Currently you're playing blind. The game doesn't tell you where you are, or what
it looks like, so we should change that. Before we ask the player what they want
to do, we should tell the player where they are and describe their current
location to them. Additionally, if they forget while they're playing, they
should be able to ask the game to `describe` their current location.

Firstly, we will add a function, under the `# Functions` comment:

    def describe(loc_name, locs):
        location = locs[loc_name]
        BLANK_1

and then we will change the body of our main loop like so:

    while player['health'] > 0:
        describe(BLANK_2, locations)
        input = raw_input("What do you do? ")
        command = ...

        if command[0] == 'quit':
            quit()
        elif command[0] == 'describe':
            continue
        else:
            print "I don't know how to do that."

**Note:** the `continue` keyword is used to skip ahead to the next iteration of
the loop. We use this rather than the `describe` function we are defining
because we describe the location at the beginning of each loop anyway (so
calling `describe` inside the `if` statement would result in it being printed
twice in succession, try it for yourself to verify).

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      Replace <code>BLANK_1</code> and <code>BLANK_2</code> to make your game
      print a description of the player's current environment.
    </p>
    <p>
      <strong>Hint 1</strong> the <code>describe</code> function should print
      out the name of the location (<code>loc_name</code>) as well as the
      description (found in the <code>location</code> dictionary).
    </p>
    <p>
      <strong>Hint 2</strong> we should describe the player's current location
      which should be in the player's dictionary under the
      <code>'location'</code> key (So this is what we should pass to the
      <code>describe</code> function).
    </p>
  </div>
</div>

#### The `help` command

Now we can see where we're going! But players don't know what they can do, so
let us tell them with a `help` command. Whenever they type `help` into the game
we will print a list of commands they can use.

Once again, we add a function under the `# Functions` heading:

    def help():
        command_descriptions = {
            "help": "Show this help page.",
            "quit": "Quit the game.",
            "describe": "Describe the current location.",
            "go": "Walk either N, S, E or W, e.g. 'go N'"
        }
        BLANK_1

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      Add a condition to the <code>if</code> statement in the main loop, similar
      to the one's for the <code>'quit'</code> and <code>'describe'</code>
      commands, to check whether the user asked for <code>'help'</code>, and
      fill its body with the appropriate function call.
    </p>
    <p>
      <strong>Hint 1</strong> The body to the <code>help()</code> function is,
      for the most part, complete. Simply loop through the
      <code>command_descriptions</code> dictionary and print each command name
      along with its description.
    </p>
  </div>
</div>

#### The `go` command

You may have noticed we were a bit pre-emptive when we defined the `help`
command: We told people there is a `go` command, but we haven't provided one
yet. Not to worry, we'll get started on it straight away, seeing as it's rather
essential for a text-based adventure.

##### Building our Map

Firstly, we need to add some locations to our adventure. Currently we have only
one, so there isn't much motivation to define a movement command, so let's add
a location call `'Town'`, and have it be north of the `'Large Gate'`.

To do this we must update the `'Large Gate'`'s `'neighbours'` dictionary as
follows:

    'neighbours': {
        'N': 'Town'
    }

And we should also add an entry into the `locations` dictionary for the `'Town'`
location:

    'Town': {
        'description':"A bustling town centre with a wooded area to the west."
        'neighbours': {
            'S':'Large Gate'
        }
    }

You'll notice that I also added the `'Large Gate'` as the southern neighbour of
`'Town'`. This makes sense in a normal world, but this is your adventure game,
so don't feel as though physics should restrain you. If on the other hand you do
want behaviour like that of the normal world, you will have to remember to add
these complementary neighbours.

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    Add some of your own locations and link them up as neighbours. To start you
    off, the description for <code>'Town'</code> hints at a wooded area to the
    west.
  </div>
</div>

**Note:** Like our commands, location names are also case sensitive, meaning
`'Town'` is a different location from `'town'`. This may not be a good idea,
but luckily only we the programmer have to deal with it, so just remember to
take care with capitalisation when writing out what is neighbouring what.

##### `move()`

Now we have places to go to, we can define our move function, like so:

    def move(player, locs, cmd):
        if len(cmd) < 2:
            print "You need to specify a direction to go in: N, E, S or W."
            print "E.g. 'go N'"
            return

        dir = cmd[1]
        neighbours = locs[player['location']][BLANK_1]

        if BLANK_2:
            player['location'] = neighbours[dir]
        else:
            print "There's no route in the direction: " + dir + "!"

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      <strong>Hint 1</strong> Which key for a given location, produces its
      dictionary of neighbours?
    </p>
    <p>
      <strong>Hint 2</strong> Before we set the player's new location, we must
      check whether there is actually a route in that direction, by checking
      whether the provided direction (<code>dir</code>) is a key in the
      <code>neighbours</code> dictionary.
    </p>
    <p>
      After completing the <code>move</code> function, we must connect it up to
      the <code>if</code> statement in our main loop. As with the previous
      commands, this is achieved by adding a condition to the if statement
      (this time for the <code>'go'</code> command) and then making the
      appropriate function call. In this case, the three parameters to
      <code>move</code> are the <code>player</code> dictonary, the
      <code>locations</code> dictionary, and finally <code>command</code>
      which holds the entire command as a list of words.
    </p>
    <p>
      Try your game out and see how the move command works, to make sure you
      can get to every you expected to.
    </p>
  </div>
</div>

### Tasks

Here are a selection of features you can try and add to your game. You don't
have to follow this list exactly, and are ancouraged to use your imagination!

#### Bonus: Improving `describe`

It would be nice if we could tell which was the name of the location and
which was the description if we could underline the name in some way.

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      Print a line of <code>=</code> signs as long as the name, underneath
      the name of the location in the <code>describe()</code> function.
    </p>
    <p>
      <strong>Hint</strong> <code>str * n</code> is the string <code>str</code>
      concatenated with itself <code>n</code> times.
    </p>
  </div>
</div>

It might also be useful to know the names of the neighbours of the current
location, when describing them.

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      Augment the <code>describe()</code> function to also print the neighbours
      for the location in question, along with their directions.
    </p>
  </div>
</div>

#### Adding objects at locations

We might want to add objects to different locations that the player will be
able to interact with. For example, coins, or a chest, or a sword (if the theme
for your game is fantasy).

To do this, we suggest implementing to new dictionaries:

* `objects` which contains information about every single object inside the
  game, regardless of where it is found.
* `object_locations` which is a dictionary, with locations as the key, and the
  value should be a `list` of objects from the objects variable.

E.G:

    objects = {
      "Chest": {...},
      "Sword": {...}
    }

    object_locations = {
      "Town": ["Chest", "Sword"]
    }

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      Create the <code>objects</code> variable. We want the values of
      everything in this dictionary to also be a dict. What should the keys of
      <strong>these</strong> dictionaries be? I.E: What information do we want
      to store about object, maybe a description of it? And whether a user will
      be able to pick it up?
    </p>
  </div>
</div>

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      Create the <code>object_locations</code> variable, and add some objects
      to some locations.
    </p>
  </div>
</div>

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task - Looking Around</strong></div>
  <div class="panel-body">
    <p>
      Create a new <code>look</code> command for the user, which will display
      information about the neighbors of your current location, and any objects
      currently in your location.
    </p>
  </div>
</div>

#### Interacting with objects

We want the user to be able to pick up and drop objects, create a new list in
the `player` dict that will store a list of all of the objects the player is
currently holding, and fill it with any objects you want the user to start
with. Call this list `"inventory"`.

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task</strong></div>
  <div class="panel-body">
    <p>
      Create the <code>"inventory"</code> list in the <code>player</code> dict.
    </p>
  </div>
</div>

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task - Inspecting the Inventory</strong></div>
  <div class="panel-body">
    <p>
      Create a new command, <code>inventory</code>, which will allow the user
      to list the objects which they have stored in their inventory.
    </p>
  </div>
</div>

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task - Picking up Objects</strong></div>
  <div class="panel-body">
    <p>
      A user may want to pick up objects at a location and put them into their
      inventory. Implement a <code>pickup</code> command that will allow a user
      to pick up an object <strong>only from the current location</strong>. We
      want a way for the user to specify which object they want to pick up, the
      way you do this is up to you.
    </p>
    <p>
      <strong>Hint:</strong> you will want to remove the object from the
      <code>object_locations</code> variable, and add it to the
      <code>player["inventory"]</code> list.
    </p>
  </div>
</div>

<div class="panel panel-primary">
  <div class="panel-heading"><strong>Task - Dropping Objects</strong></div>
  <div class="panel-body">
    <p>
      Implement a <code>drop</code> command that does the opposite of the
      <code>pickup</code> command.
    </p>
  </div>
</div>



