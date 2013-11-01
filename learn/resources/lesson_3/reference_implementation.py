"""
A full implementation of a game for the Coding Lesson:
http://ox.compsoc.net/learn/resources/lesson_3/

This program does not take advantage of a lot of python language features, as
it only uses techniques that have been taught thus far. In addition, standard
coding practices have been dropped in favour of making understandable code for
people who have been following our course from the start, up until this point.

"""


print "The CompSoc Ultimate Adventure Game"
print "(a text-based adventure)"
print ""


############################
# Game Data (Doesn't Change)

locations = {
    "The Town Square": {
        "description": ("The centre of your home town, there is a fountain in "
                        "the middle and you're surrounded by trees!"),
        "neighbors": {
            "S": "The Town South Gate",
            "N": "The Town Hall Entrance"
        }
    },
    "The Town South Gate": {
        "description": "Few venture beyond this point",
        "neighbors": {
            "N": "The Town Square"
        }
    },
    "The Town Hall Entrance": {
        "description": "I wander what's inside!",
        "neighbors": {
            "S": "The Town Square",
            "N": "The Town Hall"
        }
    },
    "The Town Hall": {
        "description": "Nothing interesting going on in here...",
        "neighbors": {
            "S": "The Town Hall Entrance",
        }
    }
}


# A dict we use to get from a direction command to a string direction
compas = {
    'N': 'North',
    'E': 'East',
    'S': 'South',
    'W': 'West'
}


##########################
# Game State (Does Change)

player = {
    "location": "The Town Square"
}

##################
# In-Game Commands

def cmd_help():
    command_descriptions = {
        "help": "Show this help Page",
        "quit": "Quit the game",
        "go": "Walk either N, E, S or W, e.g: 'go N'",
        "describe": "Descript the current location"
    }

    print "Available Commands:"
    for command in sorted(command_descriptions):
        print "  " + command.ljust(10) + " - " + command_descriptions[command]


def cmd_quit():
    print "Goodbye. Thanks for playing!"
    exit()


def cmd_describe():
    desc = locations[player["location"]]['description']
    print "Location: " + player["location"] + " - " + desc


def cmd_go(cmd):
    """
    cmd is a list of each of the bits of the command that the user typed in,
    E.G: ['go'] or ['go', 'N']

    """

    # Check that the user typed in a direction to go in
    if len(cmd) < 2:
        print "You need to specify a direction to go in, either N, E, S or W."
        print "E.G: 'go N'"
        return

    direction = cmd[1]

    # Check that the direction is either N, E, S or W
    if direction not in {'N', 'E', 'S', 'W'}:
        print "I don't know how to go '" + direction + "'"

    # The dictionary of neighbors for our current location
    neighbors = locations[player["location"]]['neighbors']

    # Check if we can actually go in the direction specified
    if direction not in neighbors:
        # ... We can't
        print "You can't go " + compas[direction] + " from here!"
    else:
        # We can go in the direction given! Lets do that
        player["location"] = neighbors[direction]
        cmd_describe()


############
# Start Game

print "Type 'help' for a list of commands"
cmd_describe()


###########
# Main Loop

while True:

    try:
        command = raw_input("> ")
    except (KeyboardInterrupt, EOFError):
        print "quit";
        cmd_quit();

    if command == '':
        print "You didn't type a command, type 'help' for a list of commands"
    else:
        cmd = command.split(' ')

        if cmd[0] == 'help':
            cmd_help()
        elif cmd[0] == 'quit':
            cmd_quit()
        elif cmd[0] == 'go':
            cmd_go(cmd)
        elif cmd[0] == 'describe':
            cmd_describe()
        else:
            print "Unknown Command: '" + cmd[0] + "'"
            cmd_help()
