# cs50xSnake

## Cs50x final project the world renown game Snake



### Preparations:

Step 1: Setup with Github for version-control, python Version 3.14.7, pip Version 26.3 and pygame-ce Version 2.5.8 in Pycharm.

Pycharms AI Features are deactivated. Only the autocomplete is on, to help with functions that are not yet fully understood.

I used ChatGPT to help me find the best versions to use with this Project and Setup Pycharm to not use anything that would collide

with cs50x academic honesty guidelines.

Main Problem was: old pygame is depricated because of open source problems, so that Team changed to pygame-ce for python versions newer than 3.13.



Step 2: Learn the documentation at https://www.pygame.org/docs/. I wrote a 9 Page Google doc that contains all the functions that

I could find that might be useful, when working and gave comments to their functionality for a faster lookup, than the original site.



Step 3: Watching Videos to get a feel for pygame and best practices because some of the Function do simular things or default to another.

Pygame in 18 min 		https://www.youtube.com/watch?v=blLLtdv4tvo

Pygame Full Course		https://www.youtube.com/watch?v=lJ4wobV3bZQ



Step 4: Analysis

Gameloop:

1. Process Input
2. Check State/ State Logic
3. Interpolate next State
4. Update State
5. Draw Screen



Implementation notes in Google Docs

Process Input notes in Google Docs

Collision notes in Google Docs

Movement notes in Google Docs

Draw screen notes in Google Docs



Implementation Process:

class button 			https://www.youtube.com/watch?v=jyrP0dDGqgY

class button allows to create multiple Buttons with just a Basic class

Problem: It makes the main function very cluttered to do everything in there and some functions that Buttons might do are not accessable from

the Buttons.

My Solution: Using my Knowledge from Unreal Engine I will create two classes GameMode and GameState.



class gamemode takes care of the logistics behind a stage in a game, every stage like MainMenu and Game get their own gamemode

class gamestate is the place to store the most important information, there is only one of them in the whole Project



Actual Game Implementation and Navigation:

class MainMenu contains all MainMenu Logic and Navigation between submenus

class Game contains logic for the Game and Navigation between submenus

class Snake dictates the score, tempo, body and direction

class Field contains redundant Information About Snakes Position and Fruits Position 



Enum:

class MainMenuState

class Field\_State

class Direction

class Game\_State


class highscore https://www.geeksforgeeks.org/python/writing-csv-files-in-python/ and https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/
&#x20;

