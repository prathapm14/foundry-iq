from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import uuid


@dataclass
class DataSource:
    """Represents a data source attached to a KnowledgeBase."""

    type: str
    connection_string: Optional[str] = None
    query: Optional[str] = None
    container: Optional[str] = None
    refresh_interval: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass
class KnowledgeBase:
    """A minimal knowledge base container (no real indexing)."""

    name: str
    description: Optional[str] = None
    id: str = field(default_factory=lambda: f"kb-{uuid.uuid4().hex[:8]}")
    sources: List[Any] = field(default_factory=list)

    def add_source(self, source: Any) -> None:
        """Add either a DataSource instance or a dict-like config."""
        self.sources.append(source)

    def build(self) -> None:
        # In a real implementation, this would ingest, chunk, embed, and index.
        return None

    def deploy(self) -> None:
        # Placeholder for deployment lifecycle.
        return None
