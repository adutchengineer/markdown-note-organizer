"""Tests for the note index."""

import pytest


@pytest.mark.skip(reason="Not yet implemented")
def test_index_by_tag():
    """Notes should be retrievable by tag."""
    from mdnotes.index import NoteIndex
    from mdnotes.parser import Note

    index = NoteIndex()
    index.add(Note(filepath="a.md", title="Note A", tags={"python", "testing"}, word_count=100))
    index.add(Note(filepath="b.md", title="Note B", tags={"javascript"}, word_count=50))

    results = index.by_tag("python")
    assert len(results) == 1
    assert results[0].filepath == "a.md"


@pytest.mark.skip(reason="Not yet implemented")
def test_index_backlinks():
    """Backlinks should find notes that link to a given title."""
    from mdnotes.index import NoteIndex
    from mdnotes.parser import Note

    index = NoteIndex()
    index.add(Note(filepath="a.md", title="Note A", links=["Note B"], word_count=100))
    index.add(Note(filepath="b.md", title="Note B", links=[], word_count=50))

    results = index.backlinks("Note B")
    assert len(results) == 1
    assert results[0].filepath == "a.md"


@pytest.mark.skip(reason="Not yet implemented")
def test_index_unknown_tag_returns_empty():
    """Querying a tag that no note has should return an empty list."""
    from mdnotes.index import NoteIndex

    index = NoteIndex()
    results = index.by_tag("nonexistent")
    assert results == []
