# main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 
import pandas as pd
import numpy as np
from typing import Optional

app = FastAPI()

# Mount static files and templates
templates = Jinja2Templates(directory="templates")

# Generate datasets
def generate_datasets():
    """Generate 500+ products dataset for each category"""
    np.random.seed(42)
    
    # Laptop Dataset
    laptop_brands = ['Dell', 'HP', 'Lenovo', 'Apple', 'Asus', 'Acer', 'MSI', 'Razer']
    laptop_processors = ['Intel i3', 'Intel i5', 'Intel i7', 'Intel i9', 'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7', 'AMD Ryzen 9', 'Apple M1', 'Apple M2']
    laptop_ram = [4, 8, 16, 32, 64]
    laptop_storage = [256, 512, 1024, 2048]
    laptop_screen = [13.3, 14, 15.6, 17.3]
    laptop_purpose = ['Gaming', 'Business', 'Student', 'Professional', 'General Use']
    
    laptops = []
    for i in range(120):
        laptops.append({
            'Product_ID': f'LAP{i+1:03d}',
            'Brand': np.random.choice(laptop_brands),
            'Processor': np.random.choice(laptop_processors),
            'RAM_GB': np.random.choice(laptop_ram),
            'Storage_GB': np.random.choice(laptop_storage),
            'Screen_Size': np.random.choice(laptop_screen),
            'Purpose': np.random.choice(laptop_purpose),
            'Price': np.random.randint(30000, 200000),
            'Rating': round(np.random.uniform(3.5, 5.0), 1)
        })
    laptop_df = pd.DataFrame(laptops)
    
    # Phone Dataset
    phone_brands = ['Samsung', 'Apple', 'OnePlus', 'Xiaomi', 'Oppo', 'Vivo', 'Realme', 'Google']
    phone_ram = [4, 6, 8, 12, 16]
    phone_storage = [64, 128, 256, 512, 1024]
    phone_battery = [4000, 4500, 5000, 5500, 6000]
    phone_camera = ['12MP', '48MP', '64MP', '108MP', '200MP']
    
    phones = []
    for i in range(120):
        phones.append({
            'Product_ID': f'PHN{i+1:03d}',
            'Brand': np.random.choice(phone_brands),
            'RAM_GB': np.random.choice(phone_ram),
            'Storage_GB': np.random.choice(phone_storage),
            'Battery_mAh': np.random.choice(phone_battery),
            'Camera': np.random.choice(phone_camera),
            'Price': np.random.randint(10000, 150000),
            'Rating': round(np.random.uniform(3.5, 5.0), 1)
        })
    phone_df = pd.DataFrame(phones)
    
    # TV Dataset
    tv_brands = ['Samsung', 'LG', 'Sony', 'Mi', 'OnePlus', 'TCL', 'Panasonic']
    tv_sizes = [32, 43, 50, 55, 65, 75, 85]
    tv_types = ['LED', 'QLED', 'OLED', 'NanoCell']
    tv_resolution = ['HD', 'Full HD', '4K', '8K']
    
    tvs = []
    for i in range(100):
        tvs.append({
            'Product_ID': f'TV{i+1:03d}',
            'Brand': np.random.choice(tv_brands),
            'Screen_Size': np.random.choice(tv_sizes),
            'Type': np.random.choice(tv_types),
            'Resolution': np.random.choice(tv_resolution),
            'Smart_TV': np.random.choice(['Yes', 'No']),
            'Price': np.random.randint(15000, 300000),
            'Rating': round(np.random.uniform(3.5, 5.0), 1)
        })
    tv_df = pd.DataFrame(tvs)
    
    # Camera Dataset
    camera_brands = ['Canon', 'Nikon', 'Sony', 'Fujifilm', 'Panasonic', 'Olympus']
    camera_types = ['DSLR', 'Mirrorless', 'Point & Shoot', 'Action Camera']
    camera_mp = [16, 20, 24, 32, 45, 50]
    
    cameras = []
    for i in range(80):
        cameras.append({
            'Product_ID': f'CAM{i+1:03d}',
            'Brand': np.random.choice(camera_brands),
            'Type': np.random.choice(camera_types),
            'Megapixels': np.random.choice(camera_mp),
            'Video_Quality': np.random.choice(['1080p', '4K', '6K', '8K']),
            'Price': np.random.randint(25000, 500000),
            'Rating': round(np.random.uniform(3.5, 5.0), 1)
        })
    camera_df = pd.DataFrame(cameras)
    
    # Headphones Dataset
    headphone_brands = ['Sony', 'Bose', 'JBL', 'Sennheiser', 'Apple', 'Samsung', 'Boat']
    headphone_types = ['Over-Ear', 'On-Ear', 'In-Ear', 'Earbuds']
    
    headphones = []
    for i in range(100):
        headphones.append({
            'Product_ID': f'HP{i+1:03d}',
            'Brand': np.random.choice(headphone_brands),
            'Type': np.random.choice(headphone_types),
            'Noise_Cancelling': np.random.choice(['Yes', 'No']),
            'Wireless': np.random.choice(['Yes', 'No']),
            'Battery_Hours': np.random.randint(10, 50) if np.random.random() > 0.3 else 0,
            'Price': np.random.randint(1000, 50000),
            'Rating': round(np.random.uniform(3.5, 5.0), 1)
        })
    headphone_df = pd.DataFrame(headphones)
    
    return {
        'laptops': laptop_df,
        'phones': phone_df,
        'tvs': tv_df,
        'cameras': camera_df,
        'headphones': headphone_df
    }

