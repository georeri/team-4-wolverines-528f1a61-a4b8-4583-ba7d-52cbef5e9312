*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***      StartingX   StartingY   Direction   EndingX EndingY
Move N to position      0           0           NORTH       0       1
Move S to position      9           9           SOUTH       9       8
Move E to position      0           0           EAST        1       0
Move W to position      9           9           WEST        8       9
Move N to boundary      9           9           NORTH       9       9
Move S to boundary      0           0           SOUTH       0       0
Move E to boundary      9           9           EAST        9       9
Move W to boundary      0           0           WEST        0       0



*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
