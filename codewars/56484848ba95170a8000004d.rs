fn gps(s: i32, x: Vec<f64>) -> i32 {
    // if x length is less than or equal to 1 return 0 since the car didn't move
    if x.len() <= 1 {
        return 0;
    }

    let mut max_avg_speed = 0.0;

    for pair in x.windows(2) {
        let delta_distance = pair[1] - pair[0];
        // (3600 * delta_distance) / s
        let speed = 3600.0 * delta_distance / s as f64;

        if speed > max_avg_speed {
            max_avg_speed = speed;
        }
    }

    max_avg_speed.floor() as i32
}
