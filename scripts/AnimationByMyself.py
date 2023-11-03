#AnimationByMyself
import matplotlib.animation as animation 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
import numpy as np

centrosol = (0, 0)
solradio = (0.5)
plt.style.use('dark_background')

#Figures
sol = Circle(centrosol, solradio)
orbit = Ellipse(xy=(3, 0), width=13.2, height=6, 
                        edgecolor='gray', fc='None', lw=2, ls = '-.')

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
    # t is a parameter which varies 
	# with the frame number 
	t = 0.05 * i 
	
	# x, y values to be plotted 
	x = 3 + 6.7 * np.sin(t) 
	y = 3 * np.cos(t) 
	
	# appending values to the previously 
	# empty x and y data holders 
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(x, y) 
	
	return line, 

anim = animation.FuncAnimation(fig, animate, init_func = init, 
							frames = 500, interval = 20, blit = True) 

plt.show()