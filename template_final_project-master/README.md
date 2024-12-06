
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Maze Run
## CS110 B1 Final Project  Semester 1, 2024

## Team Members

Makenna and Allie

***

## Project Description

In the Maze Run, we will be moving a character through a vertical maze of randomly sized rectangles. The user needs to use the up/down and right keyboard arrows to get through the maze of rectangles. If the character touches one of the rectangles the game will automatically end and display the end screen.
***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu
2. End game display when game is won
3. Moveable character (with keyboard arrows)
4. Randomized barriers (rectangles)
5. End game display when game is lost

### Classes

- Button: Draws a rectangle with a parameter to write text inside 
-Cell: generates different sized rectangles to create different mazes 
- Character: creates a character (sprite object) that will move throughout the maze based on user actions through the keyboard arrows. Has functions to move based on the keys hit: up or down.
- Maze: creates a maze of random rectangles that the character will have to move through. Several rectangles will be present but different widths and heights will be sued each time.
- Setup: creates the initial screen with the directions printed 


## ATP

|Test Description 1:   

    Tests whether or not the sprite/character moves with  the use of the 3 cursor control keys.

Procedure:

    Press up key,  Expected Results: Character moves up
    Press down key,  Expected Results: Character moves down
    Press down right,  Expected Results: Character moves right

Test Description 2:   

    Checks that the begin and start screen button works.

Procedure:

    Click the begin button, Expected: The maze screen appears and the maze begins.

Test Description 3: 

    test that the when the game is replayed, the rectangles are drawn at different height

Procedure:

    Click the begin button 3 times, play the game and compare the rectangle mazes Expected Results: mazes will not be identical

Test Desription 4:

    test end box that appears when you win 

Procedure:

    Move arrow until it hits rectangle, Expected: text that "you won" appears

Test Description 5:

    test end box that appears when you loose 

Procedure:

    Move arrow until it hits rectangle, Expected: text that "you lost" appears

