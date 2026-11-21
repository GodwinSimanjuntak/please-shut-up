from lib import node_hidden
TEST = '''
const assert = require('assert');
const { range } = require('./range');
assert.deepStrictEqual(range(1, 5), [1, 2, 3, 4, 5]);
assert.deepStrictEqual(range(3, 1, -1), [3, 2, 1]);
assert.deepStrictEqual(range(0, 6, 2), [0, 2, 4, 6]);
assert.deepStrictEqual(range(2, 2), [2]);
console.log('ok');
'''
def check(work, orig, answer):
    return node_hidden(work, TEST)
