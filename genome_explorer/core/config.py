"""Configuration management for Genome Explorer AI."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass
class AppConfig:
    """Application configuration settings."""
    
    # Paths
    data_dir: Path = Path("data")
    models_dir: Path = Path("models")
    cache_dir: Path = Path(".cache")
    
    # AI/ML Settings
    openai_model: str = "gpt-4-turbo-preview"
    embedding_model: str = "all-MiniLM-L6-v2"
    max_tokens: int = 4096
    temperature: float = 0.7
    
    # Visualization Settings
    plot_height: int = 600
    plot_width: int = 800
    color_scheme: str = "viridis"
    
    # Performance
    cache_ttl: int = 3600  # 1 hour
    batch_size: int = 32
    num_workers: int = 4
    
    @classmethod
    def from_env(cls) -> "AppConfig":
        """Create config from environment variables."""
        return cls(
            data_dir=Path(str(Path.cwd() / "data")),
            models_dir=Path(str(Path.cwd() / "models")),
            cache_dir=Path(str(Path.cwd() / ".cache")),
        )

# Global config instance
config = AppConfig.from_env() 