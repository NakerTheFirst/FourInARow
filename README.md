# FourInARow
Python, OOP-based Four In A Row game implementation. The goal is to place 4 same colour orbs which line up horizontally, vertically or diagonally. The game modes featured are player vs player and player vs AI. User can play in 2 interface modes: GUI and console interface.

<br>
<p align="center"><img width="640" src="https://github.com/NakerTheFirst/FourInARow/blob/main/interface.png" alt="Image of an interface of a four in a row game"></p>
<p align="center">Game's Graphical User Interface</p>

## Structure
The programme consists of 8 classes: Engine, Board, UI, ConsoleInterface, GUI, Player, HumanPlayer and AIPlayer. The UI is an abstract base class, which serves as a template for the GUI and ConsoleInterface classes which inherit from it, and use polymorphism to implement their own versions of its methods. The same pattern occurs in Player, HumanPlayer and AIPlayer classes, which are contained in the Board class. The Board handles all the necessary game logic, while the Engine class boots all the components and serves as a driver of ConsoleInterface and GUI. The Engine class contains objects of the Board, ConsoleInterface and GUI classes, and has 2 methods for selecting the interface type, and running the game.

## Class diagram
![Image of a class diagram of a four in a row game](https://github.com/NakerTheFirst/FourInARow/blob/main/class_diagram.png)
