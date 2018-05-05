from population_pro import POPULATION
import constants_pro as c
import time
import matplotlib.pyplot as plt
import pickle

parents = POPULATION(c.popSize)

parents.Initialize()

parents.Evaluate(pb=False, pp=True)

print "0",
parents.Print()

start_time = time.time()

fitnesses = []

fitnesses.append(parents.p[0].fitness)

g=0

try:
    while True:
#while (time.time() - start_time) < 30:

#for g in range(1, c.numGens):

        g = g + 1

        children = POPULATION(c.popSize)

        children.Fill_From(parents)

        children.Evaluate(pp=False, pb=True)

        fitnesses.append(parents.p[0].fitness)

        print g,
        children.Print()

        #children.Reset()

        parents.LookForNewBest(children, g)

        parents.ReplaceWith(children)

except KeyboardInterrupt:
    pass


parents.p[0].Start_Evaluation(pb=False, pp=True)

# pickle.dump(fitnesses, open('fitnesses_test.p', 'wb'))

# print fitnesses

f = plt.figure()

panel = f.add_subplot(111)

plt.plot(fitnesses)

plt.title('Best Fitness by Generation (w/ Genetic Algorithm)')
plt.ylabel('Best Fitness')
plt.xlabel('Generations')


# panel.set_ylim(-1, +2)

plt.show()