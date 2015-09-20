import numpy as np
import matplotlib.pyplot as plt
import sys, os


data = np.loadtxt((sys.path[0] + "/Daily Journals/data.txt"), comments='#', skiprows=1, usecols=(2,3))
data = data.tolist()
data.sort()

