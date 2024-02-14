#!/usr/bin/node
let = require('./101-data').dict;

let totalist = Object.entries(dict);
let vals = Object.values(dict);
let valsUniq = [...new Set(vals)];
let newDict = {};
for (let j in valsUniq) {
  let list = [];
  for (let k in totalist) {
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
