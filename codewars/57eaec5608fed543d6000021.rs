use either::Either;

fn div_con(arr: &[Either<i32, String>]) -> i32 {
    let mut left_sum = 0;
    let mut right_sum = 0;

    for item in arr {
        match item {
            Either::Left(num) => left_sum += num,
            Either::Right(s) => {
                if let Ok(num) = s.parse::<i32>() {
                    right_sum += num;
                }
            }
        }
    }

    left_sum - right_sum
}
