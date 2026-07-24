import argparse
import md2atxt.link as module

test_assemble_header_0_in = ["deck:MyDeck", "notetype:MyType"]
test_assemble_header_0_out = """#separator:semicolon
#html:true
#deck:MyDeck
#notetype:MyType
"""


def test_assemble_header_0():
    result = module.assemble_header(test_assemble_header_0_in)
    assert result == test_assemble_header_0_out


test_assemble_header_1_in = []
test_assemble_header_1_out = """#separator:semicolon
#html:true
"""


def test_assemble_header_1():
    result = module.assemble_header(test_assemble_header_1_in)
    assert result == test_assemble_header_1_out


def test_link(testenv_path):

    tmp = str(testenv_path)

    args = argparse.Namespace()
    args.convert = False
    args.link = True
    args.loglevel = "DEBUG"
    args.header = ["deck:Default", "notetype:Basic"]
    args.output = f"{tmp}/md2atxt.txt"
    args.in_file = [
        f"{tmp}/test-01.al.expected",
        f"{tmp}/test-02.al.expected",
        f"{tmp}/test-03.al.expected",
    ]
    module.link(args)

    with open(f"{tmp}/md2atxt.txt.expected") as exp_file:
        exp = exp_file.read()

    with open(f"{tmp}/md2atxt.txt") as res_file:
        res = res_file.read()

    assert res == exp
