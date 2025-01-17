"""
Example Application: Demonstrates the integration of all layers in the framework.

This script:
1. Loads API credentials from the config.json file.
2. Fetches narrative data (currently static but can integrate with APIs).
3. Analyzes the data using the Truth Layer for perspectives and biases.
"""

import json
from code.truth_layer import analyze_truth

# Load API credentials from config.json
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def fetch_live_data():
    # Placeholder: Add API integration for fetching live data
    # For now, this will use static narratives
    return {
        "Government": "The government narrative focuses on stability and order.",
        "Media": "Exclusive coverage reveals potential government agendas.",
        "Public": "The public narrative highlights concerns about freedom and transparency."
    }

if __name__ == "__main__":
    try:
        # Load configuration
        config = load_config()

        # Fetch narratives (static or from APIs)
        narratives = fetch_live_data()

        # Analyze the narratives
        result = analyze_truth(narratives)

        # Print results
        print("Analysis Results:")
        for source, details in result.items():
            print(f"{source}: {details}")

    except FileNotFoundError:
        print("Error: 'config.json' not found. Please create and configure the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
