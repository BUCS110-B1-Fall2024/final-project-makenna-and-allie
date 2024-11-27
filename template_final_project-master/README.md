
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Maze Run
## CS110 B1 Final Project  Semester 1, 2024

## Team Members

Makenna and Allie

***

## Project Description

In the Maze Run, we will be moving a character through a complex maze. The maze will have hidden features that take away the 'lives' of the character, including when the character goes down dead ends and spontaneous rocks/items in the way of the character. Along with looking out for these dangers, the user will need to answer random trivia questions displayed on the screen every 30 seconds and if they get it wrong they lose a 'life'. Once 3 'lives' are lost, the game will automatically end through the quit program. The character will be controlled by the user through the keyboard, the arrows will be used to move the character through the maze and the letters/numbers will be used to answer the trivia questions.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu
2. End game display
3. Moveable character (with keyboard arrows)
4. Trivia display
5. life system (with quit feature)

### Classes

- Character: creates a character (turtle object) that will move throughout the maze based on user input. Has functions to move
forward, backward, right and left.
- Trivia: Creates a trivia object, that will be displayed throughout certain checkpoints in the maze, uses user input and contains a function that checks if the input is correct. 

## ATP


|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
|Test Description 1:   

    Tests whether or not the sprite/character moves with  the use of all 4 cursor control key.

Procedure:

    Press up key,  Expected Results: Character moves up
    Press down key,  Expected Results: Character moves down
    Press right key,  Expected Results: Character moves right
    Press left key,  Expected Results: Character moves left

Test Description 2:   

    Checks that the begin and start screen button works.

Procedure:

    Click the begin button, Expected: The maze screen appears and the maze begins.
    Click the level button, Expected: Level adusjts from easy to hard. 
    Click the theme buttons, Expected: Background image of the maze changes.

Test Description 3: 

    Tests that the music plays at the right times.

Procedure:

    Click the begin button, Expected Results: Music begins when the screen changes.
    Screen changes from maze to the tend screen, Expected Results: The music stops when the game ends.

Test Desription 4:

    Make sure the sprite/character loses a live when it runs into the maze border.

Procedure:

    Move the arrows until the charcter runs into the border, Expected Results: A live is lost. 

Test Description 5:

    Make sure that the game over screen displays the right screen when you lose and when you win. 

Procedure:

    

