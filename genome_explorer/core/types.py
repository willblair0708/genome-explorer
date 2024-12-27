"""Core type definitions for Genome Explorer AI."""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple, Union
from datetime import datetime

class GenomeFormat(str, Enum):
    """Supported genome file formats."""
    FASTA = "fasta"
    FASTQ = "fastq"
    BAM = "bam"
    VCF = "vcf"
    BED = "bed"

class VisualizationType(str, Enum):
    """Types of genome visualizations."""
    LINEAR = "linear"
    CIRCULAR = "circular"
    KARYOTYPE = "karyotype"
    COVERAGE = "coverage"
    VARIANTS = "variants"

@dataclass
class GenomeRegion:
    """A region in a genome."""
    chromosome: str
    start: int
    end: int
    strand: Optional[str] = None
    features: Optional[Dict[str, str]] = None

@dataclass
class GenomeFeature:
    """A feature in a genome (gene, exon, etc.)."""
    id: str
    type: str
    region: GenomeRegion
    attributes: Dict[str, str]
    score: Optional[float] = None

@dataclass
class MutationEvent:
    """A mutation event in a genome."""
    region: GenomeRegion
    type: str  # SNP, insertion, deletion, etc.
    ref: str
    alt: str
    impact: Optional[str] = None
    probability: float = 1.0

@dataclass
class SimulationState:
    """State of a genomic simulation."""
    generation: int
    population_size: int
    mutation_events: List[MutationEvent]
    fitness_scores: Dict[str, float]
    timestamp: datetime

@dataclass
class EducationModule:
    """An educational module."""
    id: str
    title: str
    description: str
    difficulty: str
    prerequisites: List[str]
    content: str
    quiz: Dict[str, Dict[str, Union[str, List[str]]]]
    completed: bool = False
    score: Optional[float] = None

# Type aliases
ChromosomeID = str
Position = int
Sequence = str
GenomeCoordinate = Tuple[ChromosomeID, Position]
FeatureMap = Dict[GenomeCoordinate, List[GenomeFeature]] 