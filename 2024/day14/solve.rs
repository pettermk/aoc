use std::env;
use std::fs;

fn main() {
    println!("");
    let contents = fs::read_to_string("test_input.txt")
        .expect("Should be ok");
    println!(contents);
}
    
