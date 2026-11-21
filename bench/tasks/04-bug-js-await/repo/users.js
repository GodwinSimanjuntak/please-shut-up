const db = require('./db');

async function getUserName(id) {
  const user = db.findUser(id);
  return user.name;
}

module.exports = { getUserName };
