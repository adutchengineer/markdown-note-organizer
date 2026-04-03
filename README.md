# mdnotes

A Markdown note organizer you will build independently to demonstrate everything from the [Python](https://dutchengineer.com/foundations/python/) module. If you use Obsidian, Logseq, or any Markdown-based note system, you have a real folder of notes you could point this tool at when you are done.

Every Python concept from the module shows up: reference semantics when managing the in-memory index, dictionaries and sets for fast lookup, generators for lazy file processing, functions and decorators for shared logic, error handling for malformed input, and Pydantic models for structured note metadata.

## Getting started

```bash
uv sync --all-extras
uv run pytest tests/ -v
```

Every test has real assertions that will fail until you implement the code. Read each test to understand what the function should do.

## What to build

**File parsing** extracts metadata from each Markdown note. Notes can have YAML-style frontmatter with `title` and `tags`. Internal links use `[[double bracket]]` syntax. The parser extracts the title (from frontmatter, falling back to the first `#` heading, then the filename), tags as a list of strings, all wiki-style links, and a word count of the body.

**Data model** uses Pydantic to validate each parsed note. The `Note` model has `filepath`, `title`, `tags` (a set of strings), `links` (a list), and `word_count`.

**Indexing** builds three in-memory indexes from a folder of notes: a tag index (given a tag, return all notes with that tag), a backlink index (given a note title, return all notes that link to it), and a search index (given a keyword, return matching notes).

**Search** supports three modes: keyword search across titles and bodies, tag search for all notes with a given tag, and backlink search for all notes linking to a given title.

**Table of contents** generates a `TOC.md` file listing all notes grouped by tag, with links and word counts. Untagged notes go under an "Untagged" section.

**Error handling** ensures the tool never crashes on bad input. Handle files that are not valid UTF-8, directories that do not exist, malformed YAML frontmatter, notes with no title or headings, and permission errors. Log warnings for skipped files and continue processing.

## Project structure

```
src/mdnotes/
├── __init__.py
├── parser.py        # Note model, frontmatter parsing, link extraction
├── index.py         # NoteIndex with tag, backlink, and search indexes
├── search.py        # Keyword, tag, and backlink search functions
├── toc.py           # Table of contents generator
└── cli.py           # CLI entry point
tests/
├── test_parser.py   # Parsing and metadata extraction tests
├── test_index.py    # Index building and lookup tests
└── test_search.py   # Search functionality tests
```

## How to submit

1. Fork this starter repo
2. Complete the requirements
3. Push to your GitHub repo
4. Verify CI passes (green badge)
5. Submit your repository URL
