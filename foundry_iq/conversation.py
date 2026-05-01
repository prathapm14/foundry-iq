"""Small local conversation session wrapper (stub)."""

from __future__ import annotations

from dataclasses import dataclass

from .agent import Agent, ChatResponse


@dataclass
class ConversationSession:
    agent: Agent

    def send_message(self, message: str) -> ChatResponse:
        return self.agent.chat(message)
