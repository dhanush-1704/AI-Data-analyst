import json
import subprocess
from datetime import datetime


class AnalystMind:
    def __init__(self, metadata: dict, baseline_plan: dict):
        self.metadata = metadata
        self.baseline_plan = baseline_plan

        self.dataset_type = None
        self.analysis_strategy = None

        self.thoughts = []
        self.final_plan = {}
        self.executive_summary = []
        self.limitations = []

    def _call_llm(self, prompt: str) -> dict:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            capture_output=True,
            encoding="utf-8",
            errors="replace"
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        raw = result.stdout.strip()

        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            raise RuntimeError(f"Invalid JSON from LLM:\n{raw}")

    def think_and_decide(self) -> dict:
        prompt = f"""
You are a senior data analyst.

Your tasks:
1. Identify the dataset type
2. Decide the correct analysis strategy
3. Choose meaningful visualizations
4. Write executive-level insights
5. State limitations clearly

Rules:
- Respond ONLY in valid JSON
- No markdown
- No code

JSON FORMAT:
{{
  "dataset_type": string,
  "analysis_strategy": string,
  "thoughts": [string],
  "final_plan": {{
    "visualizations": [
      {{ "type": string, "column": string }}
    ],
    "statistics": [string],
    "notes": [string]
  }},
  "executive_summary": [string],
  "limitations": [string]
}}

DATASET METADATA:
{json.dumps(self.metadata, indent=2)}

BASELINE PLAN:
{json.dumps(self.baseline_plan, indent=2)}
"""

        response = self._call_llm(prompt)

        self.dataset_type = response.get("dataset_type")
        self.analysis_strategy = response.get("analysis_strategy")
        self.thoughts = response.get("thoughts", [])
        self.final_plan = response.get("final_plan", self.baseline_plan)
        self.executive_summary = response.get("executive_summary", [])
        self.limitations = response.get("limitations", [])

        return self.final_plan

    def write_report(self, path="reports/ai_insights.md"):
        lines = [
            "# AI Analyst Report",
            f"Generated on {datetime.now()}",
            "",
            f"## Dataset Type: {self.dataset_type}",
            f"## Analysis Strategy: {self.analysis_strategy}",
            "",
            "## Reasoning",
            *[f"- {t}" for t in self.thoughts],
            "",
            "## Executive Summary",
            *[f"- {s}" for s in self.executive_summary],
            "",
            "## Limitations",
            *[f"- {l}" for l in self.limitations],
        ]

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
