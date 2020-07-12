const User = require('../models/User');
const Product = require('../models/Product');
const Discount = require('../Helpers/Discount');
const { ErrorHandler } = require('../Helpers/error')

module.exports = {
  async index(req, res, next) {
    try {
      const { productId } = req.params;
      const product = await Product.findByPk(productId)
      if (!product) {
        throw new ErrorHandler(404, 'Product Not Found')  
      }
      const { userId } = req.query
      let user;
      if (userId != "" && userId !== undefined){
        user = await User.findByPk(userId)
        if (!user) {
          throw new ErrorHandler(404, 'User Not Found')  
        }
      }
      const discount = new Discount(product, user)
      return res.json(discount.getDiscount());
    } catch (error) {
        return res.status(error.statusCode).json({status: 'error',message: error})
    }
  }  
};

