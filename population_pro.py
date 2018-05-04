from individual_pro import INDIVIDUAL
import copy
import random
import constants_pro as c
import pickle


class POPULATION:

    def __init__(self, popSize):

        self.p = {}
        self.popSize = popSize


    def Reset(self):


        for i in self.p:
            self.p[i].fitness = 0

    def Initialize(self):

        for i in range(0, self.popSize):

            self.p[i] = INDIVIDUAL(i)

    def Print(self):

        for i in self.p:
            if (i in self.p):
                self.p[i].Print()
        print ("")


    def Evaluate(self, pb, pp):

        for i in self.p:

            #self.p[i].fitness = 0

            self.p[i].Start_Evaluation(pb, pp)

            self.p[i].Compute_Fitness()


    def Fill_From(self, other):

        self.Copy_Best_From(other)

        self.Collect_Children_From(other)

    def Copy_Best_From(self, other):

        best = -10000000000000000
        index = -1

        for i in other.p:
            if other.p[i].fitness > best:
                best = other.p[i].fitness
                index = i

        self.p[0] = copy.deepcopy(other.p[index])
        return index

    def Collect_Children_From(self, other):

        for i in other.p:
            winner = other.Winner_Of_Tournament_Selection()
            if i != 0:
                self.p[i] = copy.deepcopy(winner)
                self.p[i].Mutate()

                # self.p[i] = copy.deepcopy(other.p[i])

    def Winner_Of_Tournament_Selection(other):

        p1 = random.randint(0, len(other.p)-1)
        p2 = random.randint(0, len(other.p)-1)

        while p1 == p2:
            p2 = random.randint(0, len(other.p) - 1)

        if other.p[p1].fitness > other.p[p2].fitness:

            return other.p[p1]
        else:
            return other.p[p2]

    def Mutate(self):

        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):

        for i in self.p:
            if self.p[i].fitness < other.p[i].fitness:

                self.p[i] = other.p[i]


    def LookForNewBest(self, other, g):

        for i in self.p:

            if (self.p[i].fitness < other.p[i].fitness) and (i == 0):

                name = "robot_" + str(g) + ".p"
                f = open(name, "wb")

                pickle.dump(self.p[i], f)

                f.close()

















