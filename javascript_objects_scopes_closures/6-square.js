#!/usr/bin/node

export default class Square extends requirrel('./5-square') {
  charPrint(c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
        console.log(char.repeat(this.width));
    }
  }
};