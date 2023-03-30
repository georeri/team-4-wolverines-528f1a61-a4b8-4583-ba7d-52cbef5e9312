*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***      StartingX   StartingY   StartingMoveCount   Direction   EndingX EndingY EndingMoveCount
Move N to position      0           0           1                   NORTH       0       1       2
Move S to position      9           9           5                   SOUTH       9       8       6
Move E to position      0           0           9                   EAST        1       0       10
Move W to position      9           9           22                  WEST        8       9       23
Move N to boundary      9           9           83                  NORTH       9       9       84
Move S to boundary      0           0           101                 SOUTH       0       0       102
Move E to boundary      9           9           1001                EAST        9       9       1002
Move W to boundary      0           0           10001               WEST        0       0       10002



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
