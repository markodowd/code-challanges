fn get_count(string: &str) -> usize {
    let mut vowels_count: usize = 0;

    for letter in string.chars() {
        if "aeiuo".contains(letter) {
            vowels_count += 1
        }
    }

    vowels_count
}
