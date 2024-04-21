from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional, Dict, Generator, Any

    from mov_cli import Config
    from mov_cli.http_client import HTTPClient
    from mov_cli.scraper import ScraperOptionsT

from mov_cli.scraper import Scraper
from mov_cli.utils import EpisodeSelector
from mov_cli import Single, Multi, Metadata, MetadataType

__all__ = ("Boilerplate", )

class Boilerplate(Scraper):
    def __init__(self, config: Config, http_client: HTTPClient, options: Optional[ScraperOptionsT] = None) -> None:
        self.base_url = ...
        
        super().__init__(config, http_client)

    def search(self, query: str, limit: int = 10) -> Generator[Metadata, Any, None]:
        ...
    
    def scrape_metadata_episodes(self, metadata: Metadata) -> Dict[int, int] | Dict[None, int]:
        ...
    
    def scrape(self, metadata: Metadata, episode: EpisodeSelector, **kwargs) -> Single | Multi:
        ...