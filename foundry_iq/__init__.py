"""Foundry IQ (educational stubs).

These classes are intentionally minimal and designed to support the examples
in this repository. They are *not* an official Microsoft SDK.
"""

from .client import FoundryIQClient
from .knowledge_base import KnowledgeBase, DataSource
from .agent import Agent, AgentConfig, Tool

__all__ = [
    "FoundryIQClient",
    "KnowledgeBase",
    "DataSource",
    "Agent",
    "AgentConfig",
    "Tool",
]
