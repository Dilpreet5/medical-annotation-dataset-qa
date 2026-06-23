from core.qa_checks import detect_missing_labels
from core.qa_checks import validate_dataset


def calculate_health_score():
    # Placeholder for health score calculation logic
    # This function should compute and return the health score based on relevant metrics

    score = 100
    
    score = max(score, 0)
    score = min(score, 100)
    if detect_missing_labels():        #Missing Label Detection
        count = len(detect_missing_labels())
        score -= 5 * count
    if validate_dataset():              #Dataset Validation
        count = len(validate_dataset())
        score -= 3 * count
        
    return max(0, score)


def get_health_status(score):           #Health Status based on health score
    if score >=95:
        return "Excellent 🟢"
    elif score >=75:
        return "Good 🟡"
    elif score >=50:
        return "Fair 🟠"
    else:
        return "Poor 🔴"
    
    