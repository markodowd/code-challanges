impl Solution {
    pub fn or_array(nums: Vec<i32>) -> Vec<i32> {
        let mut answer = vec![];

        for index in 0..nums.len() - 1 {
            answer.push(nums[index] | nums[index + 1])
        }

        answer
    }
}
