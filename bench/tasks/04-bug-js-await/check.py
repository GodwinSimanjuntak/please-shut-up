from lib import node_hidden
TEST = '''
const assert = require('assert');
const { getUserName } = require('./users');
(async () => {
  assert.strictEqual(await getUserName(1), 'Ada');
  assert.strictEqual(await getUserName(2), 'Linus');
  console.log('ok');
})().catch((e) => { console.error(e); process.exit(1); });
'''
def check(work, orig, answer):
    return node_hidden(work, TEST)
