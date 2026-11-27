from dataclasses import dataclass


@dataclass
class Question:
    id: int
    value: int
    answer: str
    question: str
    positionData: str
