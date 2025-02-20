from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel

class DevelopmentalArea(str, Enum):
    GROSS_MOTOR = "gross_motor"
    FINE_MOTOR = "fine_motor"
    ADL = "adaptive_daily_living"
    RECEPTIVE_LANGUAGE = "receptive_language"
    EXPRESSIVE_LANGUAGE = "expressive_language"
    COGNITIVE = "cognitive"
    SOCIAL_EMOTIONAL = "social_emotional"

class DevelopmentalMilestone(BaseModel):
    area: DevelopmentalArea
    age_range: str
    milestone: str
    questions: List[str]
    conversation_starters: List[str]
    follow_up_questions: List[str]
    indicators: List[str]

class AssessmentMetrics:
    def __init__(self):
        self.milestones = {
            "0-6": self._get_0_6_months_milestones(),
            "6-12": self._get_6_12_months_milestones(),
            "12-18": self._get_12_18_months_milestones(),
            "18-24": self._get_18_24_months_milestones(),
            "24-30": self._get_24_30_months_milestones(),
            "30-36": self._get_30_36_months_milestones()
        }

    def _get_0_6_months_milestones(self) -> Dict[DevelopmentalArea, DevelopmentalMilestone]:
        return {
            DevelopmentalArea.GROSS_MOTOR: DevelopmentalMilestone(
                area=DevelopmentalArea.GROSS_MOTOR,
                age_range="0-6",
                milestone="Eyes follow a moving object",
                questions=[
                    "How does your baby respond when you move toys in front of them?",
                    "Does your baby watch objects as they move across their field of vision?"
                ],
                conversation_starters=[
                    "Tell me about how your baby interacts with moving objects or toys.",
                    "What catches your baby's attention the most?"
                ],
                follow_up_questions=[
                    "Can you give me an example of when you noticed this?",
                    "How smooth is their eye movement when following objects?"
                ],
                indicators=[
                    "Smoothly follows moving objects",
                    "Shows interest in moving objects",
                    "Maintains eye contact with moving objects"
                ]
            ),
            # Add other areas similarly...
        } 