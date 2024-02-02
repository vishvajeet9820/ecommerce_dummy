from services.OrderService import OrderService
from services.ProductService import ProductService


def route_setup(app):
    #
    # @api {get} /get-products Get Product list
    # @apiName Get Product list
    # @apiDescription User can get list of products
    # 
    # @apiParam (Query parameter) {Integer} skip      Page number
    # @apiParam (Query parameter) {Integer} limit     Maximum number of results to be returned
    # @apiParam (Query parameter) {Float} min_price      Minimum Price search parameter to filter records
    # @apiParam (Query parameter) {Float} max_price     Maximum Price search parameter to filter records
    # 
    # @apiParamExample {json} Input
    #   {
    #      "skip": 1,
    #      "limit": 10
    #   }
    #
    # @apiSuccessExample {json} SuccessResponse
    #    {
    #        "code": "RECORD_FETCHED_SUCCESSFULLY",
    #        "data": [
    #            {
    #                "page": {
    #                    "limit": 5,
    #                    "nextOffset": 5,
    #                    "prevOffset": null,
    #                    "total": 7
    #                },
    #                "records": [
    #                    {
    #                        "id": "65b956d9e14c0917859f6e1f",
    #                        "name": "Samsung Galaxy",
    #                        "priceInINR": 100000,
    #                        "quantity": 9
    #                    },
    #                    {
    #                        "id": "65ba558801ea367913f74975",
    #                        "name": "Apple Iphone",
    #                        "priceInINR": 129000,
    #                        "quantity": 53
    #                    },
    #                    {
    #                        "id": "65ba569801ea367913f74976",
    #                        "name": "Redmi",
    #                        "priceInINR": 18000,
    #                        "quantity": 13
    #                    },
    #                    {
    #                        "id": "65bacb9f72276add6ade6b09",
    #                        "name": "Motorola",
    #                        "priceInINR": 25500,
    #                        "quantity": 50
    #                    },
    #                    {
    #                        "id": "65bacc2680b56be747e747dc",
    #                        "name": "Huawei",
    #                        "priceInINR": 33625,
    #                        "quantity": 33
    #                    }
    #                ]
    #            }
    #        ],
    #        "message": "Record fetched successfully",
    #        "status": "success"
    #    }
    #
    # @apiErrorExample {Object} INVALID_MAXIMUM_PRICE_FILTER_VALUE
    # HTTP/1.1 400 INVALID_MAXIMUM_PRICE_FILTER_VALUE
    #   {
    #        "error": "Maximum Price value should not be less than 0"
    #   }
    #        
    @app.route("/get-products")
    def getProducts():
        productObject = ProductService()
        return productObject.getProducts()
        

    #
    # @api {post} /add-products Add Product in the inventory
    # @apiName Add Product in the inventory
    # @apiDescription User can add a product in the inventory
    # 
    # @param (Request body) {String} name Name of the product
    # @param (Request body) {Float} price_in_INR Price of the product in INR 
    # @param (Request body) {Integer} quantity Product available quantity
    # 
    # @apiParamExample {json} Input
    #   {
    #       "name": "Huawei",
    #       "quantity": "33", 
    #       "price_in_INR": 33625
    #   }
    #
    # @apiSuccessExample {json} SuccessResponse
    # {
    #    "code": "RECORD_ADDED_SUCCESSFULLY",
    #    "data": {
    #        "name": "Sansui",
    #        "priceInINR": 15627,
    #        "quantity": 76
    #    },
    #    "message": "Record added successfully",
    #    "status": "success"
    # }
    #
    # @apiErrorExample {Object} PRODUCT_NAME_MISSING
    # HTTP/1.1 400 PRODUCT_NAME_MISSING
    # {
    #    "error": "Name of the product is missing"
    # }
    #
    @app.route("/add-products", methods = ["POST"])
    def addProducts():
        productObject = ProductService()
        return productObject.addProducts()
        

    #
    # @api {post} /new-order Placing a new order
    # @apiName Placing a new order
    # @apiDescription User can place a new order
    # 
    # @param (Request body) {Object} user_address Stores the details like city, country and zip_code
    # @param (Request body) {List} item_list Stores productId and boughtQuantity of the products which are part of the order 
    # 
    # @apiParamExample {json} Input
    # {
    #    "user_address": {
    #        "city": "HLO",
    #        "country": "IND",
    #        "zip_code": 201001
    #    },
    #    "item_list": [
    #        {
    #            "productId": "65b956d9e14c0917859f6e1f",
    #            "boughtQuantity": 10
    #        }
    #    ]
    # }
    #
    # @apiSuccessExample {json} SuccessResponse
    # {
    #    "code": "ORDER_PLACED_SUCCESSFULLY",
    #    "data": {
    #        "createdOn": "Fri, 02 Feb 2024 01:55:31 GMT",
    #        "items": [
    #            {
    #                "boughtQuantity": 10,
    #                "productId": "65b956d9e14c0917859f6e1f"
    #            }
    #        ],
    #        "total_amount": 1000000,
    #        "user_address": {
    #            "city": "HLO",
    #            "country": "IND",
    #            "zip_code": 201009
    #        }
    #    },
    #    "message": "Order placed successfully",
    #    "status": "success"
    # }
    #
    # @apiErrorExample {Object} INVALID_PRODUCT
    # HTTP/1.1 400 INVALID_PRODUCT
    # {
    #    "error": "The product with the product ID. :- 65b956d9e14c0917859f6e15 is unavailable in the inventory. The provided product ID is invalid"
    # }
    #
    @app.route("/new-order", methods = ["POST"])
    def newOrder():
        orderObject = OrderService()
        return orderObject.newOrder()
        

    #
    # @api {post} /fetch-orders Get list of all orders placed
    # @apiName Get list of all orders placed
    # @apiDescription User can get list of all orders placed
    # 
    # @param  
    # 
    #
    # @apiSuccessExample {json} SuccessResponse
    # {
    #    "code": "ORDER_LIST_FETCHED_SUCCESSFULLY",
    #    "data": [
    #        {
    #            "createdOn": 1706722996.732807,
    #            "items": [
    #                {
    #                    "boughtQuantity": 19,
    #                    "productId": "65b956d9e14c0917859f6e1f"
    #                },
    #                {
    #                    "boughtQuantity": 19,
    #                    "productId": "65ba558801ea367913f74975"
    #                },
    #                {
    #                    "boughtQuantity": 23,
    #                    "productId": "65ba569801ea367913f74976"
    #                }
    #            ]
    #            "total_amount": 4765000,
    #            "user_address": {
    #                "city": "KLO",
    #                "country": "IND",
    #                "zip_code": 221300
    #            }
    #        }
    #        "message": "Order List fetched successfully",
    #        "status": "success"
    # }
    #
    @app.route('/fetch-orders')
    def fetchOrders():
        orderObject = OrderService()
        return orderObject.fetchOrders()
