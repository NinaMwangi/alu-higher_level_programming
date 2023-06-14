#!/usr/bin/node
const Squared = requirel('./5-square');

module.exports = class Square extends Squared {
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
