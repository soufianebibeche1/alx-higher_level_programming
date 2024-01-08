#!/usr/bin/node
const args = process.argv.slice(2);
function add (a, b) {
  return (a + b);
}
const nb1 = Number(args[0]);
const nb2 = Number(args[1]);
console.log(add(nb1, nb2));
