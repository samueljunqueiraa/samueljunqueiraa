"""Shared fixtures for galaxy-profile tests with real data integration."""

import copy
import os
import pytest

from generator.config import validate_config
from generator.svg_builder import SVGBuilder
from generator.github_api import GitHubAPI  # Importando a API real

@pytest.fixture
def real_data():
    """Busca dados reais do seu perfil usando o GITHUB_TOKEN do ambiente."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        pytest.skip("GITHUB_TOKEN não encontrado. Pulando teste com dados reais.")
    
    api = GitHubAPI(token)
    stats = api.get_user_stats("samueljunqueiraa")
    languages = api.get_language_stats("samueljunqueiraa")
    
    return stats, languages

@pytest.fixture
def sample_config():
    """Configuração validada com seus dados de Systems Analyst."""
    return {
        "username": "samueljunqueiraa",
        "profile": {
            "name": "Samuel Junqueira",
            "tagline": "Systems Analyst | Java Specialist",
            "company": "Fábrica",
            "location": "Machado, MG",
            "bio": "Analista de Sistemas focado no ecossistema Java.",
            "philosophy": "The best code is the code that empowers others.",
        },
        "galaxy_arms": [
            {"name": "Java Backend", "color": "synapse_cyan", "items": ["Java 21", "Spring Boot", "JPA", "PostgreSQL"]},
            {"name": "Frontend & UI", "color": "dendrite_violet", "items": ["TypeScript", "React", "Tailwind", "Flutter"]},
            {"name": "Architecture & Ops", "color": "axon_amber", "items": ["Hexagonal Architecture", "DDD", "Docker", "Git"]},
        ],
        "projects": [
            {"repo": "samueljunqueiraa/erp-industrial", "arm": 0, "description": "ERP para gestão fabril."},
            {"repo": "samueljunqueiraa/wallet-ddd", "arm": 2, "description": "Projeto Wallet com Hexagonal Architecture."},
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
def svg_builder(sample_config, real_data):
    """Cria o SVGBuilder usando o espelho dos seus dados REAIS do GitHub."""
    stats, languages = real_data
    config = validate_config(copy.deepcopy(sample_config))
    return SVGBuilder(config, stats, languages)
