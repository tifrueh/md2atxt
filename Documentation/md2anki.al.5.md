---
title: "md2anki.al"
section: "5"
---

# NAME

md2anki.al - md2anki "al" file format

# DESCRIPTION

An Anki line file is, technically, a simple plain-text file, which contains a
list of HTML chunks, separated by a single "`;`" character. Each such HTML chunk
shall be enclosed by two "`"`" characters, one on each end, with every occurrence
of "`"`" within the chunk either being escaped with a second "`"`" character or as
an HTML entity.

Note that this is also exactly what the conversion stage of **md2anki**(1)
produces, if applied to a correctly formatted Markdown file (see
**md2anki.md**(5)).

# NOTES

An Anki line file is, essentially, simply a fragment of a plain-text Anki import
file as described in

<https://docs.ankiweb.net/importing/text-files.html>

# EXAMPLE

The approximate conversion of the example Markdown file given as example in
**md2anki.md**(5) would look as follows:

```csv
"foo";"<h2>What is a bar?</h2>";"<p>A bar is usually a baz.</p>"
```

# SEE ALSO

**pandoc**(1), **md2anki**(1), **md2anki.md**(5), **md2anki.txt**(5)
