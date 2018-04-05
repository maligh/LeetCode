# /**
#  * Question Link: https://leetcode.com/problems/reverse-integer/
#  * Primary idea: 字符串翻转
#  * Time Complexity: O(n), Space Complexity: O(1)
#  */
 
#!/usr/local/bin/python3

class Solution:
    def reverse(self, x):
	    res =  int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
	    return res if res < 2147483648 and res >= -2147483648 else 0