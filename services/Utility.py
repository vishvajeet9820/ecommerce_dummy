# @description  This class will contain utility functions for different services.
class Utility():

    # @description The method checks if the provided value is a float or not
    # @param {any} value
    # @returns {Boolean} True/False
    # @memberof Utility
    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False