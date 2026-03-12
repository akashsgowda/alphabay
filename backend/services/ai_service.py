import random


def analyze_image(image):

    """
    Simulates pothole severity detection.
    """

    severities = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

    severity = random.choice(severities)

    confidence = random.randint(70, 95)

    return {
        "severity": severity,
        "confidence": confidence,
        "incident_type": "pothole"
    }