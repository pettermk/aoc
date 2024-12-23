use std::collections::HashMap;
use std::fs;
use std::thread;
use std::time::Duration;

#[derive(Debug)]
struct Robot {
    x: usize,
    y: usize,
}

#[derive(Debug)]
struct Box {
    x: usize,
    y: usize,
}

#[derive(Debug)]
struct Motion {
    x: i32,
    y: i32,
}

#[derive(Debug)]
struct Wall {
    x: usize,
    y: usize,
}

impl Robot {
    fn move_it(&mut self, movement: &Motion, boxes: &mut Vec<Box>, walls: &Vec<Wall>) {
        let new_position = (
            (self.x as i32 + movement.x) as usize,
            (self.y as i32 + movement.y) as usize,
        );
        println!("Robot tries {:?}", new_position);
        if walls
            .iter()
            .any(|w| w.x == new_position.0 && w.y == new_position.1)
        {
            return;
        }
        if let Some(index_) = boxes
            .iter()
            .position(|b| b.x == new_position.0 && b.y == new_position.1)
        {
            if Box::move_it(index_, movement, boxes, &walls) {
                self.x = new_position.0;
                self.y = new_position.1;
            }
        } else {
            self.x = new_position.0;
            self.y = new_position.1;
        }
    }
}

impl Box {
    fn move_it(index_: usize, movement: &Motion, boxes: &mut Vec<Box>, walls: &Vec<Wall>) -> bool {
        let me = &boxes[index_];
        let new_position = (
            (me.x as i32 + movement.x) as usize,
            (me.y as i32 + movement.y) as usize,
        );
        if walls
            .iter()
            .any(|w| w.x == new_position.0 && w.y == new_position.1)
        {
            return false;
        }
        if let Some(i) = boxes
            .iter()
            .position(|b| b.x == new_position.0 && b.y == new_position.1)
        {
            if Box::move_it(i, movement, boxes, &walls) {
                let m_me = &mut boxes[index_];
                m_me.x = new_position.0;
                m_me.y = new_position.1;
                return true;
            } else {
                return false;
            }
        } else {
            let m_me = &mut boxes[index_];
            m_me.x = new_position.0;
            m_me.y = new_position.1;
        }
        true
    }
}

fn generate_input(input_map: &String) -> (Robot, Vec<Box>, Vec<Wall>) {
    let array: Vec<String> = input_map.split("\n").map(|s| s.to_string()).collect();
    let mut boxes = Vec::<Box>::new();
    let mut walls = Vec::<Wall>::new();
    let mut robot = Robot { x: 0, y: 0 };
    for (i, line) in array.iter().enumerate() {
        for (j, character) in line.chars().enumerate() {
            match character {
                '#' => walls.push(Wall { x: j * 2, y: i }),
                'O' => boxes.push(Box { x: j * 2, y: i }),
                '@' => (robot.x, robot.y) = (j * 2, i),
                _ => (),
            }
        }
    }
    (robot, boxes, walls)
}

fn simulate(input: &String, robot: &mut Robot, boxes: &mut Vec<Box>, walls: &Vec<Wall>) {
    let movement_map: HashMap<char, Motion> = [
        ('>', Motion { x: 1, y: 0 }),
        ('^', Motion { x: 0, y: -1 }),
        ('<', Motion { x: -1, y: 0 }),
        ('v', Motion { x: 0, y: 1 }),
        ('\n', Motion { x: 0, y: 0 }),
    ]
    .into();
    input.chars().for_each(|c| {
        robot.move_it(&movement_map[&c], boxes, walls);
        print_state(robot, boxes, walls);
    });
    let sum: usize = boxes.into_iter().map(|b| b.y * 100 + b.x).sum();
    println!("{:?}", sum);
}

fn print_state(robot: &Robot, boxes: &Vec<Box>, walls: &Vec<Wall>) {
    let mut grid: Vec<Vec<char>> = vec![vec![' '; 100]; 100];
    grid[robot.y][robot.x] = '@';
    boxes.iter().for_each(|b| grid[b.y][b.x] = 'O');
    walls.iter().for_each(|w| grid[w.y][w.x] = '#');
    for row in grid.iter() {
        let row_str: String = row.iter().collect(); // Convert the row (Vec<char>) to a String
        println!("{}", row_str); // Print the row
    }
    // thread::sleep(Duration::from_millis(150));
}

fn main() {
    let inputs: Vec<String> = fs::read_to_string("input.txt")
        .unwrap()
        .split_terminator("\n\n")
        .map(|s| s.to_string())
        .collect();
    println!("{}", inputs[0]);
    let (mut robot, mut boxes, walls) = generate_input(&inputs[0]);
    simulate(&inputs[1], &mut robot, &mut boxes, &walls);
}
