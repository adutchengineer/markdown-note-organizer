"""Parse Markdown files to extract frontmatter, titles, tags, and links."""

from pydantic import BaseModel


class Note(BaseModel):
    """Represents a parsed Markdown note."""

    filepath: str
    title: str
    tags: set[str] = set()
    links: list[str] = []
    word_count: int = 0


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from Markdown content.

    Returns a dict with 'title' and 'tags' keys (if present).
    """
    raise NotImplementedError


def parse_note(filepath: str) -> Note:
    """Parse a single Markdown file into a Note.

    - Extract title from frontmatter, or fall back to first # heading
    - Extract tags from frontmatter
    - Find all [[wiki-style]] links
    - Count words in the body (excluding frontmatter)
    """
    raise NotImplementedError
