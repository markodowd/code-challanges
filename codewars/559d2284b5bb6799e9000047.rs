fn add_length(s: &str) -> Vec<String> {
    let mut result = vec![];

    for word in s.split_whitespace() {
        let length = word.len();

        let combined = format!("{} {}", word, length);

        result.push(combined);
    }

    result
}
