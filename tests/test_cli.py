import argparse
import pathlib
import md2atxt.cli as module


# Test if everything works correctly with joint phases.
def test_run_stages(testenv_path):

    tmp = str(testenv_path)

    args = argparse.Namespace()
    args.convert = False
    args.link = False
    args.loglevel = "DEBUG"
    args.header = ["deck:Default", "notetype:Basic"]
    args.output = f"{tmp}/md2atxt.txt"
    args.in_file = [
        f"{tmp}/test-01.md",
        f"{tmp}/test-02.md",
        f"{tmp}/test-03.md",
    ]
    module.run_stages(args)

    exp_vector = []
    res_vector = []

    for nr in ["01", "02", "03"]:
        with open(f"{tmp}/test-{nr}.al.expected") as exp_file:
            exp_vector.append(exp_file.read())
        with open(f"{tmp}/test-{nr}.al") as res_file:
            res_vector.append(res_file.read())

    with open(f"{tmp}/md2atxt.txt.expected") as exp_file:
        exp_vector.append(exp_file.read())

    with open(f"{tmp}/md2atxt.txt") as res_file:
        res_vector.append(res_file.read())

    assert res_vector == exp_vector


# Test if everything works correctly even with faulty/missing files.
def test_run_stages_faulty(testenv_path):

    tmp = str(testenv_path)

    args = argparse.Namespace()
    args.convert = False
    args.link = False
    args.loglevel = "DEBUG"
    args.header = ["deck:Default", "notetype:Basic"]
    args.output = f"{tmp}/md2atxt.txt"
    args.in_file = []

    for nr in ["04", "05", "06", "07", "01", "02", "03"]:
        args.in_file.append(f"{tmp}/test-{nr}.md")

    module.run_stages(args)

    exp_vector = []
    res_vector = []

    for nr in ["01", "02", "03"]:
        with open(f"{tmp}/test-{nr}.al.expected") as exp_file:
            exp_vector.append(exp_file.read())
        with open(f"{tmp}/test-{nr}.al") as res_file:
            res_vector.append(res_file.read())

    for nr in ["04", "05", "06", "07"]:
        filepath = pathlib.Path(f"{tmp}/test-{nr}.al")
        assert not filepath.exists()

    with open(f"{tmp}/md2atxt.txt.expected") as exp_file:
        exp_vector.append(exp_file.read())

    with open(f"{tmp}/md2atxt.txt") as res_file:
        res_vector.append(res_file.read())

    assert res_vector == exp_vector
