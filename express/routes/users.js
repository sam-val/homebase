var express = require('express');
var router = express.Router();
const { Sequelize, Model, DataTypes } = require('sequelize');

// Create Sequelize instance
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: './database.sqlite'
});

// Define User model
class User extends Model {}
User.init({
  name: DataTypes.STRING,
  email: DataTypes.STRING,
  password: DataTypes.STRING
}, { sequelize, modelName: 'user' });

// Sync models with database
sequelize.sync();


// CRUD routes for User model
router.get('', async (req, res) => {
  const users = await User.findAll();
  res.json(users);
});

router.get('/:id', async (req, res) => {
  const user = await User.findByPk(req.params.id);
  res.json(user);
});

router.post('', async (req, res) => {
  const user = await User.create(req.body);
  res.json(user);
});

router.put('/:id', async (req, res) => {
  const user = await User.findByPk(req.params.id);
  if (user) {
    await user.update(req.body);
    res.json(user);
  } else {
    res.status(404).json({ message: 'User not found' });
  }
});

router.delete('/:id', async (req, res) => {
  const user = await User.findByPk(req.params.id);
  if (user) {
    await user.destroy();
    res.json({ message: 'User deleted' });
  } else {
    res.status(404).json({ message: 'User not found' });
  }
});

module.exports = router;