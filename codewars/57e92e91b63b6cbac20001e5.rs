fn duty_free(price: i32, discount: i32, holiday_cost: i32) -> i32 {
    let discount_rate = discount as f64 / 100.0;
    let discounted_price = price as f64 * discount_rate;
    
    let result = holiday_cost as f64 / discounted_price;
    
    result as i32 
}
