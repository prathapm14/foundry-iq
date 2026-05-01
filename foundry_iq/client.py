from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .knowledge_base import KnowledgeBase
from .agent import Agent, AgentConfig


@dataclass
class FoundryIQClient:
    """A tiny client stub.

    This exists to make the repository examples runnable without needing
    external services.
    """

    subscription_id: str
    resource_group: str
    credential: Optional[object] = None

    def create_knowledge_base(self, name: str, description: str | None = None) -> KnowledgeBase:
        kb = KnowledgeBase(name=name, description=description)
        return kb

    def create_agent(self, name: str, config: AgentConfig) -> Agent:
        return Agent(name=name, config=config)
