---
title: "md2anki"
section: "1"
---

# NAME

md2anki - Convert Markdown notes to Anki notes

# SYNOPSIS

**md2anki** ( **-h** | **-v** )

**md2anki** \[ **-c** | **-l** \] \[ **-o** *OUT_FILE* \] *IN_FILE* ...

# DESCRIPTION

**md2anki** is a small program that can be used to convert notes written in
Markdown (in a format specified in **md2anki.md**(5)) to Anki-importable text
files. There are two stages to the conversion, which can run in sequence by
default or can be individually selected using the "**-c**" and "**-l**" flags:

**Conversion Stage**
: The conversion stage takes in a list of files and converts them individually
into an intermediary file format (see **md2anki.al**(5)), called an "Anki line"
file. By default, the naming scheme for the output files is simply to use the
same name and parent directory as the source file, but to use "al" as file
extension instead of "md". If only one input file was specified, then the exact
path of the output file can be specified using the "**-o**" option.

**Link Stage**
: The link stage takes in a list of anki line files and links them together into
one text file that can be imported directly into Anki.

# OPTIONS

**-c**, **-\-convert**
: Only run the conversion stage.

**-h**, **-\-help**
: Display the help message.

**-l**, **-\-link**
: Only run the link stage.

**-o**, **-\-output**
: Specify an output file.

**-v**, **-\-version**
: Display version information.

# NOTES

**md2anki** is managed via GitHub at <https://github.com/tifrueh/md2anki>.
Should you find any bugs, you're very welcome to open an issue over there.

# EXIT STATUS

**0**
: Success

**1**
: Failure

# EXAMPLES

Examples are still TODO

```text
TODO
```

# SEE ALSO

**pandoc**(1), **md2anki.md**(5), **md2anki.al**(5), **md2anki.txt(5)**
