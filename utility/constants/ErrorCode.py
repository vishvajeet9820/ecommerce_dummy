class Error:

    @staticmethod
    def INTERNAL_SERVER_ERROR():
        return 'Internal Server Error'

    @staticmethod
    def INVALID_SKIP():
        return 'Skip should be an integer'

    @staticmethod
    def INVALID_LIMIT():
        return 'Limit should be an integer'

    @staticmethod
    def INVALID_MAXIMUM_PRICE_FILTER():
        return 'Maximum Price filter value must be either an integer or a floating-point number'

    @staticmethod
    def INVALID_MAXIMUM_PRICE_FILTER_VALUE():
        return 'Maximum Price value should not be less than 0'

    @staticmethod
    def INVALID_MINIMUM_PRICE_FILTER():
        return 'Minimum Price filter value must be either an integer or a floating-point number'

    @staticmethod
    def INVALID_MINIMUM_PRICE_FILTER_VALUE():
        return 'Minimum Price value should not be less than 0'

    @staticmethod
    def INVALID_MINIMUM_MAXIMUM_PRICE_FILTER_VALUE():
        return 'Minimum Price and Maximum Price filter values should not be less than 0'

    @staticmethod
    def MINIMUM_PRICE_LESS_OR_EQUAL_MAXIMUM_PRICE():
        return 'Minimum Price filter value should be less than or equal to Maximum Price filter value'

    @staticmethod
    def PRODUCT_NAME_MISSING():
        return 'Name of the product is missing'

    @staticmethod
    def SHORTAGE_OF_ITEM(productId, leftPieces):
        return f'The inventory is experiencing a shortage of the product with the specified product ID. :- {productId}, Available pieces :- {leftPieces}'

    @staticmethod
    def INVALID_PRODUCT(productId):
        return f'The product with the product ID. :- {productId} is unavailable in the inventory. The provided product ID is invalid'

    