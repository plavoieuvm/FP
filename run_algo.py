from population_pro import POPULATION
import constants_pro as c
import time
import matplotlib.pyplot as plt
import pickle
import copy

parents = POPULATION(c.popSize)

parents.Initialize()

parents.Evaluate(pb=True, pp=False)

print "0",
parents.Print()

start_time = time.time()

fitnesses = []

fitnesses.append(parents.p[0].fitness)

g=0

try:
    while True:

#while (time.time() - start_time) < 2000:    # 21600

#for g in range(1, c.numGens):

        g = g + 1

        children = copy.deepcopy(parents)

        oldBest = children.getBestIndex()

        children.Mutate()

        #children.Fill_From(parents)

        children.Evaluate(pp=False, pb=True)

        newBest = children.getBestIndex()

        children.LookForNewBest2(oldBest, newBest, g)

        parents.ReplaceWith(children)

        print g,
        parents.Print()

        fitnesses.append(parents.getBestFit())

        #children.Reset()


except KeyboardInterrupt:
    pass


parents.p[parents.getBestIndex()].Start_Evaluation(pb=False, pp=True)


f = plt.figure()

panel = f.add_subplot(111)

plt.plot(fitnesses)

plt.title('Best Fitness by Generation (w/ Parallel Hill Climber)')
plt.ylabel('Best Fitness')
plt.xlabel('Generation')


plt.show()

