from db.models.ProductModel import ProductModel
from db.models.OrderModel import OrderModel
from datetime import datetime
from entities.data_entities.OrderDE import OrderItem, UserAddress, Order
from flask import request, jsonify
from pydantic import BaseModel
from utility.constants.ErrorCode import Error as ErrorConstant
import traceback


# @description This class contains the services for fetching order details and placing new order
class OrderService(BaseModel):

    #
    # @description Get details of all orders already being placed 
    #
    # @params
    # @returns {Object} {
    #      "code": "CODE",
    #      "data": [
    #          {
    #              "createdOn": "CREATED_ON",
    #              "items": [
    #                  {
    #                      "boughtQuantity": "BOUGHT_QUANTITY",
    #                      "productId": "PRODUCT_ID"
    #                  }
    #              ],
    #              "total_amount": "TOTAL_AMOUNT",
    #              "user_address": {
    #                  "city": "CITY",
    #                  "country": "COUNTRY",
    #                  "zip_code": "ZIP_CODE"
    #              }
    #          }
    #      ],
    #      "message": "MESSAGE",
    #      "status": "STATUS"
    #  }
    # @memberof OrderService
    #
    def fetchOrders(self):
        try:
            print("-----In OrderService fetchOrders method-----")
            orderModel = OrderModel()
            orderRecordsList = orderModel.findAll()
        
            for order in orderRecordsList:
                del order['_id']
            response = jsonify({
                    'status': 'success',
                    'message': 'Order List fetched successfully',
                    'code': "ORDER_LIST_FETCHED_SUCCESSFULLY",
                    'data': orderRecordsList
                })
            return response, 200
            
        except Exception as err:
            # Return error response if an exception occurs
            traceback_str = traceback.format_exc() 
            print(f"***** Error in OrderService fetchOrders method *****: {err}\n{traceback_str}")
            response = {
                'message': str(err),
                'code': 'INTERNAL_SERVER_ERROR',
                'status': ErrorConstant.INTERNAL_SERVER_ERROR()
            }
            return jsonify(response), 500


    #
    # @description Method to place new orders and save details of the order in the database
    #
    # @param {Object} user_address Stores the details like city, country and zip_code
    # @param {List} item_list Stores productId and boughtQuantity of the products which are part of the order  
    # @returns {Object} {
    #       "code": "CODE",
    #       "data": {
    #           "createdOn": "CREATED_ON",
    #           "items": [
    #               {
    #                   "boughtQuantity": "BOUGHT_QUANTITY",
    #                   "productId": "PRODUCT_ID"
    #               }
    #           ],
    #           "total_amount": "TOTAL_AMOUNT",
    #           "user_address": {
    #               "city": "CITY",
    #               "country": "COUNTRY",
    #               "zip_code": "ZIP_CODE"
    #           }
    #       },
    #       "message": "MESSAGE",
    #       "status": "STATUS"
    #   }
    # @memberof OrderService
    #
    def newOrder(self):
        try:
            print("-----In OrderService newOrder method-----")
            data = request.get_json()
            userAddress = UserAddress()
            userAddressObject = data.get('user_address', {})
            userAddress.city = userAddressObject['city'] if 'city' in list(userAddressObject.keys()) else ""
            userAddress.country = userAddressObject['country'] if 'country' in list(userAddressObject.keys()) else ""
            userAddress.zip_code = userAddressObject['zip_code'] if 'zip_code' in list(userAddressObject.keys()) else ""
            order = OrderItem()
            orderObject = data.get('item_list', [])
            orderList = list()
            totalAmount = 0
            updateProductDetail = dict()
            productModel = ProductModel()
            for item in orderObject:
                order.productId = item['productId']
                order.boughtQuantity = item['boughtQuantity']
                try:
                    isProductAvailable = productModel.find(order.productId)
                except Exception as err:
                # Handle the exception, e.g., return a default ObjectId or raise a custom exception
                    if "is not a valid ObjectId" in str(err):
                        return jsonify({'error': f'Invalid ObjectId: {order.productId} :- {err}'}), 400
                    else:
                        return jsonify({'error': f'Invalid ObjectId: {order.productId}. :- {err}'}), 400

                if isProductAvailable is None:
                    return jsonify({'error': ErrorConstant.INVALID_PRODUCT(order.productId)}), 400 
                else:
                    leftPieces = int(isProductAvailable['quantity'])
                    if order.boughtQuantity > leftPieces:
                        return jsonify({'error': ErrorConstant.SHORTAGE_OF_ITEM(order.productId, leftPieces)}), 400
                    else:
                        pricePerPiece = int(isProductAvailable['priceInINR'])
                        orderList.append(dict(order))
                        totalAmount += (order.boughtQuantity * pricePerPiece)
                        reduceQuantity = int(leftPieces - order.boughtQuantity)
                        product_id = order.productId
                        updateProductDetail[product_id] = reduceQuantity
            
            productIdsList = list(updateProductDetail.keys())

            newOrder = Order()
            newOrder.createdOn = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
            newOrder.items = orderList
            newOrder.total_amount = totalAmount
            newOrder.user_address = dict(userAddress)

            orderModel = OrderModel()
            orderModel.insert(dict(newOrder))

            for productItemId in productIdsList:
                productModel.update(str(productItemId), updateProductDetail[productItemId])

            response = {
                    'status': 'success',
                    'message': 'Order placed successfully',
                    'code': "ORDER_PLACED_SUCCESSFULLY",
                    'data': dict(newOrder)
                }
            return jsonify(response), 201

        except Exception as err:
            # Return error response if an exception occurs
            traceback_str = traceback.format_exc() 
            print(f"***** Error in OrderService newOrder method *****: {err}\n{traceback_str}")
            response = {
                'message': str(err),
                'code': 'INTERNAL_SERVER_ERROR',
                'status': ErrorConstant.INTERNAL_SERVER_ERROR()
            }
            return jsonify(response), 500