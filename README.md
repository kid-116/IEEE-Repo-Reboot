# IEEE-Repo-Reboot
## *Track: NLP Based Search Engine for an E-Commerce Website*
<br>

## Installation

1. In your terminal, navigate to the directory where you want to install the repository <br>

2. Clone the repository <br>
`git clone https://github.com/kid-116/IEEE-Repo-Reboot.git`

3. Navigate to the flask_server <br>
`cd IEEE-Repo-Reboot//flask_server`

4. Install requirements <br>
`pip install -r requirements.txt`

5. Start the server <br>
`flask run`
6. Go to [localhost:5000](http://localhost:5000) to see the website <br>
`http://localhost:5000`

## Search Implementation
1. A query input is taken by the user and passed to a spell check API.
2. If any spelling mistake is detected by the spell check API, the corrected query is displayed to the user with a link to search with the corrected query. 
3. Then the query is passed to the NLP model, trained by us and deployed on Azure. 
4. The NLP model returns the categories with confidence scores and we select the top 3 categories.
5. All the products within the 3 categories are retrieved from the [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) database.
6. The products are sorted using [thefuzz](https://github.com/seatgeek/thefuzz) python package and a list of products with a high string similarity score is returned.
7. If no relevant products are found within the categories, a string similarity search is done on the entire database.

## Website
We have created a simple website which allows the user to browse the inventory and allows admins, who have access to the admin key, to perform CRUD operations on the database. We have used [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) to make the website responsive. We used python decorators for authentication middleware to prevent unauthorized access. Dynamic templating was implemented using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/).

## Dummy Inventory
We are populating our database using a Kaggle E-commerce dataset using a [python notebook](./dummy_inventory/inventory_creation.ipynb). In the notebook we mapped their categories to the categories defined in our NLP model and inserted them to the databse. We are not uploading images for the dummy products as it would take a lot of data, instead we are using a [random picture service](https://picsum.photos/).

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


