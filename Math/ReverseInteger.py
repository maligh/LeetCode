# /**
#  * Question Link: https://leetcode.com/problems/reverse-integer/
#  * Primary idea: 字符串翻转
#  * Time Complexity: O(n), Space Complexity: O(1)
#  */
 
#!/usr/local/bin/python3

class Solution:
    def isPalindrome(self, x):
        if x < 0 :
            return False
        return str(x) == str(x)[::-1]