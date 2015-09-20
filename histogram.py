import numpy as np
import matplotlib.pyplot as plt
import sys, os

data = np.loadtxt((sys.path[0] + "/Daily Journals/data.txt"), comments='#', skiprows=1, usecols=(2,3))
data = data.tolist()
data.sort()

days = np.array([pair[0] for pair in data])
words = np.array([pair[1] for pair in data])

print np.sum(words).astype('str') + " total words"

m, b = np.polyfit(days, words, 1)

plt.plot(days, words, '.')
plt.plot(days, m*days + b, '-')

plt.show()
