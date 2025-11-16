// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        if let Some(index) = nums.iter().position(|&num| num == target) {
            return index as i32
        }; 

        let mut answer = 0;

        for (index, item) in nums.iter().enumerate() {
            if item > &target {
                answer = index;
                break; 
            } else {
                answer = index + 1;               
            } 
        };

        answer as i32
    } 
}
