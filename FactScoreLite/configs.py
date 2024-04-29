from dataclasses import dataclass
from pathlib import Path

data_path = Path(__file__).parent / "data"


@dataclass
class FactScoreConfig:
    # Path to the data file within the package
    atomic_facts_demons_path: str = data_path / "atomic_facts_demons.json"

    fact_scorer_demons_path: str = data_path / "fact_scorer_demons.json"

    # OpenAI API
    max_tokens: int = 1024

    temp: float = 0.7

    model_name: str = "gpt-4-turbo-preview"

    # Database path
    facts_db_path: str = "facts.json"

    decisions_db_path: str = "decisions.json"

    # Metric calculation
    gamma: int = 10 # A penalty is applied to the score if the number of atomic facts is lower than gamma


