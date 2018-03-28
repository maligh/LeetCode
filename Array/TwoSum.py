# /**
#  * Question Link: https://leetcode.com/problems/two-sum/
#  * Primary idea: dict中key是nums的value，value是nums的index，所以遍历数组找到dict有值时即可得到两个下标
#  *
#  * Time Complexity: O(n), Space Complexity: O(n)
#  */

#!/usr/local/bin/python3

class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for index,value in enumerate(nums):
            if (target - value in dict) :
                return [dict[target - value], index]
            dict[value] = index