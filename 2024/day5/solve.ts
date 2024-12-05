// const file = Deno.readTextFileSync("test_input.txt");
const file = Deno.readTextFileSync("input.txt");

class Vector2D {
	public static add(vector1: Vector2D, vector2: Vector2D): Vector2D {
		return new Vector2D(vector1.x + vector2.x, vector1.y + vector2.y);
	}

	public multiply(length: number) {
	  return new Vector2D(this.x * length, this.y * length);
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

const cornerDirections: Array<Vector2D> = [
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

const topAndBottom: Array<Vector2D> = []
for (let i = 0; i < width; i++) {
  topAndBottom.push(new Vector2D(i, 0));
  topAndBottom.push(new Vector2D(i, height - 1));
}
const sides: Array<Vector2D> = [];
for (let i = 1; i < (height - 1); i++) {
  sides.push(new Vector2D(0, i));
  sides.push(new Vector2D(width - 1, i));
}

const points: Array<Vector2D> = []
for (let i = 0; i < width; i++) {
  for (let j = 0; j < height; j++) {
    points.push(new Vector2D(i, j));
  }
}

for (const p of points) {
  for (const direction of cornerDirections) {
    let newWord: string = "";
    let position = p;
    while (isWithinBounds(position, width, height)) {
      newWord = newWord + input[position.y][position.x];
      position = Vector2D.add(position, direction);
    }
    searchStrings.push(newWord);
  }
}

let count: number = 0;
for (const searchString of searchStrings) {
  if (searchString.startsWith("XMAS")) {
    count = count + 1;
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
  
  // if (
  // )
  // for (const move of moves) {
  //   const pos = Vector2D.add(p, move[1])
  //   if (isWithinBounds(pos, width, height)) {
  //     if (input[pos.y][pos.x] != move[0]) {
  //       break;
  //     }
  //   }
  //   else {
  //     break;
  //   }
  //   partialCount++;
  // }
  // if (partialCount == 5) {
  //   count++;
  // }
  // for (const direction of cornerDirections) {
  //   let newWord: string = "";
  //   let position = p;
  //   for (move of moves) {
  //
  //   }
  //
  //   while (isWithinBounds(position, width, height)) {
  //     newWord = newWord + input[position.y][position.x];
  //     position = Vector2D.add(position, direction);
  //   }
  //   console.log(newWord);
  //   searchStrings.push(newWord);
  // }
}
console.log(count);
