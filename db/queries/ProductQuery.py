#
# @description File for fetching queries for retrieving Paginated Product Details
#

class ProductQuery():


    #
    # @description Get raw query to fetch paginated schema list for Monitor and Data Operator
    #
    # @param {Integer} offset Offset after which records need to be fetched
    # @param {Integer} limit Page Size for pagination
    # @param {Object} filterConditions FilterCondition to filter records based on minimum price or maximum price or both
    # @returns {List} conditions
    # @memberof ProductQuery
    #
    def buildAggregationQuery(self, filterConditions, offset, limit):
        aggregationQuery = [
            {
                "$match": filterConditions
            },
            {
                "$facet": {
                    "records": [
                        {
                            "$skip": offset
                        },
                        {
                            "$limit": limit
                        },
                        {
                            "$project": {
                                "id": "$_id", 
                                "name": 1, 
                                "priceInINR": 1, 
                                "quantity": 1
                            }
                        }
                    ],
                "total": [
                        {
                            "$count": "total"
                        }
                    ]
                }
            },
            {
                "$unwind": "$total"
            },
            {
                "$set": {
                    "total_records": "$total.total",
                    "limitValue": limit
                }
            },
            {
                "$project": {
                    "records": 1,
                    "page": {
                        "limit": "$limitValue",
                        "nextOffset": {"$cond": {"if": {"$lt": [offset + limit, "$total_records"]}, "then": offset + limit, "else": None}},
                        "prevOffset": {"$cond": {"if": {"$gte": [offset - limit, 0]}, "then": offset - limit, "else": None}},
                        "total": "$total.total"
                    }
                }
            }
        ]
        return aggregationQuery