#!/usr/bin/node
const dict = require('./101-data').dict;

const totalDict = {};

for (const key in dict) {
  const occ = dict[key];
  if (!totalDict[occ]) {
    totalDict[occ] = [];
  }
  totalDict[occ].push(key);
}

console.log(totalDict);
