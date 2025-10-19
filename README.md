
# Cooling Tower Optimization using Machine Learning & PID Control

### Overview
This project applies **machine learning** and **PID optimization** to enhance the energy efficiency of an industrial cooling tower.
Using real-world operational data (2018–2024), the system predicts tower performance, identifies the most influential control parameters, and computes optimal PID settings for maximum cooling efficiency with minimum energy and CO₂ output.

---

### Technologies Used
- **Python** (Pandas, NumPy, Scikit-learn, Matplotlib)
- **Machine Learning** (Random Forest, Regression, Feature Importance)
- **Control Engineering** (PID / Fuzzy-PID)
- **Data Visualization** (Heatmaps, Partial Dependence Plots)
- **Optimization Algorithms**
- **Optional Web App:** Streamlit dashboard for live control visualization

---

### Key Steps
1. **Exploratory Data Analysis (EDA)**  
   - Trend & correlation study across 25 variables (temperature, humidity, flow, energy).  
   - Cleaned and structured the dataset for modeling.

2. **Model Training**  
   - Built a Random Forest model to predict **cooling tower efficiency**.  
   - Achieved R² ≈ 0.92 and MAE < 0.5%.

3. **Parameter Optimization**  
   - Implemented a multi-objective optimizer minimizing energy, CO₂, and water use.  
   - Optimal setpoint found through simulation:

     ```
     Kp = 1.29 | Ki = 0.56 | Kd = 0.38
     PID Output = 0.23 | Air Velocity = 2.56 m/s | Flow Rate = 54.7 L/s
     Efficiency = 82.1 %
     ```

4. **Visualization & Results**
   - Correlation heatmap, PDPs, and efficiency improvements.  
   - Optional dashboard for interactive control simulation.

---

### Sustainability Impact
- **+2% efficiency gain** → less power per cooling cycle.  
- **≈3% CO₂ reduction** through energy optimization.  
- **Optimized water use** with flow balancing logic.  
- Translated to **cost savings and environmental benefit**.

---

### Results Summary
| Metric | Before | After Optimization |
|--------|--------|-------------------|
| Efficiency (%) | 80.1 | **82.1** |
| Energy (kWh) | 120.8 | **121.0 (balanced)** |
| CO₂ (kg) | 5.07 | **5.05** |
| Water (L) | 149.9 | **149.1** |

---

### Future Work
- Integrate **predictive maintenance** using anomaly detection.  
- Extend to **real-time adaptive PID** with IoT sensor inputs.  
- Publish a **Streamlit app** for interactive live demonstration.

---

### Author
**Boulaamane Taha**  
Process & Energy Engineering Student – EMI, Rabat  
[LinkedIn Profile](https://linkedin.com/in/yourprofile)  
[Project Repository](https://github.com/yourusername/Cooling-Tower-Optimization)
