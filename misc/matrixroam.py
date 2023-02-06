import numpy as np
import curses
import random

# Initialize the matrix with "." and "|" characters
matrix = np.full((10, 10), ".")
matrix[:, 0] = "|"
matrix[:, 9] = "|"
matrix[0, :] = "-"
matrix[9, :] = "-"

# Initialize the player position
player_pos = [1, 1]
matrix[player_pos[0], player_pos[1]] = "@"

# Initialize the curses screen
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)

alert_messages = ["You found a treasure!", "You found a monster!", "You found a secret passage!"]

# Initialize a dictionary to store the files on each "." field
files = {}

while True:
    # Print the matrix
    for i in range(10):
        stdscr.addstr(i, 0, "".join(matrix[i]))
    stdscr.refresh()

    # Get the user input
    key = stdscr.getch()
    if key == curses.KEY_UP:
        if player_pos[0] > 1:
            player_pos[0] -= 1
    elif key == curses.KEY_DOWN:
        if player_pos[0] < 8:
            player_pos[0] += 1
    elif key == curses.KEY_LEFT:
        if player_pos[1] > 1:
            player_pos[1] -= 1
    elif key == curses.KEY_RIGHT:
        if player_pos[1] < 8:
            player_pos[1] += 1
    elif key == ord(" "):
        if matrix[player_pos[0], player_pos[1]] == ".":
            # Show a random alert message
            alert_message = random.choice(alert_messages)
            stdscr.addstr(11, 0, alert_message)
            stdscr.refresh()
            stdscr.getch()
            stdscr.addstr(11, 0, " "*len(alert_message))
            stdscr.refresh()
            pos = tuple(player_pos)
            if pos in files:
                stdscr.addstr(11, 0, "file :" + files[pos] + " already exists.")
                stdscr.refresh()
                stdscr.getch()
                stdscr.addstr(11, 0, " "*len("file :" + files[pos] + " already exists."))
                stdscr.refresh()
            else:
                stdscr.addstr(11, 0, "Enter file name:")
                stdscr.refresh()
                file_name = stdscr.getstr().decode()
                files[pos] = file_name
                stdscr.addstr(11, 0, "File saved at: " + str(pos))
                stdscr.refresh
                stdscr.getch()
                stdscr.addstr(11, 0, " "*len("File saved at: " + str(pos)))
                stdscr.refresh()
        else:
            stdscr.addstr(11, 0, "You can't save a file here!")
            stdscr.refresh()
            stdscr.getch()
            stdscr.addstr(11, 0, " "*len("You can't save a file here!"))
            stdscr.refresh()
    elif key == ord("q"):
        break

    # Clear the player position
    matrix[player_pos[0], player_pos[1]] = "."

    # Update the player position
    matrix[player_pos[0], player_pos[1]] = "@"

# Close the curses screen
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()