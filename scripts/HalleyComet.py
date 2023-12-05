
import matplotlib.animation as animation 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
import numpy as np

#Global

centrosol = (16.78, 0) #Sol
solradio = (0.3)
sol = Circle(centrosol, solradio)
sol.set_color('yellow')

plt.style.use('dark_background') #background
fig, ax = plt.subplots()
ax.add_patch(sol)
ax.set_aspect('equal')

    #Figures
orbit = Ellipse(xy=(0, 0), width=34.74, height=8.96, 
                            edgecolor='gray', fc='None', lw=1.2, ls = '-.')

    #Image
ax.add_patch(orbit)  

    # Image size
ax.set_xlim(-20, 20)
ax.set_ylim(-6, 6)

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
	x = 17.37 * np.cos(t) 
	y = 4.4887 * np.sin(t)
        
 # appending values to the previously empty x and y data holders 
	xdata.append(x) 
	ydata.append(y) 
	line.set_data([x], [y])  #Pass x and y as lists

	return line, 

    #Calling the animation function
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                                frames = 505, interval = 20, blit = True) 

#anim.save('animação.gif', writer='pillow')

plt.show()