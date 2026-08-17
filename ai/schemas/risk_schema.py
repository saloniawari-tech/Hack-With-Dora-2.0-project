from pydantic import BaseModel
from typing import List


class RiskIssue(BaseModel):
    clause_number: str
    category: str
    risk_level: str
    title: str
    clause_text: str
    explanation: str
    recommendation: str


class RiskReport(BaseModel):
    overall_score: int
    overall_risk: str
    summary: str
    issues: List[RiskIssue]