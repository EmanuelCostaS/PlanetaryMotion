import matplotlib.animation as animation 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
import numpy as np

#Global

centrosol = (-0.795, 0) #Sol
solradio = (0.5)
sol = Circle(centrosol, solradio)
sol.set_color('yellow')

plt.style.use('dark_background') #background
fig, ax = plt.subplots()
ax.add_patch(sol)
ax.set_aspect('equal')

    #Figures
orbit = Ellipse(xy=(0, 0), width=7.8, height=7.632, 
                            edgecolor='gray', fc='None', lw=1.2, ls = '-.')

    #Image
ax.add_patch(orbit)

    # Image size
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

xdata, ydata = [], []

line, = ax.plot([], [], 'o')

def init(): 
    line.set_data([], []) 
    return line, 

    #Animation
def animate(i):
    
    #t is a parameter which varies with the frame number 
    t = 0.05 * i
        
    #x, y values to be plotted 
    x = 3.9 * np.cos(t) 
    y = 3.816 * np.sin(t)
        
    #Appending values to the previously empty x and y data holders 
    xdata.append(x) 
    ydata.append(y) 
    line.set_data([x], [y])  #Pass x and y as lists

    return line, 

    #Calling the animation function
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                                frames = 505, interval = 20, blit = True) 

plt.show()
