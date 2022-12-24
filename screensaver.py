import time
import random
import curses

# Initialize curses
stdscr = curses.initscr()
curses = curses.newwin(0, 0, 0, 0)
curses.keypad(1)
curses.nodelay(1)

# Set up colors
curses.bkgd(' ', curses.color_pair(1))
curses.refresh()

# Main loop
while True:
    # Check for user input
    c = cursed.getch()
    if c == ord('q'):
        break

    # Clear the screen
    cursed.clear()

    # Draw some random characters on the screen
    for i in range(random.randint(10, 20)):
        x = random.randint(0, curses.COLS - 1)
        y = random.randint(0, curses.LINES - 1)
        c = random.choice(['#', '@', '$', '%', '&', '*', '+', '-', '.', '/'])
        cursed.addstr(y, x, c)

    # Refresh the screen
    cursed.refresh()

    # Sleep for a short period of time
    time.sleep(0.1)

# Clean up curses
curses.keypad(0)
curses.nodelay(0)
curses.clear()
curses.refresh()
curses.endwin()
