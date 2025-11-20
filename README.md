📦 Product Recommendation System (FastAPI + Jinja2)

A web-based product recommendation system built using FastAPI, Pandas, NumPy, and Jinja2 HTML templates.
It allows users to filter and get recommendations for:

💻 Laptops

📱 Smartphones

📺 Televisions

📷 Cameras

🎧 Headphones

More than 500+ synthetic product entries are generated dynamically using Python.

🚀 Features
✅ Multi-category product filtering

Each category includes filtering options:

Laptops → brand, processor, RAM, storage, purpose, price

Phones → brand, RAM, storage, camera, price

TVs → brand, size, display type, resolution, smart TV, price

Cameras → brand, camera type, megapixels, video quality, price

Headphones → brand, type, noise cancelling, wireless, price

✅ Dynamic recommendation system

Filters dataset based on user selections

Shows Top 20 results sorted by rating

Displays clean UI product cards

✅ Auto-generated dataset (no external DB needed)

500+ synthetic product records generated using NumPy

DataFrames stored in memory for fast access

✅ Clean and modern GUI

Built using HTML5 + CSS (static folder)

Jinja2 used to inject data dynamically

Home page + filter pages + results page

🛠️ Tech Stack
Component	Technology
Backend	FastAPI
Templating	Jinja2
Data	Pandas, NumPy
Server	Uvicorn
UI	HTML + CSS
Deployment	Local / Cloud
📂 Project Structure
project/
│── main.py
│── requirements.txt
│── templates/
│     ├── index.html
│     ├── laptops.html
│     ├── phones.html
│     ├── tvs.html
│     ├── cameras.html
│     ├── headphones.html
│     └── results.html
│── static/
│     ├── style.css
│     └── assets (optional)

🔧 Installation & Setup
1️⃣ Clone the repository
git clone (https://github.com/piyushranjan07/Product_Recoommendation_System/tree/main)
cd repo-name

2️⃣ Install dependencies
pip install -r requirements.txt


If requirements.txt not added yet, use:

pip install fastapi uvicorn pandas numpy jinja2

3️⃣ Run the FastAPI server
uvicorn main:app --reload

4️⃣ Open the browser
http://127.0.0.1:8000/

🖥️ How the System Works
➤ 1. Choose a Category

The home page lists all product categories.

➤ 2. Apply Filters

Each category has its own filter page built using Jinja2.

➤ 3. Get Recommendations

FastAPI processes filters → filters the DataFrame → returns top results → displays in a card layout.

🧪 API Endpoints (Frontend-driven)
Method	Route	Description
GET	/	Home page
GET	/laptops	Laptop filter UI
POST	/laptops/recommend	Laptop recommendations
GET	/phones	Phone filter UI
POST	/phones/recommend	Phone recommendations
GET	/tvs	TV filter UI
POST	/tvs/recommend	TV recommendations
GET	/cameras	Camera filter UI
POST	/cameras/recommend	Camera recommendations
GET	/headphones	Headphone filter UI
POST	/headphones/recommend	Headphone recommendations

🛠️ Future Enhancements

Connect to a real database (MongoDB / PostgreSQL)

Add machine learning-based recommendations

Add login system + user preferences

Make UI more modern using Tailwind / Bootstrap

Add comparison feature between two products

🤝 Contributing

Pull requests and improvements are welcome!
