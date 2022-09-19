# Scripts Tutorial
Scripts are Python classes which can change behaviour of the game via Python code, in
most direct way.

**List of contents**
- [Creating new script](scripts_tutorial.md#creating-new-script)
- [Using events to run code](scripts_tutorial.md#using-events-to-run-code)
- [Arguments](scripts_tutorial.md#arguments)
- [Events](scripts_tutorial.md#events)

**Can be useful**  
- [Example script file](/scripts/example_script.py)  
- [PyGame events documentation](https://www.pygame.org/docs/ref/event.html)

---
### Creating new script
To create new script, you simply need to create new Python file in `/scripts/` folder.  
You can put it inside folders there if you want to organise it better, IoA will read
any nested directory system.

After creating new file, you will need to implement few elements required for the file
to be recognised as a script.  
First of all, let's import `ioaScript` class and create your scripts' class:
```python
from core.scripts import ioaScript

class NameOfYourScript(ioaScript):
```
**NameOfYourScript** is crucial, since it needs to be unique across all the scripts.  
Make it as specific as you like.

After that, create **init** function:
```python
    def __init__(self):
        super().__init__()
```
Creating those is necessary for your script to exist. In short, they just tell the game
that the script is officially connected to the game itself.

But, creating script file makes no sense if you cannot use it for anything. For that, you
will need...

### Using events to run code
To use your script within events, you will need to create variable called "event".  
It will look like that:
```python
event = "NAME_OF_THE_EVENT"
```
Variable needs to be *String* type of data and refer to any existing Forged Event 
[which you can see here](scripts_tutorial.md#events). You cannot create script for
several events at once - for that purpose, just create new script for each event.  
Once you decide on event you want to use, you will need to create running function:
```python
def run(self, *args, **kwargs):
    #write your code here
```
What is important, is use of `*args` and `**kwargs` elements. No matter how many 
[pre-given arguments](scripts_tutorial.md#arguments) you use, adding it at the end is 
crucial, as it will maintain all other unused arguments.  
For example, here we use `pg_events` argument, but not `screen` one:

```python
# imported logging
import logging


def run(self, pg_events, *args, **kwargs):
    for event in pg_events:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            logging.debug("Player clicked left mouse button!")
```
Even if you used all currently implemented arguments, it's safer to put it at the end,
because it will make your script future-proof.

### Arguments
Arguments are additional data given by game to you, so you can use it to control your
code. Depending on argument type, it can either condition some actions, or allow you
to create those actions.

Here is list of arguments for **run()** function. Please remember about using `*args`
and `*kwargs` as last arguments!  

``fg_events`` - used to access Forged events (internal IoA event system)  
``pg_events`` - used to access PyGame events  
``screen``- used to interfere with currently used screen (variable in itself is read-only) 

### Events
Here is list of Forged Events currently used in vanilla. If you are confused about
terminology, please refer to [glossary](/docs/glossary.md#events).  

``MENU`` - used to indicate entering main menu  
``SNDV_CHG`` - indicate change of sound volume