# Generate datasets on startup
datasets = generate_datasets()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with product categories"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/laptops", response_class=HTMLResponse)
async def laptops_page(request: Request):
    """Laptop filtering page"""
    df = datasets['laptops']
    filters = {
        'brands': sorted(df['Brand'].unique().tolist()),
        'processors': sorted(df['Processor'].unique().tolist()),
        'rams': sorted(df['RAM_GB'].unique().tolist()),
        'storages': sorted(df['Storage_GB'].unique().tolist()),
        'purposes': sorted(df['Purpose'].unique().tolist())
    }
    return templates.TemplateResponse("laptops.html", {
        "request": request,
        "filters": filters
    })

@app.post("/laptops/recommend", response_class=HTMLResponse)
async def recommend_laptops(
    request: Request,
    brand: Optional[str] = Form(None),
    processor: Optional[str] = Form(None),
    ram: Optional[int] = Form(None),
    storage: Optional[int] = Form(None),
    purpose: Optional[str] = Form(None),
    price_range: Optional[str] = Form(None)
):
    """Get laptop recommendations based on filters"""
    df = datasets['laptops'].copy()
    
    if brand and brand != "All":
        df = df[df['Brand'] == brand]
    if processor and processor != "All":
        df = df[df['Processor'] == processor]
    if ram and ram != "All":
        df = df[df['RAM_GB'] == int(ram)]
    if storage and storage != "All":
        df = df[df['Storage_GB'] == int(storage)]
    if purpose and purpose != "All":
        df = df[df['Purpose'] == purpose]
    
    if price_range and price_range != "All":
        if price_range == "Under 50k":
            df = df[df['Price'] < 50000]
        elif price_range == "50k-100k":
            df = df[(df['Price'] >= 50000) & (df['Price'] < 100000)]
        elif price_range == "100k-150k":
            df = df[(df['Price'] >= 100000) & (df['Price'] < 150000)]
        elif price_range == "Above 150k":
            df = df[df['Price'] >= 150000]
    
    df = df.sort_values('Rating', ascending=False).head(20)
    products = df.to_dict('records')
    
    return templates.TemplateResponse("results.html", {
        "request": request,
        "products": products,
        "count": len(products),
        "category": "Laptops"
    })

