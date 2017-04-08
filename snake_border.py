# SNAKE
# This is a good exercise to use the curses module in Python
# I suggest you read these two codes, I have found them very useful
# Code 1: https://gist.github.com/sanchitgangwar/2158089
# Code 2: https://gist.github.com/claymcleod/b670285f334acd56ad1c

# Instructions:
# Arrow keys to move the snake, P to pause the game and Q to exit 


import curses
import random


curses.initscr()
curses.noecho()
curses.curs_set(0)

# Create the field
begin_x = 0
begin_y = 0
height = 15
width = 45
win = curses.newwin(height, width, begin_y, begin_x)
win.keypad(1)
win.border(0)
#win.nodelay(1)

g = curses.KEY_RIGHT
j = 0
k = 0

# Create snake vector
snake = [[10,20,'#'],[10,21,'#'],[10,22,'#'],[10,23,'#'],[10,24,'#'],[10,25,'#']]                                                     
win.addstr(snake[0][0], snake[0][1], '######')

 
# Pick random food coordinate, avoiding the snake
a = 0
x = random.randint(1,height-2)
y = random.randint(1,width-2)
while a < len(snake):
	if (x == snake[a][0] and y == snake[a][1]):
		x = random.randint(1,height-2)
		y = random.randint(1,width-2)
		a = 0
		continue
	a += 1


food = [x,y,'*']
win.addch(food[0], food[1], '*')
		


# Wait for next input
k = win.getch()

points = 0
win.addstr(0,5,str(points))
speed = 100

