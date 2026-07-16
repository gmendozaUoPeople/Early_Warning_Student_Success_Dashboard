def calculate_risk(attendance, average_grade):
    """
    Determines a student's academic risk level based on
    attendance and average overall grade.
    """

    if attendance < 80 or average_grade < 70:
        return "High"

    elif attendance < 90 or average_grade < 80:
        return "Moderate"

    else:
        return "Low"
    
def get_recommendation(risk_level):
    """
    Returns an intervention recommendation based on
    the student's calculated risk level.
    """

    if risk_level == "High":
        return "Schedule counselor meeting and assign tutoring."

    elif risk_level == "Moderate":
        return "Monitor progress and contact parents if needed."

    else:
        return "Continue regular academic monitoring."