@app.get("/phones", response_class=HTMLResponse)
async def phones_page(request: Request):
    """Phone filtering page"""
    df = datasets['phones']
    filters = {
        'brands': sorted(df['Brand'].unique().tolist()),
        'rams': sorted(df['RAM_GB'].unique().tolist()),
        'storages': sorted(df['Storage_GB'].unique().tolist()),
        'cameras': sorted(df['Camera'].unique().tolist())
    }
    return templates.TemplateResponse("phones.html", {
        "request": request,
        "filters": filters
    })

@app.post("/phones/recommend", response_class=HTMLResponse)
async def recommend_phones(
    request: Request,
    brand: Optional[str] = Form(None),
    ram: Optional[int] = Form(None),
    storage: Optional[int] = Form(None),
    camera: Optional[str] = Form(None),
    price_range: Optional[str] = Form(None)
):
    """Get phone recommendations based on filters"""
    df = datasets['phones'].copy()
    
    if brand and brand != "All":
        df = df[df['Brand'] == brand]
    if ram and ram != "All":
        df = df[df['RAM_GB'] == int(ram)]
    if storage and storage != "All":
        df = df[df['Storage_GB'] == int(storage)]
    if camera and camera != "All":
        df = df[df['Camera'] == camera]
    
    if price_range and price_range != "All":
        if price_range == "Under 20k":
            df = df[df['Price'] < 20000]
        elif price_range == "20k-50k":
            df = df[(df['Price'] >= 20000) & (df['Price'] < 50000)]
        elif price_range == "50k-100k":
            df = df[(df['Price'] >= 50000) & (df['Price'] < 100000)]
        elif price_range == "Above 100k":
            df = df[df['Price'] >= 100000]
    
    df = df.sort_values('Rating', ascending=False).head(20)
    products = df.to_dict('records')
    
    return templates.TemplateResponse("results.html", {
        "request": request,
        "products": products,
        "count": len(products),
        "category": "Phones"
    })

@app.get("/tvs", response_class=HTMLResponse)
async def tvs_page(request: Request):
    """TV filtering page"""
    df = datasets['tvs']
    filters = {
        'brands': sorted(df['Brand'].unique().tolist()),
        'sizes': sorted(df['Screen_Size'].unique().tolist()),
        'types': sorted(df['Type'].unique().tolist()),
        'resolutions': ['HD', 'Full HD', '4K', '8K']
    }
    return templates.TemplateResponse("tvs.html", {
        "request": request,
        "filters": filters
    })

@app.post("/tvs/recommend", response_class=HTMLResponse)
async def recommend_tvs(
    request: Request,
    brand: Optional[str] = Form(None),
    size: Optional[int] = Form(None),
    tv_type: Optional[str] = Form(None),
    resolution: Optional[str] = Form(None),
    smart_tv: Optional[str] = Form(None),
    price_range: Optional[str] = Form(None)
):
    """Get TV recommendations based on filters"""
    df = datasets['tvs'].copy()
    
    if brand and brand != "All":
        df = df[df['Brand'] == brand]
    if size and size != "All":
        df = df[df['Screen_Size'] == int(size)]
    if tv_type and tv_type != "All":
        df = df[df['Type'] == tv_type]
    if resolution and resolution != "All":
        df = df[df['Resolution'] == resolution]
    if smart_tv and smart_tv != "All":
        df = df[df['Smart_TV'] == smart_tv]
    
    if price_range and price_range != "All":
        if price_range == "Under 30k":
            df = df[df['Price'] < 30000]
        elif price_range == "30k-70k":
            df = df[(df['Price'] >= 30000) & (df['Price'] < 70000)]
        elif price_range == "70k-150k":
            df = df[(df['Price'] >= 70000) & (df['Price'] < 150000)]
        elif price_range == "Above 150k":
            df = df[df['Price'] >= 150000]
    
    df = df.sort_values('Rating', ascending=False).head(20)
    products = df.to_dict('records')
    
    return templates.TemplateResponse("results.html", {
        "request": request,
        "products": products,
        "count": len(products),
        "category": "TVs"
    })

