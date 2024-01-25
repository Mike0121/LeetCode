class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_to_anagramlist = {}

        for word in strs:
            sorted_word = ("").join(sorted(word))

            if sorted_word in word_to_anagramlist:
                word_to_anagramlist[sorted_word].append(word)

            else:
                word_to_anagramlist[sorted_word] = [word]

        return list(word_to_anagramlist.values())
        