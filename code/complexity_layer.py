### complexity_layer.py
"""
Complexity Layer: Maps interdependencies and feedback loops in event dynamics.
"""

def analyze_complexity(entities, interactions):
    """
    Analyze interdependencies and feedback loops between entities.

    :param entities: A list of entities involved in the event.
    :param interactions: A list of interactions between these entities.
    :return: A map of interdependencies and identified feedback loops.
    """
    dependency_map = map_interdependencies(entities, interactions)
    feedback_loops = detect_feedback_loops(interactions)

    return {
        "dependency_map": dependency_map,
        "feedback_loops": feedback_loops
    }

def map_interdependencies(entities, interactions):
    """
    Create a map of interdependencies between entities based on interactions.

    :param entities: A list of entities.
    :param interactions: A list of interactions between entities.
    :return: A dictionary representing the dependency map.
    """
    dependency_map = {entity: [] for entity in entities}

    for interaction in interactions:
        source, target = interaction.get("source"), interaction.get("target")
        if source in entities and target in entities:
            dependency_map[source].append(target)

    return dependency_map

def detect_feedback_loops(interactions):
    """
    Detect feedback loops in the interactions.

    :param interactions: A list of interactions between entities.
    :return: A list of identified feedback loops.
    """
    feedback_loops = []

    for interaction in interactions:
        source, target = interaction.get("source"), interaction.get("target")
        if source == target:
            feedback_loops.append(f"Self-loop detected for entity: {source}")

    return feedback_loops or ["No feedback loops detected."]

if __name__ == "__main__":
    sample_entities = ["Government", "Rebels", "International Community"]

    sample_interactions = [
        {"source": "Government", "target": "Rebels", "type": "conflict"},
        {"source": "Rebels", "target": "Government", "type": "retaliation"},
        {"source": "International Community", "target": "Government", "type": "sanction"},
        {"source": "Government", "target": "Government", "type": "policy change"}
    ]

    analysis_results = analyze_complexity(sample_entities, sample_interactions)

    print("Dependency Map:")
    for entity, dependencies in analysis_results["dependency_map"].items():
        print(f"{entity}: {', '.join(dependencies) if dependencies else 'None'}")

    print("\nFeedback Loops:")
    for loop in analysis_results["feedback_loops"]:
        print(f"- {loop}")
