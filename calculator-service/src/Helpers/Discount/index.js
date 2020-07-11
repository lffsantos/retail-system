const rules = require('../../config/discountrules');

class Discount {
    constructor(product, user) {
        this.product = product;
        this.user = user;
    }
    getDiscount(){
        let amountDiscount = (this.percentualDiscount()*this.product.price)/100
        return {
            'total_discount': this.percentualDiscount(),
            'final_price': this.product.price - amountDiscount
          }
    }

    percentualDiscount(){
        let amount = this.productDiscount() 

        if (amount > rules.maxDiscount){
            return rules.maxDiscount
        }
        
        return amount
    }

    productDiscount(){
        let discount = this.product.base_discount_percent

        let date = new Date()
        let actualDate = date.getDate()+'-'+parseInt(date.getMonth()+1)
        if(Object.keys(rules.date).includes(actualDate)) {
            discount += rules.date[actualDate]
        }
        
        date = new Date(this.user.birthdate)
        
        let birthDate = +parseInt(date.getDate())+'-'+parseInt(date.getMonth()+1)
        if (actualDate === birthDate){
            discount += rules.birthday
        }

        return discount
    }

}

module.exports = Discount
