### truth_layer.py
"""
Truth Layer: Analyzes perspectives and biases in event narratives.
"""

def analyze_truth(narratives):
    """
    Analyze multiple narratives to identify perspectives and biases.

    :param narratives: A dictionary with keys as narrative sources (e.g., 'Government', 'Media')
                      and values as the narrative text.
    :return: A structured overview of perspectives and identified biases.
    """
    results = {}

    for source, narrative in narratives.items():
        perspective = analyze_perspective(narrative)
        bias = detect_bias(narrative)
        results[source] = {
            "perspective": perspective,
            "bias": bias
        }

    return results

def analyze_perspective(narrative):
    """
    Extract the main perspective from a narrative.

    :param narrative: The text of the narrative.
    :return: A summary of the perspective.
    """
    # Placeholder for perspective analysis logic
    return f"Summary of perspective for narrative: {narrative[:50]}..."

def detect_bias(narrative):
    """
    Detect biases in a narrative.

    :param narrative: The text of the narrative.
    :return: A list of identified biases.
    """
    # Placeholder for bias detection logic
    biases = []

    if "agenda" in narrative.lower():
        biases.append("Potential hidden agenda detected")
    if "exclusive" in narrative.lower():
        biases.append("Selective reporting detected")

    return biases

if __name__ == "__main__":
    sample_narratives = {
        "Government": "The government narrative focuses on stability and order.",
        "Media": "Exclusive coverage reveals potential government agendas.",
        "Public": "The public narrative highlights concerns about freedom and transparency."
    }

    analysis_results = analyze_truth(sample_narratives)

    for source, result in analysis_results.items():
        print(f"Source: {source}")
        print(f"  Perspective: {result['perspective']}")
        print(f"  Biases: {', '.join(result['bias']) if result['bias'] else 'None'}")
