### origin_layer.py
"""
Origin Layer: Traces historical contexts and unintended consequences.
"""

def analyze_origins(event_data):
    """
    Analyze the origins and historical context of an event.

    :param event_data: A dictionary containing key details about the event.
                       Expected keys: ['description', 'history', 'actions']
    :return: A structured overview of origins and unintended consequences.
    """
    origins = trace_historical_context(event_data.get('history', []))
    consequences = identify_unintended_consequences(event_data.get('actions', []))

    return {
        "origins": origins,
        "unintended_consequences": consequences
    }

def trace_historical_context(history):
    """
    Trace historical events leading to the current scenario.

    :param history: A list of historical events.
    :return: A summary of historical context.
    """
    if not history:
        return "No historical data provided."

    context = "Historical Context:\n"
    for event in history:
        context += f"- {event}\n"

    return context

def identify_unintended_consequences(actions):
    """
    Identify unintended consequences of prior actions.

    :param actions: A list of actions taken during the event timeline.
    :return: A list of unintended consequences.
    """
    consequences = []

    for action in actions:
        if "military" in action.lower():
            consequences.append("Increased conflict due to military intervention.")
        if "sanction" in action.lower():
            consequences.append("Economic instability caused by sanctions.")
        if "negotiation" in action.lower():
            consequences.append("Delayed resolution due to prolonged negotiations.")

    return consequences or ["No unintended consequences identified."]

if __name__ == "__main__":
    sample_event_data = {
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

    analysis_results = analyze_origins(sample_event_data)

    print("Origins:")
    print(analysis_results["origins"])
    print("\nUnintended Consequences:")
    for consequence in analysis_results["unintended_consequences"]:
        print(f"- {consequence}")
