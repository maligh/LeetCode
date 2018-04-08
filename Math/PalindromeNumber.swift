/**
 * Question Link: https://leetcode.com/problems/palindrome-number/description/
 * Primary idea: 排除负数，字符串反转 对比是否相等
 * Time Complexity: O(1), Space Complexity: O(1)
 */

 class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        guard x >= 0 else {
            return false
        }
        let string = String(x)
        let reverseString = String(string.reversed())
        return (string == reverseString)
    }
}