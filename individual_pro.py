import random
import math
import pyrosim
#from robot_pro import ROBOT
#from robot_pro2 import ROBOT   # NO FEET
from robot_pro2_0 import ROBOT
import numpy
import constants_pro as c


class INDIVIDUAL:

    def __init__(self, i):

        self.ID = i

        #self.genome = numpy.random.random((4,4)) * 2 - 1

        self.genome = numpy.random.random((8,8)) * 2 - 1

        # print self.genome

        self.fitness = 0

    def Start_Evaluation(self, pb, pp):

        self.sim = pyrosim.Simulator(eval_time=c.evalTime, dt=.02, play_blind=pb, play_paused=pp)  # .02

        self.robot = ROBOT(self.sim, self.genome)

        # Start

        self.sim.start()

    def Compute_Fitness(self):

        self.sim.wait_to_finish()

        # distance into screen
        #
        # x = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=0)
        # y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
        #
        # self.fitness = y[-1] + x[-2]

        x = self.sim.get_sensor_data(sensor_id=self.robot.position, svi=0)
        #z = self.sim.get_sensor_data(sensor_id=self.robot.position, svi=2)

        orienX = self.sim.get_sensor_data(sensor_id=self.robot.veS, svi=0)


        self.fitness = x[-1] - (orienX[-1])


        del self.sim
        del self.robot

        #print(self.fitness)


    def Mutate(self):

        #geneToMutateRow = random.randint(0, 3)
        #geneToMutateCol = random.randint(0,3)

        geneToMutateRow = random.randint(0, 7)
        geneToMutateCol = random.randint(0,7)

        self.genome[geneToMutateRow][geneToMutateCol] = random.gauss(self.genome[geneToMutateRow][geneToMutateCol],
                                                    math.fabs(self.genome[geneToMutateRow][geneToMutateCol]))

        if self.genome[geneToMutateRow][geneToMutateCol] > 1:
            self.genome[geneToMutateRow][geneToMutateCol] = 1

        if self.genome[geneToMutateRow][geneToMutateCol] < 1:
            self.genome[geneToMutateRow][geneToMutateCol] = -1


    def Print(self):

        print "[ ", self.ID, " ", self.fitness, "]",









