### main_example.py
"""
Example Application: Demonstrates the integration of all layers in the framework.
"""

from code.truth_layer import analyze_truth
from code.origin_layer import analyze_origins
from code.complexity_layer import analyze_complexity

def main():
    """
    Main function to demonstrate the Project RootSource framework.
    """
    # Step 1: Truth Layer - Perspectives and Biases
    print("=== Truth Layer Analysis ===")
    narratives = {
        "Government": "The government narrative focuses on stability and order.",
        "Media": "Exclusive coverage reveals potential government agendas.",
        "Public": "The public narrative highlights concerns about freedom and transparency."
    }
    truth_results = analyze_truth(narratives)

    for source, result in truth_results.items():
        print(f"Source: {source}")
        print(f"  Perspective: {result['perspective']}")
        print(f"  Biases: {', '.join(result['bias']) if result['bias'] else 'None'}")

    # Step 2: Origin Layer - Historical Context and Consequences
    print("\n=== Origin Layer Analysis ===")
    event_data = {
        "description": "A regional conflict with international involvement.",
        "history": [
            "Colonial boundaries created post-WW1.",
            "Economic sanctions imposed in 2005.",
            "Peace agreement signed in 2010 but failed."
        ],
        "actions": [
            "Military intervention by external powers.",
            "Imposition of new economic sanctions.",
            "Attempts at negotiation without consensus."
        ]
    }
    origin_results = analyze_origins(event_data)

    print("Origins:")
    print(origin_results["origins"])
    print("\nUnintended Consequences:")
    for consequence in origin_results["unintended_consequences"]:
        print(f"- {consequence}")

    # Step 3: Complexity Layer - Interdependencies and Feedback Loops
    print("\n=== Complexity Layer Analysis ===")
    entities = ["Government", "Rebels", "International Community"]
    interactions = [
        {"source": "Government", "target": "Rebels", "type": "conflict"},
        {"source": "Rebels", "target": "Government", "type": "retaliation"},
        {"source": "International Community", "target": "Government", "type": "sanction"},
        {"source": "Government", "target": "Government", "type": "policy change"}
    ]
    complexity_results = analyze_complexity(entities, interactions)

    print("Dependency Map:")
    for entity, dependencies in complexity_results["dependency_map"].items():
        print(f"{entity}: {', '.join(dependencies) if dependencies else 'None'}")

    print("\nFeedback Loops:")
    for loop in complexity_results["feedback_loops"]:
        print(f"- {loop}")

if __name__ == "__main__":
    main()
