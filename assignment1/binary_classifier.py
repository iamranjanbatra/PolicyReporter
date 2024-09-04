from typing import List, Tuple, Optional

# Define the data structure type for clarity
ThresholdData = List[Tuple[float, int, int, int, int]]

def find_best_threshold(data: ThresholdData) -> Optional[float]:
    """
    Find the best threshold that yields a recall >= 0.9.
    
    :param data: List of tuples containing threshold and confusion matrix values
    :return: The best threshold, or None if no threshold meets the criteria
    """
    best_threshold = None
    best_precision = 0

    for threshold, tp, tn, fp, fn in data:
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        if recall >= 0.9:
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            
            if precision > best_precision:
                best_precision = precision
                best_threshold = threshold

    return best_threshold
