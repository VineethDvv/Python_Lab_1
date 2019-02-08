def longestSubstring(self, word):
    longest =0
    currentLength = 0

    if(len(word) > 0):
        currentLength = 1
        longest = 1
        dict = {word[0] : 0}
        i = 1

        while i < len(word):
            if (dict.has_key(word[i])):
                i = dict[word[i]]+1
                dict.clear()
                if (longest < currentLength):
                    longest= currentLength
                currentLength = 0
            else:
                dict[word[i]] = i
                currentLength = currentLength + 1
                i = i + 1

        if (longest < currentLength):
            longest= currentLength

    return longest