# The game goes on until the player presses Q key
while (k != ord('q') and k != ord('Q')):
	

		
	# The snake keeps going straight until the player presses another arrow key
	while (k == curses.KEY_DOWN):
		if (g == curses.KEY_UP):
			k = curses.KEY_UP
			break
		# Set snake speed		
		win.timeout(speed)		
		i = 0
		a = snake[0][0]
		b = snake[0][1]
		while (i < (len(snake)-1)):
			snake[i][0] = snake[i+1][0]
			snake[i][1] = snake[i+1][1]
			i += 1			
		snake[len(snake)-1][0] = snake[len(snake)-1][0] + 1
		i = 0
		# If the snake eats itself, the while cycle breaks
		while (i < (len(snake)-1)):
			if (snake[len(snake)-1][0] == snake[i][0] and snake[len(snake)-1][1] == snake[i][1]):
				j = 1
				break
			i += 1
		if j == 1:
			break
		# When the snake eats its food, another random food coordinate is chosen and the snake grows
		if (snake[len(snake)-1][0] == food[0] and snake[len(snake)-1][1] == food[1]):
			c = food[0]
			d = food[1]
			snake.insert(len(snake), [c,d,'#'])
			win.addch(snake[len(snake)-1][0], snake[len(snake)-1][1], '#')
			win.addch(snake[len(snake)-2][0], snake[len(snake)-2][1], '#')
			win.addch(a,b,' ')
			a = 0
			food[0] = random.randint(1,height-2)
			food[1] = random.randint(1,width-2)
			while a < len(snake):
				if (food[0] == snake[a][0] and food[1] == snake[a][1]):
					food[0] = random.randint(1,height-2)
					food[1] = random.randint(1,width-2)
					a = 0
					continue
				a += 1

			points = points + 10
			win.addstr(0,5,str(points))
			# When snake eats two foods, the speed increases			
			while (speed >= 80):
				if ((points/10)%2 == 0):
					speed = speed - 2
					break
				if ((points/10)%2 == 1):
					break
			win.addch(food[0], food[1], '*')
			
		# The snake moves
		elif (snake[len(snake)-1][0] != food[0] or snake[len(snake)-1][1] != food[1]):
			win.addch(snake[len(snake)-1][0], snake[len(snake)-1][1], '#')
			win.addch(a,b,' ')
		# If the snake touches the border, the while cycle breaks
		if snake[len(snake)-1][0] == height-1:
			break	
		g = curses.KEY_DOWN
		k = win.getch()
    		if k == -1:
			k = curses.KEY_DOWN
		# Press P key to pause 
		elif (k == ord('p') or k == ord('P')):
			k = 0		
			while (win.getch() != ord('p') and win.getch() != ord('P')):
				continue
			k = curses.KEY_DOWN
			
		elif (k != curses.KEY_UP and k != curses.KEY_RIGHT and k != curses.KEY_LEFT and k != ord('q') and k!= ord('Q') and k != ord('p') and k!= ord('P')):
			k = curses.KEY_DOWN

			
	if (snake[len(snake)-1][0] == height-1 or j == 1):
		break
			
	# Repeat the code for the other directions
	

			
	while (k == curses.KEY_UP):
		if (g == curses.KEY_DOWN):
			k = curses.KEY_DOWN
			break
		win.timeout(speed)
		i = 0
		a = snake[0][0]
		b = snake[0][1]
		while (i < (len(snake)-1)):
			snake[i][0] = snake[i+1][0]
			snake[i][1] = snake[i+1][1]
			i += 1			
		snake[len(snake)-1][0] = snake[len(snake)-1][0] - 1
		i = 0
		while (i < (len(snake)-1)):
			if (snake[len(snake)-1][0] == snake[i][0] and snake[len(snake)-1][1] == snake[i][1]):
				j = 1
				break
			i += 1
		if j == 1:
			break
		if (snake[len(snake)-1][0] == food[0] and snake[len(snake)-1][1] == food[1]):
			c = food[0]
			d = food[1]
			snake.insert(len(snake), [c,d,'#'])
			win.addch(snake[len(snake)-1][0], snake[len(snake)-1][1], '#')
			win.addch(snake[len(snake)-2][0], snake[len(snake)-2][1], '#')
			win.addch(a,b,' ')
			a = 0
			food[0] = random.randint(1,height-2)
			food[1] = random.randint(1,width-2)
			while a < len(snake):
				if (food[0] == snake[a][0] and food[1] == snake[a][1]):
					food[0] = random.randint(1,height-2)
					food[1] = random.randint(1,width-2)
					a = 0
					continue
				a += 1

			points = points + 10
			win.addstr(0,5,str(points))
			while (speed >= 80):
				if ((points/10)%2 == 0):
					speed = speed - 2
					break
				if ((points/10)%2 == 1):
					break
			win.addch(food[0], food[1], '*')		
		elif (snake[len(snake)-1][0] != food[0] or snake[len(snake)-1][1] != food[1]):
			win.addch(snake[len(snake)-1][0], snake[len(snake)-1][1], '#')
			win.addch(a,b,' ')			
		if snake[len(snake)-1][0] == 0:
			break	
		g = curses.KEY_UP
		k = win.getch()
    		if k == -1:
			k = curses.KEY_UP
		elif (k == ord('p') or k == ord('P')):
			k = 0		
			while (win.getch() != ord('p') and win.getch() != ord('P')):
				continue
			k = curses.KEY_UP
			
		elif (k != curses.KEY_DOWN and k != curses.KEY_RIGHT and k != curses.KEY_LEFT and k != ord('q') and k!= ord('Q') and k != ord('p') and k!= ord('P')):
			k = curses.KEY_UP

	if (snake[len(snake)-1][0] == 0 or j == 1):
		break



		
	while (k == curses.KEY_RIGHT):
		if (g == curses.KEY_LEFT):
			k = curses.KEY_LEFT
			break
		win.timeout(speed)		
		i = 0
		a = snake[0][0]
		b = snake[0][1]
		while (i < (len(snake)-1)):
			snake[i][0] = snake[i+1][0]
			snake[i][1] = snake[i+1][1]
			i += 1			
		snake[len(snake)-1][1] = snake[len(snake)-1][1] + 1
		i = 0
		while (i < (len(snake)-1)):
			if (snake[len(snake)-1][0] == snake[i][0] and snake[len(snake)-1][1] == snake[i][1]):
				j = 1
				break
			i += 1
		if j == 1:
			break
		if (snake[len(snake)-1][0] == food[0] and snake[len(snake)-1][1] == food[1]):
			c = food[0]
			d = food[1]
			snake.insert(len(snake), [c,d,'#'])
			win.addch(snake[len(snake)-1][0], snake[len(snake)-1][1], '#')
			win.addch(snake[len(snake)-2][0], snake[len(snake)-2][1], '#')
			win.addch(a,b,' ')
			a = 0
			food[0] = random.randint(1,height-2)
			food[1] = random.randint(1,width-2)
			while a < len(snake):
				if (food[0] == snake[a][0] and food[1] == snake[a][1]):
					food[0] = random.randint(1,height-2)
					food[1] = random.randint(1,width-2)
					a = 0
					continue
				a += 1

			points = points + 10
			win.addstr(0,5,str(points))
			while (speed >= 80):
				if ((points/10)%2 == 0):
					speed = speed - 2
					break
				if ((points/10)%2 == 1):
					break
			win.addch(food[0], food[1], '*')		
		elif (snake[len(snake)-1][0] != food[0] or snake[len(snake)-1][1] != food[1]):
			win.addch(snake[len(snake)-1][0], snake[len(snake)-1][1], '#')
			win.addch(a,b,' ')
		if snake[len(snake)-1][1] == width-1:
			break	
		g = curses.KEY_RIGHT
		k = win.getch()
    		if k == -1:
			k = curses.KEY_RIGHT
		elif (k == ord('p') or k == ord('P')):
			k = 0		
			while (win.getch() != ord('p') and win.getch() != ord('P')):
				continue
			k = curses.KEY_RIGHT
			
		elif (k != curses.KEY_UP and k != curses.KEY_DOWN and k != curses.KEY_LEFT and k != ord('q') and k!= ord('Q') and k != ord('p') and k!= ord('P')):
			k = curses.KEY_RIGHT

	if (snake[len(snake)-1][1] == width-1 or j == 1):
		break	
	

		
	while (k == curses.KEY_LEFT):
		if (g == curses.KEY_RIGHT):
			k = curses.KEY_RIGHT
			break
		win.timeout(speed)		
		i = 0
		a = snake[0][0]
		b = snake[0][1]
		while (i < (len(snake)-1)):
			snake[i][0] = snake[i+1][0]
			snake[i][1] = snake[i+1][1]
			i += 1			
		snake[len(snake)-1][1] = snake[len(snake)-1][1] - 1
		i = 0
		while (i < (len(snake)-1)):
			if (snake[len(snake)-1][0] == snake[i][0] and snake[len(snake)-1][1] == snake[i][1]):
				j = 1
				break
			i += 1
		if j == 1:
			break
		if (snake[len(snake)-1][0] == food[0] and snake[len(snake)-1][1] == food[1]):
			c = food[0]
			d = food[1]
			snake.insert(len(snake), [c,d,'#'])
			win.addch(snake[len(snake)-1][0], snake[len(snake)-1][1], '#')
			win.addch(snake[len(snake)-2][0], snake[len(snake)-2][1], '#')
			win.addch(a,b,' ')
			a = 0
			food[0] = random.randint(1,height-2)
			food[1] = random.randint(1,width-2)
			while a < len(snake):
				if (food[0] == snake[a][0] and food[1] == snake[a][1]):
					food[0] = random.randint(1,height-2)
					food[1] = random.randint(1,width-2)
					a = 0
					continue
				a += 1

			points = points + 10
			win.addstr(0,5,str(points))
			while (speed >= 80):
				if ((points/10)%2 == 0):
					speed = speed - 2
					break
				if ((points/10)%2 == 1):
					break
			win.addch(food[0], food[1], '*')		
		elif (snake[len(snake)-1][0] != food[0] or snake[len(snake)-1][1] != food[1]):
			win.addch(snake[len(snake)-1][0], snake[len(snake)-1][1], '#')
			win.addch(a,b,' ')		
		if snake[len(snake)-1][1] == 0:
			break	
		g = curses.KEY_LEFT
		k = win.getch()
    		if k == -1:
			k = curses.KEY_LEFT
		elif (k == ord('p') or k == ord('P')):
			k = 0		
			while (win.getch() != ord('p') and win.getch() != ord('P')):
				continue
			k = curses.KEY_LEFT
			
		elif (k != curses.KEY_UP and k != curses.KEY_RIGHT and k != curses.KEY_DOWN and k != ord('q') and k!= ord('Q') and k != ord('p') and k!= ord('P')):
			k = curses.KEY_LEFT

	if (snake[len(snake)-1][1] == 0 or j == 1):
		break		

	
# If the snake eats itself or touches the border, print GAME OVER	
while (k != ord('q') and k != ord('Q')):
	if (snake[len(snake)-1][0] == height-1 or snake[len(snake)-1][0] == 0 or snake[len(snake)-1][1] == width-1 or snake[len(snake)-1][1] == 0 or j ==1):
		title = "GAME OVER"
		subtitle = "Press Q to exit"
		x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
		x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
		y_title = int((height // 2) - 2)
       		win.addstr(y_title, x_title, title)
		win.addstr(y_title+1, x_subtitle, subtitle)
	k = win.getch()
	if (k == ord('q') or k == ord('Q')):
		break

while (k == ord('q') or k == ord('Q')):
	break
		 
curses.endwin()


 

	
