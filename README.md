# Snake - CS50x Final Project 2026

Snake is a reproduction of the original Classic Snake from 1998. The Games Architecture is split up in main, main\_gamestate, main\_menu and main\_game.

### Main

Main handles the creation of the most basic components. In Order: 

I use pygame-ce to create this game, so to start pygame needs to be initialized, then I set up the screen that will be the place where everything is rendered onto. Other important classes are clock and highscore, as they handle time-management and saving scores. These 3 will be made available to the following gamemodes, by saving their references into the information monopole main\_gamestate. The two gamemodes are created main\_menu and main\_game and added to main\_gamestate as well. The actual gameloop starts in the MainMenu and continues until neither gamemode is running. Once both game modes are inactive, the game is over and all pygame modules need to be uninitialized.

### Main Game State

This class contains all information important to other classes. As already said, it contains the screen, clock, highscore and gamemodes. Instead of accessing references to the class and then their functions, main\_gamestate contains helper functions.

### Main Menu

The Main Menu is split up into 3 Buttons. The Buttons are created in a helper class for ease of implementation. Start Game, Highscore and Quit. Start Game switches the GameMode to main\_game. Highscores opens up a submenu that contains a table - created with a helper class as well - that contains the scores from previous game overs. Quit is just like it says the way to close the application through menus and not just through pressing the X in the right upper corner.

### Main Game

The main\_game contains classes field, snake and game. I made the decision to put everything tightly associated with the game in the same file. 



Class Field can be seen as a 2D Array with the sole purpose to update the field variables and keep them up-to-date at all times. It contains the position of the snake and fruit at the current time, a whitelist with free spaces and a blacklist with blocked spaces by the snake, the fruit is treated as a special case to make sure access to its position is as fast as possible. Of course it also contains the spawn and draw functions for the fruit.



Class Snake has a reference to the field in order to make the field the sole class responsible for positions. A Snake has a body, direction, score and tempo. Score is a bit redundant because length of the body would also work, but an extra variable makes access easier to understand. The Snake also starts its own process of moving and if moving over a fruit its growth.



Class Game is the actual implementation of the gamelogic, including pause menu and gameover menu. Both the pause and game over menu contain the buttons “back to main menu” as well as “quit” which do precisely as expected. During the Game the current Score will be rendered atop the playfield to show the current score to the player. Pause Menu stops the game from progressing and with the button continue or a press of P the game resumes. GameOver Menu instead of continue, has a restart button that restarts the game. The most important function is the gameloop that handles the events as well as manages the current stats and what to render where. A fast way to reset is pressing R and a fast way to lose and thus save the current game is pressing L. Other than those there is also WASD as Input to change the direction of the snake.



### Example First Playthrough

Start a Game with an IDE of your choice. Press Start Game, your Snake spawns at the edge and looks to that edge, which means you got unlucky and lost instantly but don’t worry your highscore of 0 was added to the list of highscores. Press Restart to try again. This time the snake with a single block spawns in the middle of the board and the fruit some place on the grid. After collecting some amount of fruits, you block yourself in with the snake body and after hitting itself, the game is over. This time you go back to the main menu in the game over screen. Press Highscore and there you can see your highscores of 0 at the bottom and your actual score after playing a bit. 



### Structure during Development

##### Preparations:

Step 1: Setup with Github for version-control, python Version 3.14.7, pip Version 26.3 and pygame-ce Version 2.5.8 in Pycharm.

Pycharms AI Features are deactivated. Only the autocomplete is on, to help with functions that are not yet fully understood. In retrospect this was a mistake, because the autocomplete mismatched many times and just typing the functions out was faster. I used ChatGPT to help me find the best versions to use with this Project and Setup Pycharm to not use anything that would collide with cs50x academic honesty guidelines.

Main Problem was: old pygame is deprecated because of open source problems, so that Team changed to pygame-ce for python versions newer than 3.13.



Step 2: Learn the documentation at https://www.pygame.org/docs/. I wrote a 9 Page Google doc that contains all the functions that

I could find that might be useful, when working and gave comments to their functionality for a faster lookup, than the original site.



Step 3: Watching Videos to get a feel for pygame and best practices because some of the Function do similar things or default to another.

Pygame in 18 min 		https://www.youtube.com/watch?v=blLLtdv4tvo

Pygame Full Course		https://www.youtube.com/watch?v=lJ4wobV3bZQ



Step 4: Analysis

Gameloop:

Process Input

Check State/ State Logic

Interpolate next State

Update State

Draw Screen



Implementation notes in Google Docs

Process Input notes in Google Docs

Collision notes in Google Docs

Movement notes in Google Docs

Draw screen notes in Google Docs



##### Implementation Process:

class button 			https://www.youtube.com/watch?v=jyrP0dDGqgY

class button allows to create multiple Buttons with just a Basic class

Problem: It makes the main function very cluttered to do everything in there and some functions that Buttons might do are not accessible from

the Buttons.

My Solution: Using my Knowledge from Unreal Engine I will create two classes GameMode and GameState.



class gamemode takes care of the logistics behind a stage in a game, every stage like MainMenu and Game get their own gamemode

class gamestate is the place to store the most important information, there is only one of them in the whole Project



Actual Game Implementation and Navigation:

class Main Menu contains all MainMenu Logic and Navigation between submenus

class Game contains logic for the Game and Navigation between submenus

class Snake dictates the score, tempo, body and direction

class Field contains redundant Information About Snakes Position and Fruits Position



Enum:

class MainMenu State

class Field State

class Direction

class Game State



class highscore https://www.geeksforgeeks.org/python/writing-csv-files-in-python/ and https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/

After achieving a satisfactory result I refactored most of the code to make it easier to read and manage, this refactoring also made the code more mine, especially because at the beginning some code snippets were more closely inspired by the videos and documentations.



### Overview of all the resources used:

ChatGPT for Setup of the new IDE and libraries

https://www.pygame.org/docs/ for General Knowledge

https://www.youtube.com/watch?v=blLLtdv4tvo for Understanding the Library

https://www.youtube.com/watch?v=lJ4wobV3bZQ for Understanding the Library

https://www.youtube.com/watch?v=jyrP0dDGqgY for Understand more Complex Structures Buttons

https://www.geeksforgeeks.org/python/writing-csv-files-in-python/ for writing into csv in Python

https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/ for reading from csv in Python



