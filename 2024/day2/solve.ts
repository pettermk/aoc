// const file = Deno.readTextFileSync("test_input.txt");
const file = Deno.readTextFileSync("input.txt");

const lines = file.split("\n").map(
  (line: string) => line.split(" ").map(
    (char: string) => parseInt(char)
  )
).slice(0, -1)

function* pairwise<T>(iterable: Iterable<T>): Generator<[T, T], void> {
  const iterator = iterable[Symbol.iterator]();
  let a = iterator.next();
  if (a.done) return;
  let b = iterator.next();
  while (!b.done) {
    yield [a.value, b.value];
    a = b;
    b = iterator.next();
  }
}

const validCheck = (line: Array<number>) => {
  const diffs = [
    ...pairwise(line).map((pair: Array<number>) => pair[0] - pair [1])
  ]
  const signs = [
    ...pairwise(diffs.map((num: number) => Math.sign(num)))
    .map(
      (pair: Array<number>) => pair[0] - pair[1]
    )
  ]
  if (signs.some((num: number) => num != 0) || diffs.some(
    (num: number) => Math.abs(num) > 3 || num == 0
  )) {
    return false;
  }
  return true;
}

const validCheck2 = (line: Array<number>) => {
  if (validCheck(line)) {
    return true;
  }
  for (let i: number = 0; i < line.length; i++) {
    const testLine: Array<number> = line.toSpliced(i, 1);
    if (validCheck(testLine)) {
      return true;
    }
  }
  return false;
}

const validLines = lines.filter(
  (line: Array<number>) => validCheck2(line)
)

console.log(validLines.length);

