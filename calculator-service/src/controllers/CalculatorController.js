const User = require('../models/User');
const Product = require('../models/Product');
const Discount = require('../Helpers/Discount');

module.exports = {
  async index(req, res) {
    const { productId } = req.params;
    const { userId } = req.query
    const users = await User.findByPk(userId)
    const product = await Product.findByPk(productId)
    const discount = new Discount(product, users)
    return res.json(discount.getDiscount());
  }  
};

