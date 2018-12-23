# CubedAI
PyOpengl based Rubik cube game and its AI

## Installation procedure

## Running the code

## Cube visualization
The rubik's cube is visualized in a `pygame` window using `OpenGl`. The cube is represented using faces, surfaces and points.
**Face**: The cube has 6 faces, namely up, down, front, back, right and left
**Surfaces**: The cube has stickers consisting of points. Each face looks as follows  (in terms of points):
```
30--31 32--33 34--35
|   |  |   |  |   |
24--25 26--27 28--29
18--19 20--21 22--23
|   |  |   |  |   |
12--13 14--15 16--17
6---7  8---9  10--11
|   |  |   |  |   |
0---1  2---3  4---5
```
The surfaces on each of the faces are as follows:****
```
6  7  8
3  4  5
0  1  2
```
- The lateral surfaces are represented as given in **** assuming the when you see the lateral surface head on from outside the cube, the Up side is at the top of the cube and the Down side is at the bottom of the cube
- The Up and Down surfaces of the cube are represented as given in **** assuming when you see the Up surface head on from outside the cube, the Back side of the cube is at the top and the Front side is at the bottom of the cube. When you see Down surface head on from outside the cube, you should see the Front surface at the top of the cube and Back surface at the bottom of the cube.

Here are the examples of first 1, first 2 and first 5 surfaces of each face:


## Moving the cube
The class `rubiks_cube` provides you with methods of the format `move_XI` and `move_X`. Here X is the initial letter of the surface and is to be used as `rb.move_UI`, `rb.move_B`, `rb.move_FI`. `I` means "inverted". For more information on the notation end of things, kindly refer to [Ruwik Notation](https://ruwix.com/the-rubiks-cube/notation/).

## Cube configuration


## Solving algorithm
Solving algorithm rests in `src/solver.py` and the rubik's class rests in `src/rubiks_cube.py`. 