class SentimentStore:
    def __init__(self):
       self._table = {}
       self._count = {}

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._table.keys())

    def addVertex( self, word):
        if v not in self._table.keys():
            self._table[word] = set([])

    def removevertex( self, word):
        if v in self._table.keys():
            del self._table[word]

    def addEdge( self, word, score):
        if not word in self._table.keys():
            self.addVertex(word)
        self._table[word].add(score)
        if not score in self._table.keys():
            self.addVertex(score)
        self._table[score].add(word)

    def removeEdge( self, word, score, directed=False ):
        for (w, s) in self._table[word]:
            if w == score:
                self._table[word].remove( (w,s) )
                break
            if not directed:
                for (w,s) in self._table[score]:
                    if s == word:
                        self._table[score].remove( (w,s) )
                        break

    def areNeighbours( self, word, score ):
        if word in self._table.keys():
            for (w,s) in self._table[word]:
                if w == score:
                    return True
        return False
   
    def getNumberOfWords(self):
        return len(self._table.keys())

    def getNumberOfPositiveWords(self):
        count = 0

        for  p in self._table.values():
            if p > 0:
                 count += 1
        
        # klar med loopen
        return count                

    def getNumberOfNegativeWords(self):
        count = 0

        for n in self._table.values():
            if n < 0:
                count += 1

        return count

    def getTotalWordCount(self):
        count = 0
        for w in self._count.values():
            count += w
        return count


    def addWordScore(self, word, score):
         if not word in self._table.keys():
             self._table[word] = score 
             self._count[word] = 1
         else:
             self._count[word] +=1
             self._table[word] += score

           
    def addStringScore(self, string, score):
        words = string.split(" ")
        for word in words:
            if len(word) > 3: # ignore short words
                self.addWordScore(word, score)


    def getWordSentiment(self, word): 
        try:
           return self._table[word] 
        except:
            return 0
    
        
    def getWordCount(self, word):
        try:
           return self._count[word]
        except:
            return 0
    

    def getNormalizedWordSentiment(self, word):
        # This function is important - by normalizing the data we compensate
        # for the fact that some words occurs far more often than others.
        if self.getWordCount(word) != 0:
            return self.getWordSentiment(word) / self.getWordCount(word)
        else:
            return 0


    def getStringSentiment(self, s):
        score = 0
        count = 0
        words = s.split(" ")
        for word in words:
            if len(word) > 3: # ignore short words
                count += 1
                word = word.lower()
                score += self.getNormalizedWordSentiment(word)
        return score / count





