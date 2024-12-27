# Genome Explorer AI

An interactive AI-powered platform that democratizes genomics education through intuitive visualizations, simulations, and natural language interactions.

## Features

- 🧬 Interactive Genome Visualization & Analysis
- 🤖 AI-Powered Genomic Q&A System
- 🔬 Genomics Simulation Engine
- 📊 Personalized Genome Reports
- 📚 Educational Module System
- 🎮 Interactive Genome Playground

## Quick Start

```bash
# Install dependencies with uv (recommended)
uv venv
source .venv/bin/activate
uv pip install -e .

# Or with Poetry
poetry install
poetry shell

# Run the application
streamlit run genome_explorer/app.py
```

## Development

```bash
# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Check types
mypy .

# Format code
black .
isort .
```

## Project Structure

```
genome_explorer/
├── core/           # Core functionality and utilities
├── visualization/  # Genome visualization components
├── ai/            # AI and NLP components
├── simulation/    # Genomics simulation engine
├── reports/       # Report generation system
��── education/     # Educational content and modules
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details 