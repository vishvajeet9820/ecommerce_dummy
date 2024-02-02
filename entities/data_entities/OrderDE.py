from pydantic import BaseModel
from typing import List

# @description This is a data entity for Order

class OrderItem(BaseModel):
    productId: str
    boughtQuantity: int

    # Getter and Setter for productId
    @property
    def productId(self):
        return self.productId

    @productId.setter
    def productId(self, productId):
        self.productId = productId

    # Getter and Setter for boughtQuantity
    @property
    def boughtQuantity(self):
        return self.boughtQuantity

    @boughtQuantity.setter
    def boughtQuantity(self, boughtQuantity):
        self.boughtQuantity = boughtQuantity

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

    # Getter and Setter for city
    @property
    def city(self):
        return self.city

    @city.setter
    def city(self, city):
        self.city = city

    # Getter and Setter for country
    @property
    def country(self):
        return self.country

    @country.setter
    def country(self, country):
        self.country = country

    # Getter and Setter for zip_code
    @property
    def zip_code(self):
        return self.zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self.zip_code = zip_code

class Order(BaseModel):
    createdOn: str
    items: List[OrderItem]
    total_amount: float
    user_address: UserAddress

    # Getter and Setter for createdOn
    @property
    def createdOn(self):
        return self.createdOn

    @createdOn.setter
    def createdOn(self, createdOn):
        self.createdOn = createdOn

    # Getter and Setter for items
    @property
    def items(self):
        return self.items

    @items.setter
    def items(self, items):
        self.items = items

    # Getter and Setter for total_amount
    @property
    def total_amount(self):
        return self.total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self.total_amount = total_amount

    # Getter and Setter for user_address
    @property
    def user_address(self):
        return self.user_address

    @user_address.setter
    def user_address(self, user_address):
        self.user_address = user_address

    
