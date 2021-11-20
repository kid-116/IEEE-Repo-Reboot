# IEEE-Repo-Reboot
## Track: NLP Based Search Engine for an E-Commerce Website
## Progress
### Done
- NLP model has been trained and deployed using Azure ML Studio
- Backend flask server is completed
- Responsive frontend UI has been designed
### Todo
- NLP model API is to be connected to the flask server search feature
- Dummy inventory is to be added
- Flask server needs to be deployed on a service like Heroku

## Multi-Class Natural Language Processing Model
To train and deploy a Natural Language Processing Multi-Class Classification Model to determine the category (or set of most probable categories) of the product from the search query thereby reducing the search time for queries on the e-commerce website.
### Steps
0. Finding the proper dataset
1. Data preparation
2. Text preprocessing
3. Feature engineering
4. Train and evaluate models
5. Deploy trained models as web services



### Step 0: 
**Dataset link**: [Amazon review data (nijianmo.github.io)](https://nijianmo.github.io/amazon/index.html)

Data used: 10,000 products from each category (filtered through the metadata using collab notebooks in .jsonl (json line format))

**Categories include:**

-	All Beauty
-	Arts, Crafts & Sewing
-	Automotive
-	Books
-	Cell Phones & Accessories
-	Clothing, Shoes and Jewelry
-	Electronics
-	Home and Kitchen
-	Industrial & Scientific
-	Luxury Beauty
-	Musical Instruments
-	Office Products
-	Pantry
-	Software
-	Sports & Outdoors
-	Sports Collectibles
-	Tools & Home Improvement
-	Toys & Games
-	Video Games

### Step 1: 
**Data preparation**
<br>
<br>
 ![Data preparation](./images/data-prep-pipeline.png)


