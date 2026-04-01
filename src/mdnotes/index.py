"""Build and query an in-memory index of notes."""

from mdnotes.parser import Note


class NoteIndex:
    """In-memory index supporting tag, backlink, and keyword lookups."""

    def __init__(self) -> None:
        self.notes: list[Note] = []

    def add(self, note: Note) -> None:
        """Add a note to the index."""
        raise NotImplementedError

    def by_tag(self, tag: str) -> list[Note]:
        """Return all notes that have the given tag."""
        raise NotImplementedError

    def backlinks(self, title: str) -> list[Note]:
        """Return all notes that link to the given title."""
        raise NotImplementedError

    def build_from_directory(self, directory: str) -> None:
        """Parse all .md files in a directory and add them to the index."""
        raise NotImplementedError
