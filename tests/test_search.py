"""Tests for keyword search."""

def test_keyword_search_matches_title():
    """Search should match notes by title."""
    from mdnotes.parser import Note
    from mdnotes.search import keyword_search

    notes = [
        Note(filepath="a.md", title="Python Variables", word_count=100),
        Note(filepath="b.md", title="JavaScript Basics", word_count=50),
    ]
    results = keyword_search(notes, "python")
    assert len(results) == 1
    assert results[0].filepath == "a.md"


def test_keyword_search_case_insensitive():
    """Search should be case-insensitive."""
    from mdnotes.parser import Note
    from mdnotes.search import keyword_search

    notes = [Note(filepath="a.md", title="Python Variables", word_count=100)]
    results = keyword_search(notes, "PYTHON")
    assert len(results) == 1


def test_keyword_search_no_results():
    """Search with no matching notes should return an empty list."""
    from mdnotes.parser import Note
    from mdnotes.search import keyword_search

    notes = [Note(filepath="a.md", title="Python Variables", word_count=100)]
    results = keyword_search(notes, "rust")
    assert len(results) == 0
