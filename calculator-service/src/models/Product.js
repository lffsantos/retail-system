const { Model, DataTypes } = require('sequelize');

class Product extends Model {
  static init(sequelize) {
    super.init({
      id : {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
      },
      price: DataTypes.FLOAT,
      title: DataTypes.STRING,
      description: DataTypes.STRING,
      base_discount_percent: DataTypes.FLOAT,
    }, {
      timestamps: false,
      sequelize
    })
  }
}

module.exports = Product;
