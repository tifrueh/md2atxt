---
title: "md2anki.md"
section: "5"
---

# NAME

md2anki.md - md2anki Markdown file format

# DESCRIPTION

To be used with **md2anki**(1), Markdown files need to adhere to a specific
format, described in this manual.

Firstly, the file shall include a TOML metadata header, delimited by the
following character sequence:

```
+++
```

In this header, the TOML key `noteid` shall be set to a user-defined identifier.
Note that this identifier will be used by Anki for duplicate detection, so it
should be unique across all the notes that the user ever wants to import via a
text file.

And secondly, the parts of the file that should be used as the fields in the
final Anki note shall be delimited by the following character sequence:

```
<!-- || -->
```

# EXAMPLE

A Markdown file that should become an Anki note with the identifier "`foo`",
containing two fields with a simple question and an answer, would look as
follows:

```markdown
+++
noteid: "foo"
+++

## What is a bar?

<!-- || -->

A bar is usually a baz.
```

# SEE ALSO

**pandoc**(1), **md2anki**(1), **md2anki.al**(5), **md2anki.txt**(5)
