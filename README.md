# Illini Popcorn: PlantFit

**Event:** Precision Digital Agriculture Hackathon 2026 
**Track:** Smart Crops 
**Theme:** Plant Water Stress and Precision Irrigation

**Team Member**

Ximin Pian - xpiao2@illinois.edu, UIUC, (PhD candidate in CEE)

Priyal Maniar - priyalm2@illinois.edu, UIUC, (MSIM’26 Grad Student)

Prisha Singhania - pds4@illinois.edu, UIUC, (MSIM’26 Grad Student)

Yuyang Liu - yuyang19@illinois.edu, UIUC, (MSIM’27 Grad Student)

**Problem Statement:** Crops are thirsty and we often know too late. This causes great loss in productivity. We integrate a minimum invasive crop sap flow sensor to see the “pulse of the crop” and combine it with environmental data and forecasts to provide irrigation advice.

**PlantFit** is a data-driven crop management system designed to optimize irrigation schedules using real-time weather data, plant sap flow data,time series forecasting and predictive modeling. This project integrates atmospheric forecasts with plant-specific metrics to ensure efficient water usage and optimal growth for crops.

**Slides link**
[View Presentation](https://www.canva.com/design/DAHDUa_mb_k/wt2sLgOy3A5au5aAAXjsIw/view?utm_content=DAHDUa_mb_k&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h92986a0da3)


##  Key Features

- **Automated Irrigation Modeling:** Execute core agricultural logic via `run_irrigation_model.py` to calculate precise watering needs.
    
- **Weather Integration:** Processes 48-hour forecasts and historical precipitation data to adjust for upcoming environmental changes.
    
- **Zone Management:** Modular control for different field sectors, allowing for specialized treatment based on soil type or crop stage.
    
- **Baseline Calibration:** Utilizes a `trained_baseline.csv` to compare current field data against historical performance standards.
    
- **Visual Prototyping:** Includes an interactive interface (`plantfit_prototype.html`) for monitoring plant health.

## Data Sources

This project integrates diverse agricultural, meteorological, and geospatial datasets for Bondville, Illinois:

- **Satellite Imagery (NDVI):** Sentinel-2 Level-2A satellite imagery sourced via the Copernicus Browser, used to monitor vegetation health and density.
- **Weather Data:** Environmental Conditions data from the [NOAA SURFRAD Network (Bondville Station)](https://gml.noaa.gov/grad/surfrad/bondvill.html).
- **Precipitation Data:** Historical precipitation metrics from the [Illinois Water and Atmospheric Resources Monitoring (WARM) Program](https://warm.isws.illinois.edu/warm/datatype.asp).
- **Evapotranspiration (ET) Data:** Pulled via the **OpenET API** to measure water movement from the soil and plants into the atmosphere.
- **IoT Sensor Data (Simulated):** Represents readings from 2 sensors per plant (capturing 4 distinct data points each). To model the July–August yield window, this dataset was synthetically generated using seasonal variation patterns and time series forecasting. 
    * *Note: While currently using modeled data for the prototype, the pipeline is designed to ingest live, real-world sensor data to drive accurate, real-time predictions in deployment.*

 ##  Data Pipeline




- **Data Pipeline:** An NSFI-driven pipeline using satellite and sensor data to trigger real-time plant stress alerts.
![WhatsApp Image 2026-03-08 at 11 30 52](https://github.com/user-attachments/assets/e42a88eb-29e7-48b0-a4cf-febf000625bc)

---


##  Repository Structure

|**File / Folder**|**Function**|
|---|---|
|`data/`|Contains raw and processed datasets used in the project|
|`outputs/`|Generated files - figures and trained models|
|`prototypes/`|Web-based dashboard interface and product demo video|
|`scripts/`| Execution python files and modules|
|`.gitattributes`|Git configuration for path-specific attributes|
|`gitignore`|Specifies intentionally untracked files to ignore|
|`README.md`|Project overview and documents|
|`requirements.txt`|List of Python dependencies required for the system.|

---

##  Installation & Setup

### Prerequisites

- Python 3.8+
    
- Pip (Python package manager)
    

### Installation

1. **Clone the repository:**
    
    Bash
    
    ```
    git clone https://github.com/PriyalManiar/illini_popcorn.git
    cd illini_popcorn
    ```
    
2. **Install dependencies:**
    
    Bash
    
    ```
    pip install -r requirements.txt
    ```

3. **External API**
    API key was originally stored in the .env file but have also include it in the api_key file

---

##  Usage

The system is designed to be modular, allowing for both automated modeling and manual data adjustment.

### Running the Irrigation Model

To generate irrigation recommendations based on current forecasts and crop baselines, run the primary script:

Bash

```
python irrigation_model.py
```

### Data Customization

- **Forecast Adjustments:** You can manually update `mock_48hr_forecast.csv` with specific temperature or humidity data to simulate different environmental stress tests.
    
- **Model Calibration:** The `trained_baseline.csv` file serves as the ground truth for "healthy" crop behavior. Updating this allows the model to adapt to different corn hybrids.
    

### Web-based Dashboard Prototype

To view the conceptual UI for this system, open `plantfit_prototype.html` in any web browser. This dashboard provides a visual representation of soil moisture levels and plant health trends.

---

## 📄 License

This project is licensed under the **MIT License**
