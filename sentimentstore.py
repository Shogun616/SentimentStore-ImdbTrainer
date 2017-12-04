class SentimentStore:
    def __init__(self):
          self._table = {}

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._table.keys())

    def addVertex( self, word ):
        if word not in self._table.keys():
            self._table[word] = set([])

    def removevertex( self, word):
        if word in self._table.keys():
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
            if s == score:
                self._table[word].remove( (w,s) )
                break
            if not directed:
                for (w,s) in self._table[score]:
                    if w == word:
                        self._table[score].remove( (w,s) )
                        break


    def areNeighbours( self, word, score ):
        if word in self._table.keys():
           for (w,s) in self._table[word]:
               if s == score:
                   return True
        return False


    def findDFSPath( self, word, score, visited=[] ):
        if self.areNeighbours(word, score):  #Base Case
            return [ word, score ]

        if word in self._table():
            neighbours = self._table[word]
        for (w,s) in neighbours: #Recursive Case
            if n not in visited:
                p = self.findDFSPath( n, score, visited + [word] )
                if p !=None:
                    return [word] + p #path found

        return None

    def getNumberOfWords(self):
        return 25000

    def getNumberOfPositiveWords(self):
        return 12500

    def getNumberOfNegativeWords(self):  
        return 12500

    def getTotalWordCount(self):
        return 50000

    def addWordScore(self, word, score):
         if not word in self._table.keys():
             self.addVertex(word)
         self._table[word].add(score)
         if not score in self._table.keys():
            self.addVertex(score)
         self._table[score].add(word)
       
    def addStringScore(self, string, score):
        words = string.split(" ")
        for word in words:
            if len(word) > 3: # ignore short words
                self.addWordScore(word, score)

    def getWordSentiment(self, word): 
        return 125000

        
    def getWordCount(self, word):
        return 50000

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



