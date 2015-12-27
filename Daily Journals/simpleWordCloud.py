from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

directory = path.dirname(__file__)

# Read text
text = open(path.join(directory, "fileContents.txt")).read()
wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
