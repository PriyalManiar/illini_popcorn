# Illini Popcorn: Precision Irrigation Management

**Illini Popcorn** is a data-driven crop management system designed to optimize irrigation schedules using real-time weather data, soil moisture tracking, and predictive modeling. This project integrates atmospheric forecasts with plant-specific metrics to ensure efficient water usage and optimal growth for popcorn crops.

## 🚀 Key Features

- **Automated Irrigation Modeling:** Execute core agricultural logic via `run_irrigation_model.py` to calculate precise watering needs.
    
- **Weather Integration:** Processes 48-hour forecasts and historical precipitation data to adjust for upcoming environmental changes.
    
- **Zone Management:** Modular control for different field sectors, allowing for specialized treatment based on soil type or crop stage.
    
- **Baseline Calibration:** Utilizes a `trained_baseline.csv` to compare current field data against historical performance standards.
    
- **Visual Prototyping:** Includes an interactive interface (`plantfit_prototype.html`) for monitoring system status and plant health.
    

---

## 📂 Repository Structure

|**File / Folder**|**Function**|
|---|---|
|`precipitation/`|Scripts for parsing and analyzing rainfall events.|
|`sap/`|Modules handling Soil-Plant-Atmosphere (SAP) sensor data.|
|`weather/`|API integrations for localized weather monitoring and forecasting.|
|`zone management/`|Logic for subdividing and managing specific agricultural plots.|
|`run_irrigation_model.py`|The main execution script that synthesizes data into recommendations.|
|`trained_baseline.csv`|Pre-calculated data used to calibrate the model's predictions.|
|`mock_48hr_forecast.csv`|Sample weather data for testing the model without live API calls.|
|`requirements.txt`|List of Python dependencies required for the system.|

---

## 🛠️ Installation & Setup

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
    

---

## 📈 Usage

The system is designed to be modular, allowing for both automated modeling and manual data adjustment.

### Running the Irrigation Model

To generate irrigation recommendations based on current forecasts and crop baselines, run the primary script:

Bash

```
python run_irrigation_model.py
```

### Data Customization

- **Forecast Adjustments:** You can manually update `mock_48hr_forecast.csv` with specific temperature or humidity data to simulate different environmental stress tests.
    
- **Model Calibration:** The `trained_baseline.csv` file serves as the ground truth for "healthy" crop behavior. Updating this allows the model to adapt to different corn hybrids.
    

### Web Dashboard Prototype

To view the conceptual UI for this system, open `plantfit_prototype.html` in any web browser. This dashboard provides a visual representation of soil moisture levels and plant health trends.

---

## 📄 License

This project is licensed under the **MIT License**
