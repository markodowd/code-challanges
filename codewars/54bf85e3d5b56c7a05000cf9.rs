fn number(lines: &[&str]) -> Vec<String> {
    let mut answer = vec![];

    for (index, item) in lines.iter().enumerate() {
        let formatted = format!("{}: {item}", { index + 1 });
        answer.push(formatted);
    }

    answer
}
