---
title: "md2anki"
section: "1"
---

# NAME

md2anki - convert Markdown notes to Anki notes

# SYNOPSIS

| **md2anki** ( **-h** | **-v** )

| **md2anki** \[ **-c** | **-l** \] \[ **-L** *LOGLEVEL* \] \[ **-H** *KEY:VALUE* ... \]
|         \[ **-o** *OUT_FILE* \] *IN_FILE* ...

# DESCRIPTION

**md2anki** is a small program that can be used to convert notes written in
Markdown (in a format specified in **md2anki.md**(5)) to Anki-importable text
files. There are two stages to the conversion, which run in sequence by default
or can be individually selected using the "**-c**" and "**-l**" flags:

**Conversion Stage**
: The conversion stage takes in a list of files and converts them individually
into an intermediary file format (see **md2anki.al**(5)), called an "Anki line"
file. By default, the naming scheme for the output files is simply to use the
same name and parent directory as the source file, but to use "al" as file
extension instead of "md". If only one input file was specified, then the exact
path of the output file can be specified using the "**-o**" option.

**Link Stage**
: The link stage takes in a list of Anki line files and links them together into
one text file that can be imported directly into Anki.

# OPTIONS

**-c**, **-\-convert**
: Only run the conversion stage.

**-h**, **-\-help**
: Display the help message.

**-H**, **-\-header** *KEY:VALUE*
: Set the "`key`" header of the Anki import file produced to "`value`". This
can, for example, be used to preset a deck name for the notes within via the
"`deck`" header. Or to set a column from which the deck for the individual notes
shall be read via the "`deck column`" header. See the Anki documentation for
reference.

  This option be specified multiple times.

  Note, however, that this option only has an effect if it is supplied for an
  execution of the program during which the link stage runs.

**-l**, **-\-link**
: Only run the link stage.

**-L, -\-loglevel** *LOGLEVEL*
: Set the logging level. Should be one of ( DEBUG | INFO | WARNING | ERROR |
CRITICAL ).

**-o**, **-\-output** *OUT_FILE*
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

**pandoc**(1), **md2anki.md**(5), **md2anki.al**(5), **md2anki.txt**(5)
