"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/
1832. Check if the Sentence Is Pangram
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
