from typing import List

def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    """  calcula o percentual de acerto """
    
    correct_predictions = 0
    for i in range(len(true_classes)):
        if true_classes[i] == predicted_classes[i]:
            correct_predictions += 1

    accuracy = correct_predictions / len(true_classes)

    return accuracy