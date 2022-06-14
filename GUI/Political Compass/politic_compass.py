import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.collections import PolyCollection
def plot_compass(coordinates):
    def get_cube():
        phi = np.arange(1,10,2)*np.pi/4
        Phi, Theta = np.meshgrid(phi, phi)
        x = np.cos(Phi)*np.sin(Theta)
        y = np.sin(Phi)*np.sin(Theta)
        z = np.cos(Theta)/np.sqrt(2)
        return x,y,z
    def plot_cube(pad1, pad2, pad3, color):
        ax.plot_surface(x * a + pad1, y * a + pad2, z * a + pad3, alpha=0.1, color=color)
    def title_set():
        mylabel = ""
        for a, left, right in zip([px, py, pz], lefts, rights):
            mylabel += " "
            if a > 0:
                mylabel += right
            else:
                mylabel += left
        ax.set_title(f"Economic Axis: {px} | Governmental Axis: {py} | Cultural Axis: {pz}\nYou are closest to a{mylabel}.")

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")
    zero = [0, 0]
    moving = [-60, 60]
    a = 60
    x,y,z = get_cube()
    pad = 30
    plot_cube(pad, pad, pad, "skyblue")
    plot_cube(pad, -1*pad, pad, "yellow")
    plot_cube(-1*pad, pad, pad, "red")
    plot_cube(-1*pad, -1*pad, pad, "lightgreen")
    plot_cube(pad, pad, -1*pad, "#154360")
    plot_cube(pad, -1*pad, -1*pad, "goldenrod")
    plot_cube(-1*pad, pad, -1*pad, "darkred")
    plot_cube(-1*pad, -1*pad, -1*pad, "darkgreen")
    lim = 60
    ax.set_xlim(-1*lim,lim)
    ax.set_ylim(-1*lim,lim)
    ax.set_zlim(-1*lim,lim)
    ax.plot(zero, moving, color="black", lw="2")
    ax.plot(moving, zero, color="black", lw="2")
    ax.plot3D(zero, zero, moving, color="black", lw="2")
    ax.set_xlabel('Left <--> Right')
    ax.set_ylabel('\n\nLibertarian <--> Authoritarian')
    ax.set_zlabel('Progressive <--> Conservative')

    px, py, pz = coordinates
    ax.plot3D(px, py, pz,  'P', color="black", label="You")
    ax.plot3D(px, -1*pad*2, -1*pad*2,  'v', color="red")
    ax.plot3D(pad*2, py, -1*pad*2,  'v', color="red")
    ax.plot3D(pad*2, pad*2, pz,  'v', color="red")
    ax.plot3D(np.linspace(0, px, num=20), np.linspace(0, py, num=20), np.linspace(0, pz, num=20), ls=":", lw="3", color="red")

    lefts = ["Left-Wing", "Libertarian", "Progressive"]
    rights = ["Right-Wing", "Authoritarian", "Conservative"]
    title_set()
    plt.legend()
    plt.show()

def random():
    return np.random.randint(-60, 61)
#plot_compass([random(), random(), random()])