#!/usr/bin/node
let argCount = process.argv.length - 2;
if (argCount < 1) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
