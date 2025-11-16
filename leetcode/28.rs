// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if let Some(index) = haystack.find(&needle) {
            return index as i32
        }

        -1
    }
}
