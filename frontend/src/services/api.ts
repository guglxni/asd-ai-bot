export interface AssessmentResponse {
  message: string;
  assessmentData?: any;
}

class ApiService {
  private baseUrl = 'http://localhost:8000/api';

  async startAssessment(ageMonths: number): Promise<AssessmentResponse> {
    const response = await fetch(`${this.baseUrl}/assessment/start`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ age_months: ageMonths }),
    });
    return response.json();
  }

  async processResponse(message: string, context: any): Promise<AssessmentResponse> {
    const response = await fetch(`${this.baseUrl}/assessment/process`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message, context }),
    });
    return response.json();
  }
}

export const apiService = new ApiService(); 