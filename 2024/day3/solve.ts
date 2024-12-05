// const file = Deno.readTextFileSync("test_input.txt");
const file = Deno.readTextFileSync("input.txt");

const re = /mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)/g

const matches = file.match(re);

let sum = 0;

let enable = true;
for (const match of matches) {
  if (match == "do()") {
    enable = true;
    continue;
  }
  if (match == "don't()") {
    enable = false;
    continue
  }
  const left = match.split(",")[0].split("(")[1];
  const right = match.split(",")[1].split(")")[0];
  // console.log(left);
  // console.log(right);
  // console.log(match);
  if (enable) {
    sum += parseInt(left) * parseInt(right);
  }
}
console.log(sum);
// while ((match = re.exec(file)) !== null) {
//   console.log(match);
// }



