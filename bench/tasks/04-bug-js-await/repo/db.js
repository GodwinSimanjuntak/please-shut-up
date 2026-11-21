const USERS = { 1: { id: 1, name: 'Ada' }, 2: { id: 2, name: 'Linus' } };

async function findUser(id) {
  await new Promise((r) => setTimeout(r, 5));
  return USERS[id];
}

module.exports = { findUser };
