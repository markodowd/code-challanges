fn hex_to_dec(hex_string: &str) -> u32 {
    u32::from_str_radix(hex_string, 16).unwrap()
}
