import md2atxt.link as module

test_assemble_header_in = ["deck:MyDeck", "notetype:MyType"]
test_assemble_header_out = """#separator:semicolon
#html:true
#deck:MyDeck
#notetype:MyType
"""


def test_assemble_header():
    result = module.assemble_header(test_assemble_header_in)
    assert result == test_assemble_header_out
