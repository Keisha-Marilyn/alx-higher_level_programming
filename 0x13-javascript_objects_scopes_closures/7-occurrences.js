#!/usr/bin/node

const nbOccurrences = (list, searchElement) => list.filter((element) => searchElement === element).length;

module.exports = { nbOccurrences };
