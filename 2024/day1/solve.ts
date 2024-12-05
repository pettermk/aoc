// const file = Deno.readTextFileSync("test_input.txt");
const file = Deno.readTextFileSync("input.txt");

const left: number[] = [];
const right: number[] = [];

for (const line of file.split("\n")) {
  const splitted = line.split("   ");
  left.push(parseInt(splitted[0]));
  right.push(parseInt(splitted[1]));
}

left.pop();
right.pop();

const sortedLeft = left.sort()
const sortedRight = right.sort()

let sum: number = 0;
for (const i in sortedLeft) {
  console.log(sortedLeft[i]);
  sum = sum + Math.abs(sortedLeft[i] - sortedRight[i]);
}

let similarity: number = 0;
const s2 = sortedLeft.reduce(
  (acc: number, current: number) => acc + (sortedRight.filter(j => j == current).length * current), 0
)
for (const i in sortedLeft) {
  similarity += (sortedRight.filter(j => j == sortedLeft[i]).length) * sortedLeft[i];
}

console.log(left);

console.log(sum);
console.log(similarity);
console.log(s2);

