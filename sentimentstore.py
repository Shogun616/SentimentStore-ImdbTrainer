class SentimentStore:
    def __init__(self):
        # TODO: decide which data structure you need to track
        #       the sentiment of each word
        # TODO: decide which data structure you need to track
        #       the number of times each word has been seen
        pass
    
    def getNumberOfWords(self):
        # TODO:
        return 0

    def getNumberOfPositiveWords(self):
        # TODO:  return the number of unique words with positive scores
        return 0

    def getNumberOfNegativeWords(self):
        # TODO:  return the number of unique words with negative scores
        return 0

    def getTotalWordCount(self):
        # TODO:  return the total number of unique words in the store
        return 0

    def addWordScore(self, word, score):
        # TODO: add a word with a score
        #        - add score to our running total score for that word
        #        - add 1 to our count for number of times this word has been seen
        pass

    def addStringScore(self, string, score):
        words = string.split(" ")
        for word in words:
            if len(word) > 3: # ignore short words
                self.addWordScore(word, score)

    def getWordSentiment(self, word):
        # TODO: return sentiment score for a given word,
        # TODO: return 0 if word not in store
        return 0

    def getWordCount(self, word):
        # TODO: return how many times we have seen a word
        # TODO: return 0 if word not in store
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



