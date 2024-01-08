#!/usr/bin/node
const args = process.argv.slice(2);
const nb = Number(args[0]);
function factorial (nb) {
  if (isNaN(nb) || (nb === 0)) {
    return 1;
  } else {
    return (nb * factorial(nb - 1));
  }
}
console.log(factorial(nb));
