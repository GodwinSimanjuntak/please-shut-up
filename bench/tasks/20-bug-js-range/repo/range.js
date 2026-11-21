/**
 * Inclusive integer range: range(1, 3) -> [1, 2, 3].
 * Step can be negative: range(3, 1, -1) -> [3, 2, 1].
 */
function range(start, end, step = 1) {
  const out = [];
  if (step > 0) {
    for (let i = start; i < end; i += step) out.push(i);
  } else {
    for (let i = start; i > end; i += step) out.push(i);
  }
  return out;
}

module.exports = { range };
