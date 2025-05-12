'''

Given a string, return the first character that does not repeat (i.e., appears only once).
If all characters repeat, return "_".

Input:  "leetcode"
Output: "l"
Explanation:

'l' appears once ✅

'e' appears 3 times ❌

't', 'c', 'o', 'd' also appear once

But 'l' is the first non-repeating
--------------------------------------
Input:  "aabbccdde"
Output: "e"
Explanation:
'e' is the only character that appears once all others repeat
'''
class FirstNonRepeatingCharacter:
    def get_first_non_repeated(self,input):

