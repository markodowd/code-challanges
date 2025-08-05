fn evaporator(mut content: f64, evap_per_day: i32, threshold: i32) -> i32 {
    let mut days = 0;
    
    let min_ml = content * (1.0 * threshold as f64 / 100.0);

    loop {
        content -= content * (1.0 * evap_per_day as f64 / 100.0);
        days += 1;
        
        if content < min_ml {
            break;
        }
    }
    
    days
}
