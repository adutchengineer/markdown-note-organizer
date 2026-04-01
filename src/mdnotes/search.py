"""Search notes by keyword."""

from mdnotes.parser import Note


def keyword_search(notes: list[Note], query: str) -> list[Note]:
    """Return notes whose title or body contains the query (case-insensitive)."""
    raise NotImplementedError
