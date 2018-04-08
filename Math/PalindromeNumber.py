# /**
#  * Question Link: https://leetcode.com/problems/palindrome-number/description/
#  * Primary idea: 排除负数，字符串反转 对比是否相等
#  * Time Complexity: O(1), Space Complexity: O(1)
#  */

#!/usr/local/bin/python3

def isPalindrome(x):
	if x < 0 :
		return False
	return str(x) == str(x)[::-1]

print(isPalindrome(124321))