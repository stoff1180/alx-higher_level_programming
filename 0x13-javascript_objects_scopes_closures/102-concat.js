#!/usr/bin/node
const fs = require('fs');

let fsf = fs.readFileSync(process.argv[2]).toString();
let ssf = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fsf + ssf);
