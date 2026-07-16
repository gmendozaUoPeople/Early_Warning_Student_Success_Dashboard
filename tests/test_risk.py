from risk import calculate_risk, get_recommendation


# -----------------------
# Risk Level Tests
# -----------------------

def test_high_risk_low_attendance():
    assert calculate_risk(75, 90) == "High"


def test_high_risk_low_grade():
    assert calculate_risk(95, 65) == "High"


def test_moderate_risk_attendance():
    assert calculate_risk(85, 90) == "Moderate"


def test_moderate_risk_grade():
    assert calculate_risk(95, 75) == "Moderate"


def test_low_risk():
    assert calculate_risk(95, 92) == "Low"


# -----------------------
# Recommendation Tests
# -----------------------

def test_high_recommendation():
    assert get_recommendation("High") == \
        "Schedule counselor meeting and assign tutoring."


def test_moderate_recommendation():
    assert get_recommendation("Moderate") == \
        "Monitor progress and contact parents if needed."


def test_low_recommendation():
    assert get_recommendation("Low") == \
        "Continue regular academic monitoring."