impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if let Some(index) = haystack.find(&needle) {
            return index as i32
        }

        -1
    }
}
