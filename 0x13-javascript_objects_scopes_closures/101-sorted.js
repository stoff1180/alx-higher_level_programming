#!/usr/bin/node
const dict = require('./101-data').dict;

const totaList = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const i in totaList) {
    if (totaList[i][1] === valsUniq[j]) {
      list.unshift(totaList[i][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
