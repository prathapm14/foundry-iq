from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


def Tool(name: str, description: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator to register a function as an agent tool (stub).

    The decorated function gets two attributes: __tool_name__ and __tool_description__.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        setattr(func, "__tool_name__", name)
        setattr(func, "__tool_description__", description)
        return func

    return decorator


@dataclass
class AgentConfig:
    model: str = "gpt-4"
    temperature: float = 0.7
    max_tokens: int = 1024
    system_prompt: str = "You are a helpful AI assistant."
    response_format: str = "markdown"

    knowledge_bases: List[str] = field(default_factory=list)
    search_strategy: str = "hybrid"

    # Safety / performance toggles (stubs)
    content_filter: str = "strict"
    pii_detection: bool = True
    cache_enabled: bool = True
    streaming: bool = False


@dataclass
class ChatResponse:
    content: str
    sources: List[Dict[str, str]] = field(default_factory=list)
    debug_info: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Agent:
    name: str
    config: AgentConfig
    _tools: Dict[str, Callable[..., Any]] = field(default_factory=dict)

    def add_tools(self, tools: List[Callable[..., Any]]) -> None:
        for t in tools:
            tool_name = getattr(t, "__tool_name__", t.__name__)
            self._tools[tool_name] = t

    def chat(self, message: str) -> ChatResponse:
        # Educational behavior: echo + show what would happen.
        content = (
            f"[{self.name}] (stub) I received: {message}\n\n"
            f"Model: {self.config.model}\n"
            f"Search strategy: {self.config.search_strategy}\n"
            f"Knowledge bases: {', '.join(self.config.knowledge_bases) or 'none'}\n"
        )
        return ChatResponse(content=content)
