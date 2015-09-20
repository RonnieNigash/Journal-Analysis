import numpy as np
import matplotlib.pyplot as plt

with open("/Daily Journals/data.txt") as f:
	data = f.read()

data = data.split('\n')
data = data.pop(0) # get rid of words at top

days = [row.split(' ')[2] for row in data] # month, date, days, words is format
words = [row.split(' ')[-1] for row in data]

graph = plt.figure()

