import numpy as np
import math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)
    for i in range(N):
        for j in range(N):
            if i==j :
                dist[i][j]=np.inf
            else :
                dist[i][j]= sum(abs(x-y) for x,y in zip(data[i], data[j]))
    print(np.unravel_index(np.argmin(dist), dist.shape))

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 

    wordsInText = text.split()
    words = list(set(wordsInText))
    docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    docFreqs = np.empty(len(words), dtype=float)
    termFreqs = np.empty((len(docs),len(words)), dtype=float)

    for i , word in enumerate(words) :
        docFreqs[i] = sum(word in doc for doc in docs)/len(docs)
        for j , doc in enumerate(docs) :
            termFreqs[j][i] = doc.count(word)/len(doc)
    
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    it_idf = np.empty((len(docs),len(words)), dtype=float)
    for i in range(len(words)) :
        for j in range(len(docs)):
            it_idf[j][i] = termFreqs[j][i]*math.log(1/docFreqs[i],10)

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    find_nearest_pair(it_idf)


main(text)
