// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        let mut answer = vec![];

        let kelvin = celsius + 273.15;
        let fahrenheit = celsius * 1.80 + 32.00;

        answer.push(kelvin);
        answer.push(fahrenheit);

        answer
    }
}
