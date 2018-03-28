/**
 * Question Link: https://leetcode.com/problems/two-sum/
 * Primary idea: dict中key是nums的value，value是nums的index，所以遍历数组找到dict有值时即可得到两个下标
 *
 * Time Complexity: O(n), Space Complexity: O(n)
 */

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int : Int]()
        for (index, value) in nums.enumerated() {
            if let firstIndex = dict[target - value] {
                return [firstIndex, index]
            }
            dict[value] = index
        }
        fatalError("No valid result")
    }
}
