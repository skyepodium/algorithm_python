from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # 1. init
        c = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        l = []

        for word in words:
            code = ""
            for w in word:
                code += c[ord(w) - 97]

            if code not in l:
                l.append(code)

        return len(l)

