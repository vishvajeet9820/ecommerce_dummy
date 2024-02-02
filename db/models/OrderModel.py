from bson import ObjectId
from configs.config import ORDER_DETAILS_COLLECTION
from db.Connections import Connection
from flask import jsonify

# @description This is database model file that contains db operations for order model
class OrderModel():

    DB = Connection().db
    orderCollection = DB[ORDER_DETAILS_COLLECTION]


    #
    # @description This method will insert new orders
    #
    # @param {Object} [newOrder={}]
    # @returns
    # @memberof OrderModel
    #
    def insert(self, newOrder):
        try:
            result = self.orderCollection.insert_one(newOrder)
            return True
        except Exception as err:
            return jsonify({'error': f'{err}'}), 500


    #
    # @description This method will find all orders placed
    #
    # @param
    # @returns
    # @memberof OrderModel
    #
    def findAll(self):
        try:
            result = self.orderCollection.find()
            return list(result)
        except Exception as err:
            return jsonify({'error': f'{err}'}), 500


