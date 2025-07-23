impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut answer = vec![];
        let vec_len = nums.len() as i32;

        let start: i32 = 0;
        
        for i in start..vec_len - 1 {
            for j in i+1..vec_len {
                if nums[i as usize] + nums[j as usize] == target {
                    answer.push(i);
                    answer.push(j);
                }
            }
        }

        answer
    }
}
