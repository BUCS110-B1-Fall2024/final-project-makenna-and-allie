
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Maze Run
## CS110 B1 Final Project  Semester 1, 2024

## Team Members

Makenna and Allie

***

## Project Description

In the Maze Run, we will be moving a character through a vertical maze of randomly sized rectangles. The user needs to use the up/down keyboard arrows to get through the maze of rectangles. The maze will take away the 'lives' of the character if the character touches one of the rectangles. Once 2 'lives' are lost, the game will automatically end through the quit program.

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
4. Randomized barriers (rectangles)
5. life system (with quit feature)

### Classes

- Character: creates a character (turtle object) that will move throughout the maze based on user actions through the keyboard arrows. Has functions to move based on the keys hit: up or down.
- Maze: creates a maze of random rectangles that the character will have to move through. Several rectangles will be present but different widths and heights will be sued each time.
- Life: determines how many 'lives' the charcter has left, based on if the character has touched any of the rectangles. The character will have 2 lives, if a rectangle is touched twice in one round, the character automatically 'dies'. 

## ATP

|Test Description 1:   

    Tests whether or not the sprite/character moves with  the use of the 2 cursor control keys.

Procedure:

    Press up key,  Expected Results: Character moves up
    Press down key,  Expected Results: Character moves down

Test Description 2:   

    Checks that the begin and start screen button works.

Procedure:

    Click the begin button, Expected: The maze screen appears and the maze begins.

Test Description 3: 

    Tests that the music plays at the right times.

Procedure:

    Click the begin button, Expected Results: Music begins when the screen changes.
    Screen changes from maze to the tend screen, Expected Results: The music stops when the game ends.

Test Desription 4:

    Make sure the sprite/character loses a live when it runs into the maze's rectangle.

Procedure:

    Move the arrows until the charcter runs into the border, Expected Results: A live is lost. 

Test Description 5:

    Make sure that the game over screen displays the right screen when you lose and when you win. 

Procedure:

    1. Lose the game, Expected Results: Game over screen shows up with a try again button and the end score.
    2. Win the game, Expected Results: Game over screen shows up with a play again button and the end score.

