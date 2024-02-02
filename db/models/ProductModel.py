from bson import ObjectId
from configs.config import PRODUCT_DETAILS_COLLECTION
from db.Connections import Connection
from flask import jsonify


# @description This is database model file that contains db operations for product model
class ProductModel():

    DB = Connection().db
    productCollection = DB[PRODUCT_DETAILS_COLLECTION]


    #
    # @description This method will help to send aggregate request to DB
    #
    # @param {List} [condition=[]]
    # @returns {Object}
    # @memberof ProductModel
    #
    def aggregate(self, aggregateQuery):
        try:
            result = self.productCollection.aggregate(aggregateQuery)
            return list(result)
        except Exception as err:
            return jsonify({'error': f'{err}'}), 500


    #
    # @description This method will help to send create request to DB
    #
    # @param {Object} product
    # @returns 
    # @memberof ProductModel
    #
    def insert(self, product):
        try:
            result = self.productCollection.insert_one(product)
            return True
        except Exception as err:
            return jsonify({'error': f'{err}'}), 500


    #
    # @description This method will help to send find request to DB
    #
    # @param {String} productId
    # @returns {Object}
    # @memberof ProductModel
    #
    def find(self, productId):
        try:
            result = self.productCollection.find_one({"_id": ObjectId(productId)})
            return result
        except Exception as err:
            return jsonify({'error': f'{err}'}), 500


    #
    # @description This method will help in send update data request to DB
    #
    # @param {String} productId
    # @param {Integer} reduceQuantity
    # @returns 
    # @memberof ProductModel
    #
    def update(self, productId, reduceQuantity):
        try:
            result = self.productCollection.update_one(
                {"_id": ObjectId(productId)},
                {"$set": {"quantity": reduceQuantity}}
                )
            return result
        except Exception as err:
            return jsonify({'error': f'{err}'}), 500

