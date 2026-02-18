"""Shared fixtures for galaxy-profile tests."""

import copy

import pytest

from generator.config import validate_config
from generator.svg_builder import SVGBuilder


@pytest.fixture
def sample_config():
    """A valid config dict with 3 galaxy_arms and 2 projects tailored for Samuel's profile."""
    return {
        "username": "samueljunqueiraa",
        "profile": {
            "name": "Samuel Junqueira",
            "tagline": "Systems Analyst | Java Specialist",
            "company": "Fábrica",
            "location": "Machado, MG",
            "bio": "Analista de Sistemas focado no ecossistema Java e arquiteturas modernas.",
            "philosophy": "The best code is the code that empowers others.",
        },
        "social": {
            "email": "samuel@example.com",
            "linkedin": "samueljunqueiraa",
            "website": "https://github.com/samueljunqueiraa",
        },
        "galaxy_arms": [
            {"name": "Java Backend", "color": "synapse_cyan", "items": ["Java 21", "Spring Boot", "JPA", "PostgreSQL"]},
            {"name": "Frontend & UI", "color": "dendrite_violet", "items": ["TypeScript", "React", "Tailwind", "Flutter"]},
            {"name": "Architecture & Ops", "color": "axon_amber", "items": ["Hexagonal Architecture", "DDD", "Docker", "Git"]},
        ],
        "projects": [
            {"repo": "samueljunqueiraa/erp-industrial", "arm": 0, "description": "ERP construído do zero para gestão fabril."},
            {"repo": "samueljunqueiraa/wallet-ddd", "arm": 2, "description": "Implementação de carteira utilizando Hexagonal Architecture."},
        ],
        "theme": {
            "void": "#020c20",
            "nebula": "#051633",
            "star_dust": "#0a224a",
            "synapse_cyan": "#00d4ff",
            "dendrite_violet": "#a78bfa",
            "axon_amber": "#ffb020",
            "text_bright": "#f1f5f9",
            "text_dim": "#94a3b8",
            "text_faint": "#64748b",
        },
        "stats": {"metrics": ["commits", "stars", "prs", "issues", "repos"]},
        "languages": {"exclude": ["HTML", "Shell", "Makefile"], "max_display": 8},
    }


@pytest.fixture
def sample_stats():
    """Realistic stats dict."""
    return {"commits": 1847, "stars": 342, "prs": 156, "issues": 89, "repos": 42}


@pytest.fixture
def sample_languages():
    """Language byte counts reflecting a Java-heavy focus."""
    return {
        "Java": 650000,
        "TypeScript": 280000,
        "JavaScript": 120000,
        "Dart": 95000,
        "CSS": 45000,
        "PL/pgSQL": 30000,
        "Dockerfile": 15000,
    }


@pytest.fixture
def cfg(sample_config):
    """Return a deep copy of sample_config for mutation-safe tests."""
    return copy.deepcopy(sample_config)


@pytest.fixture
def svg_builder(sample_config, sample_stats, sample_languages):
    """Create an SVGBuilder from validated sample fixtures."""
    config = validate_config(copy.deepcopy(sample_config))
    return SVGBuilder(config, sample_stats, sample_languages)
def svg_builder(sample_config, sample_stats, sample_languages):
    """Create an SVGBuilder from validated sample fixtures."""
    config = validate_config(copy.deepcopy(sample_config))
    return SVGBuilder(config, sample_stats, sample_languages)
