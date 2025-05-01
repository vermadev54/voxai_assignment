# 📊 Contact Center Analytics Summary Report

Welcome to the **Contact Center Analytics Summary Report** repository! This project aims to analyze and enhance customer engagement and operational efficiency in contact centers through data-driven insights, machine learning, and visualization.

---

## 🔍 Overview

This repository contains a comprehensive analysis of a contact center's operations using synthetic data. The insights focus on critical areas like IVR navigation, call drop-offs, agent performance, customer sentiment, and bot failures. An interactive dashboard has also been built for real-time monitoring of key performance indicators (KPIs).

---

## 📂 Repository Structure

```plaintext
.
├── Summery_report.ipynb  # Jupyter Notebook with analysis and insights
├── data/                 # Directory for synthetic data (if applicable)
├── app.py             # Streamlit dashboard implementation
├── README.md             # Project overview and documentation
```

---

## 📈 Key Insights

1. **IVR Navigation**:
   - Most common path: `Start > Billing`, highlighting a need for billing-related assistance.
   - Higher drop-offs at early stages indicate user frustration or confusion.

2. **Agent Performance**:
   - Variability in **Average Handling Time (AHT)** and **First Call Resolution (FCR)**.
   - Top-performing agents achieved higher FCR and lower escalation rates.

3. **Customer Sentiment**:
   - Overall sentiment: 38.90% positive, 51.75% neutral, and 9.35% negative.
   - Calls ending in transfers/escalations often show worsened sentiment.

4. **Bot Failures**:
   - Leading causes: `no_match` and `no_input`.
   - Majority of live agent transfers stem from failed self-service attempts.

---

## 🛠️ Methodology

1. **Synthetic Data Generation**:
   - Simulated 2,000 calls with realistic features like IVR paths, durations, customer utterances, and sentiments.

2. **Data Preprocessing**:
   - Addressed missing values, standardized formats, and anonymized sensitive identifiers.

3. **Exploratory Data Analysis (EDA)**:
   - Visualized IVR paths, drop-offs, handling times, and transfer behavior.

4. **Natural Language Processing (NLP) & Machine Learning (ML)**:
   - Applied keyword extraction and clustering for intent analysis.
   - Sentiment analysis tracked emotional trends in customer utterances.

5. **Visualization**:
   - Built an interactive Streamlit dashboard with filters for agent, team, and date.

---

## 📊 Recommendations

1. **Improve IVR Routing**:
   - Redesign unclear paths (e.g., `Start > TechSupport`) to reduce drop-offs.
   - Introduce early clarification prompts.

2. **Optimize Bot Performance**:
   - Retrain NLU models with failed query patterns (`no_match`, `ambiguous_query`).
   - Adjust fallback confidence thresholds or escalate earlier to human agents.

3. **Enhance Agent Training**:
   - Focus on agents with high escalations and low FCR.
   - Leverage sentiment trends as coaching feedback.

4. **Refine Intent Analytics**:
   - Utilize detected topics to update FAQs and improve self-service options.

5. **Monitor & Scale**:
   - Deploy dashboards with real-time KPIs segmented by team, shift, and customer type.

---

## ⚙️ Tools & Technologies

- **Data Analysis**: Python, Pandas
- **Dashboarding**: Streamlit
- **NLP & ML**: Scikit-learn, NLTK
- **Visualization**: Matplotlib, Seaborn

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Required libraries: Pandas, NumPy, Scikit-learn, Streamlit, NLTK, Matplotlib, Seaborn

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/vermadev54/voxai_assignment.git
   cd voxai_assignment
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the Streamlit dashboard:
   ```bash
   streamlit run app.py
   ```

---

## 📬 Feedback & Contributions

Feedback, suggestions, and contributions are welcome! Please open an issue or submit a pull request for any improvements.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ✍️ Author

- **Vermadev54**  
GitHub Profile: [vermadev54](https://github.com/vermadev54)

---

Feel free to reach out for any further questions or collaboration opportunities! 🚀