const express = require('express');

const CalculatorController = require('./controllers/CalculatorController');

const routes = express.Router();

routes.get('/discounts/:productId/', CalculatorController.index);

module.exports = routes;