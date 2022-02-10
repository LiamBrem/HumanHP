class Person():

    def __init__(self, weight, time, averageStep, totalStep):
        self.weight = float(weight) # Pounds
        self.time = float(time) # seconds
        self.averageStep = float(averageStep) # inches
        self.totalStep = float(totalStep) # number

        self.heightOfStairs = self.averageStep * self.totalStep # this is gonna have to be found at some point

        self.weight *= 4.4482216153 # converts from lbs to N

        self.averageStep *= 0.0254 # converts from inches to meters

    def workDone(self): # in joules
        print("WORK: " + str(self.heightOfStairs * self.weight))

        return self.heightOfStairs * self.weight # we're gonna have to get the height in here 

    def powerExpended(self): # in watts
        print("POWER: " + str(self.workDone() / self.time))

        return self.workDone() / self.time


    def horsepower(self): 
        print("HORSEPOWER: " + str(self.powerExpended()/746))

        return self.powerExpended()/746   