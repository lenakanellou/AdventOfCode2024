use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    // Get command-line arguments
    let args: Vec<String> = env::args().collect();


    let mut dlist: Vec<i32> = Vec::new();
    let mut slist: Vec<i32> = Vec::new();

    // Check if a filename was provided
    if args.len() < 2 {
        eprintln!("Usage: {} <filename>", args[0]);
        return Ok(()); // Gracefully exit
    }

    let file_path = &args[1]; // The first argument after the program name is the filename


    // Call the function to read the file
    /* if let Err(e) = read_lines(file_path) {
        eprintln!("Error reading file: {}", e);
    } */

    
    let (mut llist, mut rlist) = read_lines(file_path)?;
    llist.sort();
    println!("{:?}", llist);
    rlist.sort();
    println!("{:?}", rlist);

    for (l, r) in llist.iter().zip(rlist.iter()) {
        dlist.push((l - r).abs())
    }
    println!("{:?}", dlist);
    let dist_sum: i32 = dlist.iter().sum();
    println!("The sum of the distance vector is: {}", dist_sum);

    for (index, l) in llist.iter().enumerate() {
        slist.push(0);

        for r in &rlist {
            if l == r {
                slist[index] += 1;
            }
        }

        slist[index] *= l
        
    }
    println!("The similarity vector is: {:?}, the similarity score is {}.", slist, slist.iter().sum::<i32>());

    Ok(())

}

fn read_lines<P>(filename: P) -> Result<(Vec<i32>, Vec<i32>), io::Error>
where
    P: AsRef<Path>,
{
    let mut llist: Vec<i32> = Vec::new();
    let mut rlist: Vec<i32> = Vec::new();
    let mut nums: Vec<i32> = Vec::new();

    // Open the file
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    // Iterate over the lines
    for (index, line) in reader.lines().enumerate() {
        let line = line?; // Unwrap the Result to get the line content
        nums = line.split_whitespace().map(|s| s.parse::<i32>().unwrap()) // parse each part as i32
        .collect();

        println!("Line {}: {} and {}", index + 1, nums[0], nums[1]);
        llist.push(nums[0]);
        rlist.push(nums[1]);
    }

    Ok((llist, rlist))
}
