from pydantic import BaseModel
from uuid import UUID

# @description This is a data entity for Product

class Product(BaseModel):
    _id: UUID
    name: str
    priceInINR: float
    quantity: int

    # Getter and Setter for properties
    def getSetProperty(self, prop_value=None):
        if prop_value is not None:
            return prop_value
        return self.getSetProperty

    @property
    def id(self):
        return self.getSetProperty(self._id)

    @id.setter
    def id(self, _id):
        self._id = _id

    @property
    def name(self):
        return self.getSetProperty(self.name)

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def priceInINR(self):
        return self.getSetProperty(self.priceInINR)

    @priceInINR.setter
    def priceInINR(self, priceInINR):
        self.priceInINR = priceInINR

    @property
    def quantity(self):
        return self.getSetProperty(self.quantity)

    @quantity.setter
    def quantity(self, quantity):
        self.quantity = quantity
