#!/usr/bin/node

exports.esrever = function (list) {
  const newarry = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newarry.push(list[i]);
  }
  return newarry;
};