@app.get("/cameras", response_class=HTMLResponse)
async def cameras_page(request: Request):
    """Camera filtering page"""
    df = datasets['cameras']
    filters = {
        'brands': sorted(df['Brand'].unique().tolist()),
        'types': sorted(df['Type'].unique().tolist()),
        'megapixels': sorted(df['Megapixels'].unique().tolist()),
        'video_qualities': ['1080p', '4K', '6K', '8K']
    }
    return templates.TemplateResponse("cameras.html", {
        "request": request,
        "filters": filters
    })

@app.post("/cameras/recommend", response_class=HTMLResponse)
async def recommend_cameras(
    request: Request,
    brand: Optional[str] = Form(None),
    camera_type: Optional[str] = Form(None),
    megapixels: Optional[int] = Form(None),
    video_quality: Optional[str] = Form(None),
    price_range: Optional[str] = Form(None)
):
    """Get camera recommendations based on filters"""
    df = datasets['cameras'].copy()
    
    if brand and brand != "All":
        df = df[df['Brand'] == brand]
    if camera_type and camera_type != "All":
        df = df[df['Type'] == camera_type]
    if megapixels and megapixels != "All":
        df = df[df['Megapixels'] == int(megapixels)]
    if video_quality and video_quality != "All":
        df = df[df['Video_Quality'] == video_quality]
    
    if price_range and price_range != "All":
        if price_range == "Under 50k":
            df = df[df['Price'] < 50000]
        elif price_range == "50k-150k":
            df = df[(df['Price'] >= 50000) & (df['Price'] < 150000)]
        elif price_range == "150k-300k":
            df = df[(df['Price'] >= 150000) & (df['Price'] < 300000)]
        elif price_range == "Above 300k":
            df = df[df['Price'] >= 300000]
    
    df = df.sort_values('Rating', ascending=False).head(20)
    products = df.to_dict('records')
    
    return templates.TemplateResponse("results.html", {
        "request": request,
        "products": products,
        "count": len(products),
        "category": "Cameras"
    })

@app.get("/headphones", response_class=HTMLResponse)
async def headphones_page(request: Request):
    """Headphone filtering page"""
    df = datasets['headphones']
    filters = {
        'brands': sorted(df['Brand'].unique().tolist()),
        'types': sorted(df['Type'].unique().tolist())
    }
    return templates.TemplateResponse("headphones.html", {
        "request": request,
        "filters": filters
    })

@app.post("/headphones/recommend", response_class=HTMLResponse)
async def recommend_headphones(
    request: Request,
    brand: Optional[str] = Form(None),
    headphone_type: Optional[str] = Form(None),
    noise_cancelling: Optional[str] = Form(None),
    wireless: Optional[str] = Form(None),
    price_range: Optional[str] = Form(None)
):
    """Get headphone recommendations based on filters"""
    df = datasets['headphones'].copy()
    
    if brand and brand != "All":
        df = df[df['Brand'] == brand]
    if headphone_type and headphone_type != "All":
        df = df[df['Type'] == headphone_type]
    if noise_cancelling and noise_cancelling != "All":
        df = df[df['Noise_Cancelling'] == noise_cancelling]
    if wireless and wireless != "All":
        df = df[df['Wireless'] == wireless]
    
    if price_range and price_range != "All":
        if price_range == "Under 5k":
            df = df[df['Price'] < 5000]
        elif price_range == "5k-15k":
            df = df[(df['Price'] >= 5000) & (df['Price'] < 15000)]
        elif price_range == "15k-30k":
            df = df[(df['Price'] >= 15000) & (df['Price'] < 30000)]
        elif price_range == "Above 30k":
            df = df[df['Price'] >= 30000]
    
    df = df.sort_values('Rating', ascending=False).head(20)
    products = df.to_dict('records')
    
    return templates.TemplateResponse("results.html", {
        "request": request,
        "products": products,
        "count": len(products),
        "category": "Headphones"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)