#!/usr/bin/node

module.exports = class Square extends requirel('./5-square') {
  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
