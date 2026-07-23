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

def test_convert_file():

    module.convert_file(
        "tests/test-01.md",
        "tests/test-01.al",
    )

    with open("tests/test-01.al.expected") as exp_file:
        exp = exp_file.read()

    with open("tests/test-01.al") as res_file:
        res = res_file.read()

    assert res == exp
