# Random Walk

A Python-based Random Walk visualization using the turtle graphics library. This project creates an artistic representation of a random walk, drawing colorful paths on a black background.

## Creator

HS160

## Features

- Generates a random walk pattern
- Uses a variety of colors for the path
- Creates a visually appealing design on a black background
- Customizable number of steps, step size, and line thickness

## Requirements

- Python 3.x
- turtle module (typically comes pre-installed with Python)

## How to Run

1. Save the code in a file named `random_walk.py`
2. Open a terminal or command prompt
3. Navigate to the directory containing the file
4. Run the command: `python random_walk.py`

## Customization

You can easily customize the Random Walk by modifying the following parameters in the code:

- `color_list`: Add or remove colors to change the palette
- `t.pensize(15)`: Adjust the number to change the line thickness
- `t.speed('fastest')`: Change the drawing speed (e.g., 'slow', 'normal', 'fast')
- `range(1,510)`: Modify the range to increase or decrease the number of steps
- `t.forward(50)`: Change the number to adjust the step size

## How It Works

1. The program creates a turtle object and sets up the screen with a black background.
2. It defines a list of colors and possible movement directions (0, 90, 180, 270 degrees).
3. The turtle then takes 509 steps, each time:
   - Choosing a random color from the color list
   - Moving forward by 50 units
   - Changing direction to a random angle from the moves list
4. After completing the walk, the turtle returns to its starting position.
5. The program waits for a click on the screen to exit.

## Extending the Project

Here are some ideas to extend the functionality of your Random Walk project:

1. Add user input for the number of steps or step size
2. Implement different patterns of movement (e.g., diagonal moves)
3. Create multiple turtles for simultaneous random walks
4. Add a feature to save the generated artwork as an image file

Feel free to experiment and make the project your own!

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
