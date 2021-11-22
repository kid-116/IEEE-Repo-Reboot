const categories = ["All Beauty", "Arts, Crafts & Sewing", "Automotive", "Books", "Cell Phones & Accessories", "Clothing, Shoes and Jewelry", "Electronics", "Home and Kitchen", "Industrial & Scientific", "Luxury Beauty", "Musical Instruments", "Office Products", "Pantry", "Software", "Sports & Outdoors", "Sports Collectibles", "Tools & Home Improvement", "Toys & Games", "Video Games"];

categories.forEach((category)=>{
    var ul = document.getElementById("dropdown-menu");
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.appendChild(document.createTextNode(category));
    a.setAttribute("class", "dropdown-item");
    category = category.toLowerCase().replace(/\s/g, '-');
    a.setAttribute("href", "/products/categories/" + category)
    li.appendChild(a);
    ul.appendChild(li);
});

const searchButton = document.getElementById('search-button');
const spinner = document.getElementById('spinner');
searchButton.onclick = function() {
    console.log('searching...');
    spinner.style.visibility = 'visible';
}