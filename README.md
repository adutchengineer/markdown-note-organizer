# Markdown Note Organizer

A command-line tool that manages a folder of Markdown notes. Given a directory of `.md` files, `mdnotes` can parse metadata, build a search index, and generate a table of contents.

## Setup

```bash
pip install -e ".[dev]"
```

## Run tests

```bash
pytest tests/ -v
```

## Requirements

### File Parsing
- [ ] Extract `title` from YAML frontmatter, or fall back to the first `# heading`
- [ ] Extract `tags` from frontmatter as a list of strings
- [ ] Find all internal links in `[[double bracket]]` syntax
- [ ] Count the word count of the body (excluding frontmatter)
- [ ] Gracefully handle files with no frontmatter, no title, or malformed YAML

### Data Model
- [ ] Use Pydantic to validate each parsed note (filepath, title, tags, links, word_count)

### Indexing
- [ ] Tag index: given a tag, return all notes with that tag
- [ ] Link index: given a note title, return all notes that link to it (backlinks)
- [ ] Search index: given a keyword, return all notes whose title or body contains it

### Search
- [ ] Keyword search across title and body
- [ ] Tag search to find all notes with a given tag
- [ ] Backlink search to find all notes linking to a given title

### Table of Contents Generation
- [ ] Generate a `TOC.md` that lists all notes grouped by tag with links and word counts
- [ ] Include an "Untagged" section for notes with no tags

### Error Handling
- [ ] Do not crash on files that are not valid UTF-8
- [ ] Do not crash on directories that do not exist
- [ ] Do not crash on frontmatter that is not valid YAML
- [ ] Do not crash on notes with no title and no headings
- [ ] Log warnings for skipped files and continue processing

## Project Structure

```
src/mdnotes/
    __init__.py
    parser.py      # Parse Markdown files and extract metadata
    index.py       # Build and query in-memory note index
    search.py      # Keyword search across notes
tests/
    test_parser.py
    test_search.py
    test_index.py
```
