
from math import prod
from flask import Flask, request, abort
from mock_data import catalog
import json 
import random
from config import db
from flask_cors import CORS
from bson import ObjectId


app = Flask(__name__)
CORS(app) # *DANGER* anyone can connect to this server

me = {
            "name": "Shakita",
            "last": "Thompson",
            "age": 32,
            "hobbies": [],
            "address": {
                "street": "Margarita",
                "number": 28,
                "city": "Oceanside",
            }
        }       


@app.route("/", methods=['GET'])
def home():
    return "Hello from Python"

@app.route("/test")
def any_name():
    return "I'm a test function"  

@app.route("/about")
def about():
    return me["name"] + " " + me["last"]




#**********************************************
#**************** API ENDPOINTS ***************
#**********************************************



@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for product in cursor:
        product["_id"] = str(product["_id"])
        results.append(product)


    return json.dumps(results)


@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    print (product)

    # data validation
    # if the product does not contain a title, and is at least 5 chars long
    # return an error
    if not 'title' in product or len(product["title"]) < 5:
        return abort(400, "Title is required, and should be at least 5 chars long")

    # there should be a price
    if not "price" in product:
        return abort(400, "Price is required")   

    # if price is not float and not an int, error
    if not isinstance(product["price"], float) and not isinstance(product["price"], int):
        return abort(400, "Price should be a valid number")   


    # the price should be greater than 0
    if product["price"] <= 0:
        return abort(400, "Price should be greater than zero") 


    # save the product in the catalog
    db.products.insert_one(product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)


@app.route("/api/cheapest")
def get_cheapest():
    # find the cheapest product on the catalog list
    cursor = db.products.find({})
    cheap = cursor[0]
    for product in cursor:
        if product["price"] < cheap["price"]:
            cheap = product

    cheap["_id"] = str(cheap["_id"])

    # return it as json
    return json.dumps(cheap)

@app.route("/api/product/<id>")
def get_product(id):
    # validate if id is a valid ObjectId
    if (not ObjectId.is_valid(id)):
        return abort(400, "id is not a valid ObjectId")

    #find the product whose _id is equal to id
    result = db.products.find_one({"_id": ObjectId(id)})
    if not result:
        return abort(404) # 404 = not found
    result["_id"] = str(result["_id"])

    return json.dumps(result)



# end point to retrieve all the products by category
# you should recieve the cat name,
# return all the products that belong to that category
@app.route("/api/catalog/<category>")
def get_by_category(category):
    # do the magic
    result = []
    for product in catalog:
        if product["category"] == category:
            result.append(product)

   
    return json.dumps(result)        




# /api/categories
# return the list of unique category names
@app.route("/api/categories")
def get_categories():
    result = []
    for product in catalog:
        cat = product["category"]
        if cat not in result:
            result.append(cat)

    return json.dumps(result)


# GET /api/reports/prodCount
@app.route("/api/reports/prodCount")
def get_prod_count():
    count = len(catalog)
    return json.dumps(count)




@app.route("/api/reports/total")
def get_total():
    total = 0

    # print the title of each product
    for prod in catalog:
        totalProd = pro["price"] * prod["stock"]
        total += totalProd

    return json.dumps(total)




   
   
# /api/reports/highestInvestment
@app.route("/api/reports/highestInvesetment")
def get_highest_investment():
    highest = catalog[0]

    for prod in catalog:
        prod_invest = prod["price"] * prod["stock"]
        high_invest = highest["price"] * highest["stock"]

        if prod_invest > high_invest:
            highest = prod
   
     
    return json.dumps(highest)
   
   
   

   
# start the server
app.run(debug=True)












