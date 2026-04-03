"""Tests for the Markdown parser."""

def test_parse_frontmatter_extracts_title():
    """Frontmatter with a title field should be extracted."""
    from mdnotes.parser import parse_frontmatter

    content = "---\ntitle: My Note\ntags: [python, testing]\n---\n\nBody text here."
    result = parse_frontmatter(content)
    assert result["title"] == "My Note"


def test_parse_frontmatter_extracts_tags():
    """Tags in [tag1, tag2] format should be parsed into a list."""
    from mdnotes.parser import parse_frontmatter

    content = "---\ntitle: My Note\ntags: [python, testing]\n---\n\nBody text."
    result = parse_frontmatter(content)
    assert "python" in result["tags"]
    assert "testing" in result["tags"]


def test_parse_note_falls_back_to_heading(tmp_path):
    """A note without frontmatter should use the first # heading as the title."""
    from mdnotes.parser import parse_note

    note_file = tmp_path / "note.md"
    note_file.write_text("# Heading Title\n\nSome body text here.")
    note = parse_note(str(note_file))
    assert note.title == "Heading Title"


def test_parse_note_finds_wiki_links(tmp_path):
    """Wiki-style [[links]] should be extracted from the body."""
    from mdnotes.parser import parse_note

    note_file = tmp_path / "note.md"
    note_file.write_text("# Test\n\nSee [[Other Note]] and [[Another]].")
    note = parse_note(str(note_file))
    assert "Other Note" in note.links
    assert "Another" in note.links


def test_parse_note_counts_words(tmp_path):
    """Word count should exclude frontmatter."""
    from mdnotes.parser import parse_note

    note_file = tmp_path / "note.md"
    note_file.write_text("---\ntitle: Test\n---\n\none two three four five")
    note = parse_note(str(note_file))
    assert note.word_count == 5
