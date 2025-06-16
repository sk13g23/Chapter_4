"""Short Summary.

Defines all the methods needed to setup the game of life
"""
import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

blinker = np.array([
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]]
)

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    """Defines all the methods needed to setup the game of life."""

    def __init__(self, size):
        """Initialize the game."""
        self.board = np.zeros((size, size))

    def play(self):
        """Set up the game."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Define the movement of the cells."""
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbourcount = convolve2d(self.board, stencil, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 if (
                            neighbourcount[i, j] == 3
                            or (neighbourcount[i, j] == 2
                                and self.board[i, j])
                                        ) else 0

    def __setitem__(self, key, value):
        """Define fetching elements through square brackets."""
        self.board[key] = value

    def show(self):
        """Allow the cells to appear on the interactive game screen."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()
