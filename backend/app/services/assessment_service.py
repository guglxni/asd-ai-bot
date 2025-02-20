from app.models.developmental_metrics import AssessmentMetrics, DevelopmentalArea
from app.models.rl_model import RLAgent
from app.services.llm_service import LLMService
from typing import Dict, List, Optional
import numpy as np

class AssessmentService:
    def __init__(self):
        self.metrics = AssessmentMetrics()
        self.state_size = 512  # Increased for more context
        self.action_size = self._calculate_action_size()
        self.rl_agent = RLAgent(self.state_size, self.action_size)
        self.llm_service = LLMService()
        
        # Age groups and their corresponding questions
        self.age_groups = {
            "0-6": self._get_0_6_months_questions(),
            "6-12": self._get_6_12_months_questions(),
            "12-18": self._get_12_18_months_questions(),
            "18-24": self._get_18_24_months_questions(),
            "24-30": self._get_24_30_months_questions(),
            "30-36": self._get_30_36_months_questions()
        }
    
    async def start_conversation(self, age_months: int) -> Dict:
        """
        Start the assessment conversation with an engaging opener
        """
        age_group = self._get_age_group(age_months)
        area = self._select_initial_area(age_months)
        milestone = self.metrics.milestones[age_group][area]
        
        return {
            "message": self._generate_conversation_starter(milestone),
            "area": area,
            "milestone": milestone.milestone
        }
    
    async def process_response(self, message: str, context: Dict) -> Dict:
        """
        Process parent's response and generate follow-up
        """
        # Analyze response using NLP
        sentiment = self._analyze_sentiment(message)
        indicators = self._extract_indicators(message, context["milestone"])
        
        # Update assessment scores
        self._update_assessment_scores(context["area"], indicators)
        
        # Generate response using local LLM
        llm_response = await self.llm_service.generate_response(
            message=message,
            context=context
        )
        
        return {
            "message": llm_response,
            "area": context["area"],
            "milestone": context["milestone"],
            "assessmentData": self._get_assessment_data()
        }
    
    async def generate_cddc_chart(self, assessment_data: Dict) -> Dict:
        """
        Generate CDDC chart data
        """
        chart_data = {
            "labels": list(DevelopmentalArea),
            "datasets": [
                {
                    "label": "Current Development",
                    "data": self._calculate_development_scores(assessment_data),
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "borderColor": "rgba(75, 192, 192, 1)",
                    "borderWidth": 1
                },
                {
                    "label": "Expected Development",
                    "data": self._get_expected_scores(assessment_data["age_months"]),
                    "backgroundColor": "rgba(54, 162, 235, 0.2)",
                    "borderColor": "rgba(54, 162, 235, 1)",
                    "borderWidth": 1
                }
            ]
        }
        
        return chart_data
    
    def get_next_question(self, age_months: int, previous_responses: List[Dict]) -> Dict:
        """
        Get the next question based on the child's age and previous responses
        """
        age_group = self._get_age_group(age_months)
        state = self._create_state(previous_responses)
        question_idx = self.rl_agent.select_question(state)
        
        return self.age_groups[age_group][question_idx]
    
    def calculate_risk_score(self, responses: List[Dict]) -> float:
        """
        Calculate autism risk score based on responses
        """
        # Implement risk score calculation logic
        pass
    
    def _get_age_group(self, age_months: int) -> str:
        """
        Determine the age group based on months
        """
        if age_months <= 6:
            return "0-6"
        elif age_months <= 12:
            return "6-12"
        elif age_months <= 18:
            return "12-18"
        elif age_months <= 24:
            return "18-24"
        elif age_months <= 30:
            return "24-30"
        else:
            return "30-36"
    
    def _create_state(self, previous_responses: List[Dict]) -> np.ndarray:
        """
        Create state vector from previous responses
        """
        # Implement state creation logic
        pass 