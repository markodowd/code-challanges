fn power_of_two(x: u64) -> bool {
    if x == 0 {
        return false;
    }

    let mut num = x;

    while num % 2 == 0 {
        num /= 2;
    }

    num == 1
}
