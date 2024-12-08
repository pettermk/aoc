import { sleep } from "https://deno.land/x/sleep/mod.ts"

// const file = Deno.readTextFileSync("test_input.txt");
const file = Deno.readTextFileSync("input.txt");

const rawInput = file.split("\n");
rawInput.pop();
const width = rawInput[0].length;
const height = rawInput.length;

class Position extends Array<number> {
  constructor(...elements) {
    super(...elements);
    Object.freeze(this);
  }
  equals(other) {
    return this[0] == other[0] && this[1] == other[1];
  }
}

// type Direction = [number, number];

const getPosition = (position: Position, input: Array<string>) => {
  if (!isWithinBounds(position, input)) {
    return "|";
  }
  return input[position[1]][position[0]];
}

const move = (position: Position, direction: Direction) => {
  return new Position(position[0] + direction[0], position[1] + direction[1])
}

const isWithinBounds = (pos: Position, input: Array<str>) => {
  if (pos[0] < width && pos[0] >= 0 && pos[1] < height && pos[1] >= 0) {
    return true;
  }
  return false;
}

// Find starting point
const startingY = rawInput.findIndex(line => line.indexOf("^") != -1);
const startingX = rawInput[startingY].indexOf("^");

let position: Position = new Position(startingX, startingY);
let direction: Direction = new Position(0, -1);

const rotateDirection: Direction = (direction: Direction, degrees: number) => {
  return [
    Math.round(Math.cos(degrees) * direction[0] + Math.sin(degrees) * direction[1]),
    Math.round(-Math.sin(degrees) * direction[0] + Math.cos(degrees) * direction[1]),
  ]
}

const simulate = (input: Array<string>) => {
  let position: Position = new Position(startingX, startingY);
  let direction: Direction = new Position(0, -1);
  let visited: Array<Position> = new Array<Position>() ;
  let loop = false;
  visited.push(position);
  const turns: Array<Pair<Position, Direction>> = [];
  while(isWithinBounds(position, input)) {
    let obstacle = false;
    let newPosition = position;
    while (!obstacle) {
      const newPositionCandidate = move(newPosition, direction);
      const symbolAtPosition = getPosition(newPositionCandidate, input);
      if (["#"].includes(symbolAtPosition)) {
        obstacle = true;
      }
      else if (symbolAtPosition == "|") {
        obstacle = true;
        newPosition = newPositionCandidate;
      }
      else {
        newPosition = newPositionCandidate;
        if (!visited.some(x => x.equals(newPosition))) {
          visited.push(newPosition);
        }
      }
      let visitedMap = input.map((line) => line.split(""));

      for (const p of visited) {
        visitedMap[p[1]][p[0]] = "X";
      }
    }
    direction = rotateDirection(direction, -Math.PI / 2);
    position = newPosition;
    if (turns.some(x => x[0].equals(position) && x[1][0] == direction[0] && x[1][1] == direction[1])) {
      loop = true;
      break;
    }
    else {
      turns.push([position, direction]);
    }
  }
  console.log(visited.length);
  return loop;
}

// simulate(rawInput);

const range = (n: number): number[] => Array.from({ length: n }, (_, i) => i);

console.log(rawInput);
let modifiedInput = rawInput.map((line) => line.split(""));
let sum = 0;
for (const i of range(width)) {
  for (const j of range(height)) {
    console.log(`Processing ${j} rows`);
    if (i == startingX && j == startingY) {
      continue;
    }
    let modifiedInputCopy = modifiedInput.map(x => x.map(y => `${y}`));
    modifiedInputCopy[i][j] = '#';
    if (simulate(modifiedInputCopy.map(x => x.join("")))) {
      console.log("loop");
      sum = sum + 1;
    }
  }
  console.log(`Processing ${i} row`);
}

// let modifiedInputCopy = modifiedInput.map(x => x.map(y => `${y}`));
// modifiedInputCopy[height - 1][width - 3] = '#';
// if (simulate(modifiedInputCopy.map(x => x.join("")))) {
//   console.log("loop");
// }

console.log(sum);
