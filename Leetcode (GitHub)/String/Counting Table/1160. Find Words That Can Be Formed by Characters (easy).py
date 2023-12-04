'''
@Project : Class
@File : 1160. Find Words That Can Be Formed by Characters (easy).py
@Author : Herbert
@Date : 12/2/2023 6:33 PM
'''


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = [0] * 26

        for letter in chars:
            count[ord(letter) - ord('a')] += 1

        res = 0

        for word in words:
            if self.help(word, count):
                res += len(word)
        return res

    def help(self, word, count):
        c = [0] * 26

        for char in word:
            x = ord(char) - ord('a')
            c[x] += 1
            if c[x] > count[x]:
                return False
        return True
