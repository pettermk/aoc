// const file = Deno.readTextFileSync("test_input.txt");
const file = Deno.readTextFileSync("input.txt");

class Vector2D {
	public static add(vector1: Vector2D, vector2: Vector2D): Vector2D {
		return new Vector2D(vector1.x + vector2.x, vector1.y + vector2.y);
	}

	constructor(
		public x: number = 0, 
		public y: number = 0,
	) { }
}

const input = file.split("\n");
input.pop();

const width = input[0].length;
const height = input.length;

const isWithinBounds = (vec: Vector2D, width: number, height: number) => {
  return vec.x >= 0 && vec.x < width && vec.y >= 0 && vec.y < height;
}

const searchDirections: Array<Vector2D> = [
  new Vector2D(0, 1),
  new Vector2D(1, 1),
  new Vector2D(1, 0),
  new Vector2D(-1, 1),
  new Vector2D(-1, 0),
  new Vector2D(-1, -1),
  new Vector2D(0, -1),
  new Vector2D(1, -1)
];

const searchStrings: Array<string> = [];

const points: Array<Vector2D> = []
for (let i = 0; i < width; i++) {
  for (let j = 0; j < height; j++) {
    points.push(new Vector2D(i, j));
  }
}

let count: number = 0;
for (const p of points) {
  for (const direction of searchDirections) {
    let newWord: string = "";
    let position = p;
    while (isWithinBounds(position, width, height)) {
      newWord = newWord + input[position.y][position.x];
      position = Vector2D.add(position, direction);
      if (newWord == "XMAS") {
        count++;
        break;
      }
    }
  }
}

console.log(count);

count = 0;
const moves = [
  ['M', new Vector2D(-1, -1)],
  ['S', new Vector2D(1, -1)],
  ['A', new Vector2D(0, 0)],
  ['M', new Vector2D(-1, 1)],
  ['S', new Vector2D(1, 1)],
]
for (const p of points) {
  let partialCount = 0;
  if (p.x == 0 || p.x == (width - 1) || p.y == 0 || p.y == (height - 1)) {
    continue;
  }
  const word1 = input[p.y -1][p.x + 1] + input[p.y][p.x] + input[p.y + 1][p.x - 1];
  const word2 = input[p.y -1][p.x - 1] + input[p.y][p.x] + input[p.y + 1][p.x + 1];

  if ((word1 == 'SAM' || word1 == 'MAS') && (word2 == 'SAM' || word2 == 'MAS')){
    count++;
  }
  
}
console.log(count);
