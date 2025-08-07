fn cockroach_speed(s: f64) -> i64 {
    const CENTIMETERS_IN_METER: f64 = 100.0;
    const METERS_IN_KILOMETER: f64 = 1000.0;

    const CENTIMETERS_IN_KILOMETER: f64 = CENTIMETERS_IN_METER * METERS_IN_KILOMETER;

    const SECONDS_IN_MINUTE: f64 = 60.0;
    const MINUTE_IN_HOUR: f64 = 60.0;

    const SECONDS_IN_HOUR: f64 = SECONDS_IN_MINUTE * MINUTE_IN_HOUR;

    let answer = s * (CENTIMETERS_IN_KILOMETER / SECONDS_IN_HOUR);

    answer.floor() as i64
}
