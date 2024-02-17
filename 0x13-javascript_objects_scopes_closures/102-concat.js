#!/usr/bin/node
const fs = require('fs');

const fstFile = fs.readFileSync(process.argv[2]).toString();
const secFile = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fstFile + secFile);
