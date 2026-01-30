# Silver Price Calculator & Silver Sales Dashboard 💎

A comprehensive Streamlit application for analyzing silver prices and regional consumption patterns in India.

## Features

### 1. Silver Price Calculator (5 Marks)
- **Weight Unit Selection**: Choose between grams or kilograms
- **Cost Calculation**: Calculate total cost based on weight and current price per gram
- **Currency Conversion**: Convert INR to USD, EUR, GBP, JPY, or AUD with real-time exchange rates
- **Historical Price Chart**: View silver price trends from 2000 onwards with interactive charts
- **Price Range Filters**: 
  - ≤ 20,000 INR/kg
  - 20,000 - 30,000 INR/kg
  - ≥ 30,000 INR/kg
  - All data combined

### 2. Silver Sales Dashboard (5 Marks)
- **State-wise Visualization**: Interactive map showing silver purchases across Indian states
- **Top 5 States Analysis**: Bar chart displaying the highest silver-purchasing states
- **Karnataka Monthly Trends**: Line chart showing seasonal patterns in silver purchases
- **Data Export**: Download state-wise data as CSV for further analysis

## Data Files

- `historical_silver_price.csv`: Monthly silver price data from 2000 to 2024 (INR/kg)
- `state_wise_silver_purchased_kg.csv`: State-wise silver purchase quantities in India

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory:**
```bash
cd /Users/slaven/Downloads/MCA/IIIrd SEM/APP/cia1
```

2. **Create a virtual environment (optional but recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required packages:**
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

```bash
streamlit run cia1.py
```

The application will open in your default browser at `http://localhost:8501`

### Alternative Run Methods

```bash
# With specific Python version
python3 -m streamlit run cia1.py

# With custom port
streamlit run cia1.py --server.port=8502
```

## Deployment Options

### Option 1: Deploy to Streamlit Cloud (Recommended)

1. **Create a GitHub Repository:**
   - Push your project files to GitHub
   - Ensure `requirements.txt` is included

2. **Connect to Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your GitHub repository and main file (`cia1.py`)
   - Click "Deploy"

3. **Share Your App:**
   - Once deployed, you'll get a public URL to share
   - App auto-updates when you push changes to GitHub

### Option 2: Deploy to Heroku

1. **Create `Procfile`:**
```
web: streamlit run --server.port=$PORT --server.address=0.0.0.0 cia1.py
```

2. **Create `setup.sh`:**
```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

3. **Deploy:**
```bash
heroku create your-app-name
git push heroku main
```

### Option 3: Deploy to AWS EC2

1. **Launch an EC2 instance** (Ubuntu 20.04)

2. **SSH into instance:**
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

3. **Install dependencies:**
```bash
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt
```

4. **Run the app:**
```bash
nohup streamlit run cia1.py --server.port=8501 &
```

5. **Access via:** `http://your-instance-ip:8501`

### Option 4: Deploy to Google Cloud Run

1. **Create `Dockerfile`:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "cia1.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

2. **Build and deploy:**
```bash
gcloud run deploy silver-dashboard \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## Application Features

### Silver Price Calculator Tab
- **Price Calculator**: Real-time cost calculation based on weight and price
- **Currency Conversion**: Multi-currency support with exchange rates
- **Weight Conversion**: Automatic conversion between grams and kilograms
- **Historical Trends**: Interactive line chart of silver prices over 24 years
- **Price Range Filters**: Filter data by specific price ranges

### Sales Dashboard Tabs
- **State Map**: Horizontal bar chart showing all states/UTs ranked by silver purchases
- **Top 5 States**: 
  - Maharashtra: 22,000 kg
  - Rajasthan: 19,800 kg
  - Andhra Pradesh: 18,500 kg
  - Tamil Nadu: 17,500 kg
  - Karnataka: 16,800 kg
  
- **Karnataka Analysis**:
  - Monthly trend visualization
  - Peak and low month identification
  - Monthly percentage breakdown
  - Statistical summary

- **Complete Data Table**:
  - All states ranked by purchases
  - Percentage contributions
  - CSV export functionality

## Usage Examples

### Example 1: Calculate Silver Cost
1. Navigate to "Silver Price Calculator"
2. Select weight unit: "Kilograms"
3. Enter weight: 5 kg
4. Enter price per gram: 75 INR
5. View total cost and conversions

### Example 2: Analyze Regional Sales
1. Go to "Sales Dashboard"
2. Check "Top 5 States" tab to see major buyers
3. View "State Map" for complete distribution
4. Explore "Karnataka Analysis" for monthly trends

### Example 3: Historical Price Analysis
1. In Price Calculator, open "Historical Chart" tab
2. View complete price trend since 2000
3. Use "Price Filters" to focus on specific ranges
4. Analyze price movements over time

## Technical Details

### Technologies Used
- **Frontend**: Streamlit (Python framework)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib
- **Geospatial**: GeoPandas
- **API Integration**: Requests

### Performance Optimizations
- Data caching with `@st.cache_data` decorator
- Efficient data filtering and aggregation
- Optimized visualizations with Plotly

## Requirements

See `requirements.txt` for complete list:
- streamlit
- pandas
- geopandas
- matplotlib
- plotly
- numpy
- requests
- Pillow

## Troubleshooting

### Issue: Module not found error
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Port already in use
```bash
streamlit run cia1.py --server.port=8502
```

### Issue: Slow data loading
- Clear cache: Delete `.streamlit` folder
- Restart the app

## Project Structure

```
cia1/
├── cia1.py                              # Main Streamlit application
├── historical_silver_price.csv          # Historical price data
├── state_wise_silver_purchased_kg.csv   # State-wise purchase data
├── requirements.txt                     # Python dependencies
└── README.md                            # This file
```

## Data Sources

- **Historical Silver Prices**: 2000-2024 monthly data (INR/kg)
- **State-wise Purchases**: Current year purchase records for 32 Indian states/UTs

## Future Enhancements

- [ ] Real-time silver price API integration
- [ ] Machine learning price prediction models
- [ ] Advanced geospatial visualization with actual India map
- [ ] User login and saved preferences
- [ ] Monthly data for all states (currently Karnataka only)
- [ ] Email alerts for price changes
- [ ] PDF report generation

## License

This project is created for educational purposes (CIA-1 Assessment).

## Contact & Support

For issues or questions, please contact the development team.

## Version History

- **v1.0** (Jan 2026): Initial release with all core features

---

**Last Updated**: January 30, 2026  
**Status**: Production Ready ✅
