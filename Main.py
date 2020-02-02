import math
from Isotope import Isotope
from Decay import Decay

def main ():

    # Receive isotope data
    decayConstant = float (input ("Decay Constant: "))
    arrayLength = int (input ("Array Length: "))
    timeStep = float (input ("Time Step: "))
    iterations = int (input("Iterations: "))
    
    # Create an isotope object
    myIsotope = Isotope(arrayLength, decayConstant)

    # Create a decay object
    isotopeDecay = Decay(myIsotope, timeStep)
    
    # Call the radioactive decay method
    isotopeDecay.radioactiveRecay()
    
    # Return basic data after the half-life is reached
    print ("Initial number of undecayed nuclei: " + str (myIsotope.initialNuclei))
    print ("Final number of undecayed nuclei: " + str (myIsotope.remainingNuclei))
    print ("Simulated half life: " + str (isotopeDecay.timer))
    print ("Actual half life: " + str (math.log(2) / myIsotope.decayConstant))
    
    # Animation of the decay process
    isotopeDecay.animateDecay()

    # Visual representation of the isotope at the half life
    myIsotope.displayIsotope()

    print ("Average half life over " + str (iterations) + " iterations : " + str(isotopeDecay.averageHalflife(iterations)))
main ()

