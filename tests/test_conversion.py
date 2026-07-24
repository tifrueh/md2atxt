import argparse
import md2atxt.conversion as module

test_convert_string_in = """# Testfile
Some more **text** here.
"""

test_convert_string_out = """<h1 id=""testfile"">Testfile</h1>
<p>Some more <strong>text</strong> here.</p>
"""


def test_convert_string():
    result = module.convert_string(test_convert_string_in)
    assert result == test_convert_string_out


test_parse_file_string_in = """+++
title = "thisisatitle"
noteid = "foo"
+++

## What is a bar?

<!-- || -->

A bar is usually a baz.

<!-- || -->

There's a second part here.

<!-- || -->

And a third.
"""

test_parse_file_string_out = {
    "toml": "title = \"thisisatitle\"\nnoteid = \"foo\"",
    "md": [
        "## What is a bar?",
        "A bar is usually a baz.",
        "There's a second part here.",
        "And a third.",
    ]
}


def test_parse_file_string():
    result = module.parse_file_string(test_parse_file_string_in)
    assert result == test_parse_file_string_out


test_extract_noteid_in = """title = "thisisatitle"
noteid = "foo"

[table]
key = "there are tables, whoo"
noteid = "and an incorrect noteid"
"""

test_extract_noteid_out = "foo"


def test_extract_noteid():
    result = module.extract_noteid(test_extract_noteid_in)
    assert result == test_extract_noteid_out


test_assemble_file_in_noteid = "foo"
test_assemble_file_in_fields = [
    "<h1>What is a bar?</h1>",
    "<p>A bar is usually a baz.</p>",
    "<p>There's a second part here.</p>",
    "<p>And a third.</p>"
]

test_assemble_file_out = """"foo";"<h1>What is a bar?</h1>";"<p>A bar is usually a baz.</p>";"<p>There's a second part here.</p>";"<p>And a third.</p>"
"""


def test_assemble_file():
    result = module.assemble_file(
        test_assemble_file_in_noteid,
        test_assemble_file_in_fields
    )
    assert result == test_assemble_file_out


def test_convert_file(testenv_path):

    tmp = str(testenv_path)

    module.convert_file(
        f"{tmp}/test-01.md",
        f"{tmp}/test-01.al",
    )

    with open(f"{tmp}/test-01.al.expected") as exp_file:
        exp = exp_file.read()

    with open(f"{tmp}/test-01.al") as res_file:
        res = res_file.read()

    assert res == exp


def test_convert(testenv_path):

    tmp = str(testenv_path)

    args = argparse.Namespace()
    args.convert = True
    args.link = False
    args.loglevel = "DEBUG"
    args.header = None
    args.output = None
    args.in_file = [f"{tmp}/test-02.md", f"{tmp}/test-03.md"]
    module.convert(args)

    exp = []
    res = []

    with open(f"{tmp}/test-02.al.expected") as exp_file:
        exp.append(exp_file.read())

    with open(f"{tmp}/test-03.al.expected") as exp_file:
        exp.append(exp_file.read())

    with open(f"{tmp}/test-02.al") as res_file:
        res.append(res_file.read())

    with open(f"{tmp}/test-03.al") as res_file:
        res.append(res_file.read())

    assert res == exp
