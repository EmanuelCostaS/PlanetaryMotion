
import matplotlib.animation as animation 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
import numpy as np

#Global variables
centrosol = (0, 0)
solradio = (0.5)
t_increment = 0.01

plt.style.use('dark_background')

#Figures
sol = Circle(centrosol, solradio)
orbit = Ellipse(xy=(3, 0), width=13.2, height=6, 
                        edgecolor='gray', fc='None', lw=1.2, ls = '-.')

#Image
fig, ax = plt.subplots()

ax.add_patch(sol)
sol.set_color('yellow')

ax.add_patch(orbit)

ax.set_aspect('equal')

#Tamanho da imagem
ax.set_xlim(-5, 11)
ax.set_ylim(-4, 4)

def init(): 
	line.set_data([], []) 
	return line, 

line, = ax.plot([], [], 'o')

xdata, ydata = [], []

#Animation
def animate(i):
  
    # t is a parameter which varies with the frame number 
	t = 0.05 * i
	
	# x, y values to be plotted 
	x = 3 + 6.7 * np.sin(t) 
	y = 3 * np.cos(t) 
	
    # calculate and print the distance to the sun
	r = round(np.sqrt((x - centrosol[0])**2 + (y - centrosol[1])**2), 2)

	print(f"Distance to the sun at frame: {r}, i is {i}, t is {round(t, 2)}, x is {round(x, 2)} and y is {round(y, 2)}")
	
	# appending values to the previously empty x and y data holders 
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(x, y) 

	t -= t_increment

	return line, 

#Calling the animation function
anim = animation.FuncAnimation(fig, animate, init_func = init, 
							frames = 500, interval = 20, blit = True) 

plt.show()