from db.models.ProductModel import ProductModel
from db.queries.ProductQuery import ProductQuery
from entities.data_entities.ProductDE import Product
from flask import request, jsonify
from pydantic import BaseModel
from services.Utility import Utility
from utility.constants.ErrorCode import Error as ErrorConstant
import traceback
import uuid


# @description This class contains the services for fetching product details and adding new product details
class ProductService(BaseModel):

    #
    # @description Get paginated product details 
    #
    # @param {Integer} limit Page size for pagination
    # @param {Integer} skip Offset after which records need to be fetched
    # @param {Float} min_price Minimum Price search parameter to filter records
    # @param {Float} max_price Maximum Price search parameter to filter records
    # @returns {Object} {
    #      "code": "CODE",
    #      "data": [
    #          {
    #              "page": {
    #                  "limit": "LIMIT",
    #                  "nextOffset": "NEXT_OFFSET",
    #                  "prevOffset": "PREVIOUS_OFFSET",
    #                  "total": "TOTAL"
    #              },
    #              "records": [
    #                  {
    #                      "id": "ID",
    #                      "name": "NAME",
    #                      "priceInINR": "PRICE",
    #                      "quantity": "QUANTITY"
    #                  }
    #              ]
    #          }
    #      ],
    #      "message": "MESSAGE",
    #      "status": "STATUS"
    #  }
    # @memberof ProductService
    #
    def getProducts(self):
        try:
            print("-----In ProductService getProducts method-----")
            limit = request.args.get('limit', "5")
            skip = request.args.get('skip', "0")
            minPrice = request.args.get('min_price')
            maxPrice =  request.args.get('max_price')

            util = Utility()

            if minPrice is not None and util.is_float(minPrice) == False: 
                return jsonify({'error': ErrorConstant.INVALID_MINIMUM_PRICE_FILTER()}), 400
            if maxPrice is not None and util.is_float(maxPrice) == False:
                return jsonify({'error': ErrorConstant.INVALID_MAXIMUM_PRICE_FILTER()}), 400

            if minPrice is not None and maxPrice is not None: 
                if float(minPrice) < 0 and float(maxPrice) < 0:
                    return jsonify({'error': ErrorConstant.INVALID_MINIMUM_MAXIMUM_PRICE_FILTER_VALUE()}), 400
                elif float(minPrice) > float(maxPrice):
                    return jsonify({'error': ErrorConstant.MINIMUM_PRICE_LESS_OR_EQUAL_MAXIMUM_PRICE()}), 400
            elif (minPrice is not None and float(minPrice) < 0):
                return jsonify({'error': ErrorConstant.INVALID_MINIMUM_PRICE_FILTER_VALUE()}), 400  
            elif (maxPrice is not None and float(maxPrice) < 0): 
                return jsonify({'error': ErrorConstant.INVALID_MAXIMUM_PRICE_FILTER_VALUE()}), 400

            filterConditions = dict()
            if minPrice is not None and maxPrice is not None:
                filterConditions['priceInINR'] = {'$gte': float(minPrice), '$lte': float(maxPrice)}
            elif minPrice is not None:
                filterConditions['priceInINR'] = {'$gte': float(minPrice)}
            elif maxPrice is not None:
                filterConditions['priceInINR'] = {'$lte': float(maxPrice)}
            else:
                filterConditions['priceInINR'] = {'$gte': 1}
            
            if skip is not None and skip.isnumeric() == True:
                skip = int(skip)  
            else: 
                return jsonify({'error': ErrorConstant.INVALID_SKIP()}), 400
            if limit is not None and limit.isnumeric() == True:
                limit = int(limit)  
            else: 
                return jsonify({'error': ErrorConstant.INVALID_LIMIT()}), 400

            offset = skip * limit

            productQuery = ProductQuery()
            aggregateQuery = productQuery.buildAggregationQuery(filterConditions, offset, limit)

            productModel = ProductModel()
            productList = productModel.aggregate(aggregateQuery)

            if productList:
                for product in productList[0]['records']:
                    product['id'] = str(product['_id'])
                    del product["_id"]
            else:
                productList.append({"records": [], "page":{'limit': limit, 'total': 0}})

            response = jsonify({
                    'status': 'success',
                    'message': 'Record fetched successfully',
                    'code': 'RECORD_FETCHED_SUCCESSFULLY',
                    'data': productList
                })
            response.charset = 'utf-8'
            return response, 200
        except Exception as err:
            # Return error response if an exception occurs
            traceback_str = traceback.format_exc() 
            print(f"***** Error in ProductService getProducts method *****: {err}\n{traceback_str}")
            response = {
                'message': str(err),
                'code': 'INTERNAL_SERVER_ERROR',
                'status': ErrorConstant.INTERNAL_SERVER_ERROR()
            }
            return jsonify(response), 500


    #
    # @description Method to save product details in the database
    #
    # @param {String} name Name of the product
    # @param {Float} price_in_INR Price of the product in INR 
    # @param {Integer} quantity Product available quantity
    # @returns {Object} {
    #       "code": "CODE",
    #       "data": {
    #           "name": "NAME",
    #           "priceInINR": "PRICE_IN_INR",
    #           "quantity": "QUANTITY"
    #       },
    #       "message": "MESSAGE",
    #       "status": "STATUS"
    #   }
    # @memberof ProductService
    #
    def addProducts(self):
        try:
            print("-----In ProductService addProducts method-----")
            data = request.get_json()
            product = Product()
            product._id = uuid.uuid4()
            product.name = data.get('name', "")
            if product.name == "":
                return jsonify({'error': ErrorConstant.PRODUCT_NAME_MISSING()}), 400
            product.priceInINR = int(data.get('price_in_INR', 0))
            product.quantity = int(data.get('quantity', 0))
            
            productModel = ProductModel()
            productModel.insert(dict(product))

            response = {
                    'status': 'success',
                    'message': 'Record added successfully',
                    'code': "RECORD_ADDED_SUCCESSFULLY",
                    'data': dict(product)
                }
            return jsonify(response), 201
        except Exception as err:
            # Return error response if an exception occurs
            traceback_str = traceback.format_exc() 
            print(f"***** Error in ProductService addProducts method *****: {err}\n{traceback_str}")
            response = {
                'message': str(err),
                'code': 'INTERNAL_SERVER_ERROR',
                'status': ErrorConstant.INTERNAL_SERVER_ERROR()
            }
            return jsonify(response), 500

