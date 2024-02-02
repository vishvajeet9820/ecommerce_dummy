# README
Ecommerce Backend Service

This project implements a simple ecommerce API using Flask and MongoDB.

## Features

- **List Products API**: Retrieves a paginated list of available products wih optional filters for minimum and maximum prices.

- **Create Order API**: Creates a new order with a list of items, total amount and user address.

- **Fetch All Orders API**: Retrieves all order details.

- **Add Product API**: Adds new product in the inventory with their name, price in INR and available quantity

  ## Tech Stack

  - Python 3
  - Flask
  - MongoDB with Pymongo
 
  ## Project Structure

  - **main.py**: It's an entry point to the backend service.
 
  - **requirements.txt**: Lists the project dependencies, including Flask and PyMongo.
 
  - **routes**: This folder contains a file route.py where all endpoints are listed.
 
  - **services**: Service folder contains logic part of the project for the implementation of the API endpoints
 
  - **utility**: This folder is for storing constant variables used in this backend application.
 
  - **models**: It contains CRUD operation for different resources/entities.
 
  - **queries**: It contains aggregate query which is utilised to group data based on various filters used and provides the summed up results.
 
  - **configs**: Holds settings and parameters required by the service to get started
 
  ## Setup

1. Install project dependencies
   
  ```bash
  pip install -r requirements.txt
  ```

2. Make sure you have a Mongo DB server running locally 
