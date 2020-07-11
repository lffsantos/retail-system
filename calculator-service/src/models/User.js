const { Model, DataTypes } = require('sequelize');

class User extends Model {
  static init(sequelize) {
    super.init({
      id : {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
      },
      first_name: DataTypes.STRING,
      last_name: DataTypes.STRING,
      birth_date: DataTypes.DATEONLY,
    }, {
      timestamps: false,
      sequelize
    })
  }
}

module.exports = User;