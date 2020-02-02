from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib import patches
import numpy as np

class Isotope (object):
    
    def __init__(self, size, decayConstant):
        self.size = size
        self.decayConstant = decayConstant
        self.initialNuclei = size * size
        self.remainingNuclei = size * size
        self.isotopeArray = self.createNewIsotope()

    #Creates a size x size list of 1s
    def createNewIsotope (self):
        row = [ 1 for i in range (0, self.size)]
        array2D = [row for i in range (0, self.size)]
        return array2D
    
    #Displays the isotope using matplotlib
    def displayIsotope (self):
        plt.axis('off')
        plt.title("Isotope Decay: ", fontsize = 16)
        redLabel = patches.Patch(color='red', label='Decayed nuclei')
        greenLabel = patches.Patch(color='green', label='Undecayed nuclei')
        plt.legend(handles=[redLabel,greenLabel])
        plt.pcolor(self.isotopeArray, cmap = colors.ListedColormap (["Red", "Green"]), edgecolors='k', linewidth = 2)
        plt.show()




