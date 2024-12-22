use itertools::join;
use std::fs;
use std::thread;
use std::time::Duration;

#[derive(Debug)]
struct Speed {
    x: i32,
    y: i32,
}

#[derive(Debug)]
struct Position {
    x: usize,
    y: usize,
}

#[derive(Debug)]
struct Robot {
    position: Position,
    speed: Speed,
}

#[derive(Debug)]
struct Boundaries {
    x: usize,
    y: usize,
}

impl Robot {
    fn move_it(&mut self, boundaries: &Boundaries) {
        self.position.x = ((self.position.x as i32 + self.speed.x + boundaries.x as i32)
            % boundaries.x as i32) as usize;
        self.position.y = ((self.position.y as i32 + self.speed.y + boundaries.y as i32)
            % boundaries.y as i32) as usize;
    }
}

fn parse_robot(robot: &str) -> Robot {
    let positions: Vec<Vec<i32>> = robot
        .split(" ")
        .map(|p| {
            p.split("=")
                .last()
                .unwrap()
                .to_string()
                .split(",")
                .map(|s| s.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    Robot {
        position: Position {
            x: positions[0][0] as usize,
            y: positions[0][1] as usize,
        },
        speed: Speed {
            x: positions[1][0],
            y: positions[1][1],
        },
    }
}

fn get_grid(robots: &Vec<Robot>, boundaries: &Boundaries) -> Vec<Vec<usize>> {
    let mut grid: Vec<Vec<usize>> = vec![vec![0; boundaries.x]; boundaries.y];
    for robot in robots.iter() {
        grid[robot.position.y][robot.position.x] += 1;
    }
    grid
}

fn print_robots(robots: &Vec<Robot>, boundaries: &Boundaries) {
    let grid = get_grid(robots, &boundaries);
    let mut hit = false;
    for row in grid.iter() {
        let line = join(
            row.iter().map(|i| match i {
                0 => " ",
                _ => "x",
            }),
            "",
        );
        if line.contains("xxxxxxxxx") {
            hit = true;
        }
    }
    if hit {
        for row in grid.iter() {
            let line = join(
                row.iter().map(|i| match i {
                    0 => " ",
                    _ => "x",
                }),
                "",
            );
            println!("{}", line);
        }
        thread::sleep(Duration::from_millis(10000));
    }
}

fn move_robots(robots: &mut Vec<Robot>, boundaries: &Boundaries, iterations: usize) {
    for i in 0..iterations {
        for robot in robots.iter_mut() {
            robot.move_it(boundaries);
        }
        print_robots(robots, &boundaries);
        println!("{}", i);
    }
}

fn quadrant_sum(robots: &Vec<Robot>, boundaries: &Boundaries, quadrant: i32) -> usize {
    let grid = get_grid(robots, &boundaries);
    let cols = grid[0].len();
    let rows = grid.len();
    let mid_row = rows / 2;
    let mid_col = cols / 2;

    match quadrant {
        1 => grid[0..mid_row]
            .iter()
            .flat_map(|row| &row[0..mid_col])
            .sum(),
        2 => grid[0..mid_row]
            .iter()
            .flat_map(|row| &row[mid_col + 1..cols])
            .sum(),
        3 => grid[mid_row + 1..rows]
            .iter()
            .flat_map(|row| &row[0..mid_col])
            .sum(),
        4 => grid[mid_row + 1..rows]
            .iter()
            .flat_map(|row| &row[mid_col + 1..cols])
            .sum(),
        _ => 0,
    }
}

fn main() {
    println!("");
    let mut robots: Vec<Robot> = fs::read_to_string("input.txt")
        .unwrap()
        .split_terminator("\n")
        .map(parse_robot)
        .collect();
    let boundaries: Boundaries = Boundaries { x: 101, y: 103 };
    move_robots(&mut robots, &boundaries, 50000);
    for i in 1..5 {
        println!("Quadrant {}: {}", i, quadrant_sum(&robots, &boundaries, i));
    }
    let result: i32 = (1..5)
        .map(|i| quadrant_sum(&robots, &boundaries, i) as i32)
        .product();
    println!("{result}");
}
