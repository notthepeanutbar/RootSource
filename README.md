# **Project RootSource**

Welcome to **RootSource**, a modular framework designed to analyze complex events, uncover patterns, and identify origins and potential misinformation. This open-source framework is ideal for researchers, analysts, and developers aiming to explore the layers behind events and narratives.

---

## **Features**
1. **Layered Framework**:
   - **Truth Layer**: Analyze perspectives, biases, and narratives.
   - **Origin Layer**: Trace historical contexts and unintended consequences.
   - **Complexity Layer**: Map interdependencies and feedback loops.
2. **API Integration**:
   - Fetch live data from APIs like NewsAPI, Twitter/X, and Reddit.
   - Perform sentiment and dependency analysis using NLP APIs.
3. **Modular Design**:
   - Extendable to include additional layers or data sources.
   - Adaptable for different scenarios, from political analysis to marketing trends.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your_username/RootSource.git
cd RootSource
```

### **2. Install Dependencies**
Install required Python libraries:
```bash
pip install requests
```

### **3. Configure API Access**
Copy the `config_template.json` file, rename it to `config.json`, and fill in your API credentials:
```json
{
    "news_api_key": "your_newsapi_key_here",
    "twitter_api_key": "your_twitter_api_key_here",
    "twitter_api_secret": "your_twitter_api_secret_here",
    "reddit_api_key": "your_reddit_api_key_here",
    "google_nlp_key": "your_google_nlp_key_here",
    "openstreetmap_url": "https://api.openstreetmap.org"
}
```

### **4. Run Examples**
Start exploring the framework by running the example script:
```bash
python example_/main_example.py
```

The example script demonstrates:
1. How to load API credentials from `config.json`.
2. Fetching narrative data (static or via APIs, if configured).
3. Analyzing narratives for perspectives and biases using the Truth Layer.

---

## **Layers Overview**

### **Truth Layer**
- **Purpose**: Analyze perspectives and biases in event narratives.
- **Features**:
  - Accept multiple narrative inputs (e.g., government, media, public opinion).
  - Identify and categorize biases.
  - Output a structured overview of competing perspectives.
- **Example**:
  ```python
  from code.truth_layer import analyze_truth
  narratives = {
      "Government": "The government narrative focuses on stability and order.",
      "Media": "Exclusive coverage reveals potential government agendas.",
      "Public": "The public narrative highlights concerns about freedom and transparency."
  }
  result = analyze_truth(narratives)
  print(result)
  ```

### **Origin Layer**
- **Purpose**: Trace historical contexts and unintended consequences.
- **Features**:
  - Accept historical data inputs.
  - Perform root cause analysis.
  - Highlight unintended outcomes from key actions or decisions.
- **Example**:
  Coming soon!

### **Complexity Layer**
- **Purpose**: Map interdependencies and feedback loops.
- **Features**:
  - Analyze interactions between entities.
  - Visualize dependencies and feedback loops.
  - Provide insights into system dynamics.
- **Example**:
  Coming soon!

---

## **Folder Structure**

```
RootSource/
|— README.md
|— config_template.json  # Template for API credentials (user must rename to config.json)
|— code/
|    |— truth_layer.py
|    |— origin_layer.py
|    |— complexity_layer.py
|— example_/
|    |— main_example.py  # Demonstrates integration of all layers with API placeholders
```

---

## **What's Next?**
1. **Extend the Framework**:
   - Add more customizable layers and sublayers.
   - Enhance flexibility for domain-specific analyses.
2. **Enable Advanced Applications**:
   - Migrate the framework for real-time and large-scale scenarios.
3. **Possibility**:
   - Add visualization tools for mapping dependencies and feedback loops.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Submit a pull request with a detailed explanation.

---

## **License**
This is licensed under the MIT License. See the `LICENSE` file for more information.

---

## **Contact**
If you have any questions or suggestions, feel free to reach out via GitHub or x.com/notthepeanutbar
