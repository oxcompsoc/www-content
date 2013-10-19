[meta title="Lesson 0: Setting Up" /]

This page details what needs to be done before being able to get started with
the programming.

Throughout the course, we'll be using a text editor called
[Sublime Text](http://www.sublimetext.com/). We will show you how to use this
on the **lab computers**, and how to set it up on your laptops.

## How We'll Be Starting The Course

Initially, you will be using the computers available in the lab, so that you
can get stuck straight in. No setup or anything is required on these computers,
you can just follow the instructor / the online resources and be on your way.

<div class="panel panel-danger">
  <div class="panel-heading"><strong>Warning</strong></div>
  <div class="panel-body">
  Your data on these <strong>lab computers</strong> will be
  <strong>deleted</strong>, you will be logged in on a temporary account.
  <br /><br />
  If you would like to save your progress before the end of the session, make
  sure you copy the files to a usb stick, or email them to yourself or
  something. A helper will be able to hwlp you do this if you get stuck.
  </div>
</div>

After you have had some exposure to python and start to feel comfortable, we
will go through setting up your python development environment on your own
personal laptop, so that you will not need to use the **lab computers** to do
programming, (you could even do it outside of the course if you like).

## Setting Up your Python Development Environment on your Laptop

Firstly, download and install [Sublime Text](http://www.sublimetext.com/2) (You
can use a different plaintext editor if you already have a favourite).

From here-on-out the instructions very depending on your operating system...

### Mac OS X

Mac actually comes with python pre-installed, and a decent Terminal App.

To find your Terminal App, open your `Applications` folder, go to `Utilities`,
and then open `Terminal`. You should put this in your dock because we will be
using it a lot.

#### Test Python Works...

With your terminal open, type `python` and hit enter. If you get a python
prompt that looks a little bit like this:

    Python 2.7.5 (default, Sep  6 2013, 09:55:21)
    [GCC 4.8.1 20130725 (prerelease)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Then it works, press `Ctrl + D` to close python, and then again to close the
terminal.

### Windows

Windows is one of the few platforms that does not come with Python pre-installed,
so you will need to acquire a copy. The Python installer for Windows is freely
available [at the official website]
(http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi). Download this and
follow the instructions and by the end, you'll have a working python installation.

#### Test Python Works

##### The Easy Way

Python for Windows comes with an inbuilt editor called IDLE (named for Eric
Idle of Monty Python fame, if you're curious), which you can access by
opening the Start menu and searching for "IDLE" - it should be located
in a folder called `Python 2.7`. You can use this tool to create Python
scripts with inbuilt code highlighting and quickly run them and see the
output, all from within the program. This is by far the easiest way to
do things if you're new to this.

However, if you want to play with terminals and other cool stuff like those
crazy people running Mac OSX or Linux, then you can do it...

##### The Hard Way

Open command prompt by `Windows + R`, and typing `cmd` into the box that
appears. Type `python` into the command prompt, and something like the
following should appear:

    Python 2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)] on win
    32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

If this appears, then you are ready to begin programming in Python! You can
execute a saved script with the command `python name_of_script.py` after you've
saved them in your text editor.

If, instead, you find yourself with a message something like the following:

    'python' is not recognized as an internal or external command,
    operable program or batch file.

something has gone wrong. If you're feeling brave, read on and fix it yourself,
but feel free to ask a helper if this happens.

If your computer can't find the program `python`, this is because it's not on
what's known as the system's "path" - essentially where it looks for programs
when you reference them by name with no full path to the file. On Windows Vista
and 7 (and possibly 8), open Start, start typing `environm` until the option
"Edit environment variables for your account" comes up. Select this, click the
entry `PATH` in the box that opens up, then click `Edit`. Go to the start of
this textbox and add `C:\Python27\;` - the location of your Python installation.
If you chose to put it somewhere else in the installation, change this
accordingly. **Make sure** that this entry and the rest of the textbox are
separated by that `;` because if not things can and likely will break. This is
**important**.

There are some benefits to doing it this way - if in due course you find
yourself needing to do some programming on a different operating system or
in a different language where graphical tools aren't available, you'll find
it much less of a shock to the system if you acclimatise yourself early.
Aside from this, there's little difference between the two methods except that
one is slightly easier and more centralised than the other.
