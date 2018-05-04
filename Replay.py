import pickle
from population_pro import POPULATION

f = open("robot_1.p", "rb")

play = pickle.load(f)

play.Start_Evaluation(False, True)

f.close()