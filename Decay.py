import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import colors
from Isotope import Isotope
import random

class Decay (object):
    
    # Initialize instance variables
    def __init__ (self, isotope, timeStep):
        self.timeStep = timeStep
        self.probabilityOfDecay = isotope.decayConstant * timeStep
        self.isotope = isotope
        self.timer = 0
        self.historicalIsotope = [isotope.isotopeArray]

    # Iterates through the isotope every time step (until the half the isotope is left) and for every undecayed 
    # nuclus, generates a random number which, if smaller than the probability of decay, will cause the nucleus to decay. 
    def radioactiveRecay (self):
        self.isotope.remainingNuclei = self.isotope.initialNuclei
        self.timer = 0
        while self.isotope.remainingNuclei > self.isotope.initialNuclei // 2:
            self.isotope.isotopeArray = ([(list (map (lambda nucleus: self.__decideDecay(nucleus), row))) for row in self.isotope.isotopeArray])
            self.timer += self.timeStep
            self.historicalIsotope +=[self.isotope.isotopeArray]

    # Animates the radioactive decay of the isotope 
    def animateDecay (self):
        fig = plt.figure()
        images = []
        for array2D in self.historicalIsotope:
            plt.title("Isotope Decay: ", fontsize = 16)
            renderImage = plt.pcolor(array2D, cmap = colors.ListedColormap (["Red", "Green"]), edgecolors='k', linewidth = 2, animated = True)
            images.append([renderImage])   
        ani = animation.ArtistAnimation(fig, images, interval = 0.01, blit = True, repeat_delay = 2000)
        plt.show()

    def averageHalflife (self, iterations):
        print ("Calculating average half-life ...")
        counter = 1
        historicalHalflife = np.array([])
        while counter <= iterations:
            print ("Iteration: " + str(counter) + " / " + str(iterations), end = '\r')
            self.isotope.remainingNuclei = self.isotope.initialNuclei
            self.timer = 0
            self.isotope.isotopeArray = self.isotope.createNewIsotope()
            while self.isotope.remainingNuclei > self.isotope.initialNuclei // 2:
                self.isotope.isotopeArray = [ list(map (lambda nucleus: self.__decideDecay(nucleus), row)) for row in self.isotope.isotopeArray]
                self.timer += self.timeStep
            historicalHalflife = np.append (historicalHalflife, self.timer)
            counter += 1
        return np.average(historicalHalflife)
            
    # Private function which decides whether a nuclus will decay or not
    def __decideDecay (self, nucleus):
        if nucleus == 1: 
            randomNumber = random.random()
            if randomNumber <= self.probabilityOfDecay:
                self.isotope.remainingNuclei -= 1
                return 0
            else:
                return 1
        else:
            return 0

      