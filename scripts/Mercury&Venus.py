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
Mercury_orbit = Ellipse(xy=(0, 0), width=7.8, height=7.632, 
                            edgecolor='gray', fc='None', lw=1.2, ls = '-.')

Venus_orbit = Ellipse(xy=(-0.795, 0), width=14.46, height=14.44, 
                            edgecolor='gray', fc='None', lw=1.2, ls = '-.')

    #Image
ax.add_patch(Mercury_orbit)
ax.add_patch(Venus_orbit)

    # Image size
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

x_mercury_data, y_mercury_data = [], []
x_venus_data, y_venus_data = [], []

line_mercury, = ax.plot([], [], 'o')
line_venus, = ax.plot([], [], 'o')

def init(): 
    line_mercury.set_data([], []) 
    line_venus.set_data([], [])  
    return line_mercury, line_venus,

    #Animation
def animate(i):
    
    #t is a parameter which varies with the frame number 
    t = 0.05 * i
        
    #x, y values to be plotted 
    x_mercury = 3.9 * np.cos(t) 
    y_mercury = 3.816 * np.sin(t)

    x_venus = -0.795 + 7.23 * np.cos(t*0.5) 
    y_venus = 7.22 * np.sin(t*0.5)
        
    #Appending values to the previously empty x and y data holders 
    x_mercury_data.append(x_mercury) 
    y_mercury_data.append(y_mercury) 
    line_mercury.set_data([x_mercury], [y_mercury])
    
    x_venus_data.append(x_venus) 
    y_venus_data.append(y_venus) 
    line_venus.set_data([x_venus], [y_venus]) 

    return line_mercury, line_venus,

    #Calling the animation function
anim = animation.FuncAnimation(fig, animate, init_func = init, 
                                frames = 505, interval = 20, blit = True) 

plt.show()
