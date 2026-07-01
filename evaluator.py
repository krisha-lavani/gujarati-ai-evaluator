from metrics import (
    gujarati_score,
    length_score,
    fluency_score,
    safety_score,
    roman_gujarati_score,
    hallucination_score,
    accuracy_score
)


def evaluate_response(response):
    
    score1 = gujarati_score(response)
    score2 = length_score(response)
    score3 = fluency_score(response)
    score4 = safety_score(response)
    score5 = roman_gujarati_score(response)
    score6 = hallucination_score(response)
    score7 = accuracy_score(response)

    weighted_total = (
        score1 * 1.5 +   # Gujarati
        score2 * 1 +     # Length
        score3 * 1.5 +   # Fluency
        score4 * 2 +     # Safety
        score5 * 1 +     # Roman Gujarati
        score6 * 3 +     # Hallucination
        score7 * 3       # Accuracy
    )

    result = {
        "Gujarati Score": score1,
        "Length Score": score2,
        "Fluency Score": score3,
        "Safety Score": score4,
        "Roman Gujarati Score": score5,
        "Hallucination Score": score6,
        "Accuracy Score": score7,
        "Weighted Score": weighted_total
    }

    return result