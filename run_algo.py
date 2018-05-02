from population_pro import POPULATION
import constants_pro as c
import time

parents = POPULATION(c.popSize)

parents.Initialize()

parents.Evaluate(pb=True, pp=False)

print "0",
parents.Print()

start_time = time.time()

g=0
while (time.time() - start_time) < 120:

#for g in range(1, c.numGens):

    g = g + 1

    children = POPULATION(c.popSize)

    children.Fill_From(parents)

    children.Evaluate(pp=False, pb=True)

    print g,
    children.Print()

    parents.ReplaceWith(children)



parents.p[0].Start_Evaluation(pb=False, pp=True)


