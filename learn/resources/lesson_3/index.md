[meta title="Lesson 3: A Text-Based Adventure Game" /]

[embed page="/learn/resources/highlight.js/embed" /]

## The Goal of This Lesson

In this lesson, we will be taking a little bit of a different approach. We will
be working towards the goal of creating a text based adventure game. There will
be less guidance, so that you can try and use the skills that you have learned
in the lessions so far.

We will give you tasks to complete, and tips, and helpers will be available to
answe any questions during the lesson.

## Before we Start

There are a couple more interesting things that we would like to teach you
before getting started...

### Introducing the `dict` type

#### Some examples using `dict`

### Intruducing Functions

#### How are they useful

#### Function Arguments

#### Talk about how they've been using them the whole time, and give examples

#### Functions have their own variables

(talk about function scope)

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

#### `describe`

Currently you're playing blind. The game doesn't tell you where you are, or what
it looks like, so we should change that. Before we ask the player what they want
to do, we should tell the player where they are and describe their current
location to them. Additionally, if they forget while they're playing, they
should be able to ask the game to `describe` their current location.

Firstly, we will add a function, under the `# Functions` comment:

    describe(loc_name, locs):
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

#### `help`

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

#### `go`

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
      print a line of <code>=</code> signs as long as the name, underneath
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

e.g:

* Chests

#### Interacting with objects

#### Adding Monsters into the mix



