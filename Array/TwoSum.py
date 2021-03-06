# /**
#  * Question Link: https://leetcode.com/problems/two-sum/
#  * Primary idea: dict中key是nums的value，value是nums的index，所以遍历数组找到差值在dict的key中时即可
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