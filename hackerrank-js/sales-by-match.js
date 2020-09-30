const assert = require("assert");

// From https://www.hackerrank.com/challenges/sock-merchant/

function sockMerchant(n, ar) {
  let sockCounts = {};
  for (let i = 0; i < n; i++) {
    sockCounts[ar[i]] === undefined
      ? (sockCounts[ar[i]] = 1)
      : (sockCounts[ar[i]] += 1);
  }

  return Object.values(sockCounts).reduce(
    (count, curr) => count + Math.floor(curr / 2),
    0
  );
}

assert.strictEqual(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]), 3);
assert.strictEqual(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]), 4);
