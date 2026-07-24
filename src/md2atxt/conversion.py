import subprocess
import re
import tomllib
import pathlib
import logging

# =============================================================================
# = CUSTOM ERROR TYPES ========================================================


class ParseException(Exception):
    pass


class NoteIDMissingException(Exception):
    pass


# =============================================================================
# = GLOBALS ===================================================================

FILE_RES = r"^\+\+\+\s*(?P<toml>.*?)\s*\+\+\+\s*(?P<md>.*?)\s*$"
FIELD_RES = r"\s*<!-- \|\| -->\s*"
FILE_RE = re.compile(FILE_RES, re.DOTALL)
FIELD_RE = re.compile(FIELD_RES)
log = logging.getLogger(__name__)


# =============================================================================
# = FUNCTIONS =================================================================

def convert_string(md_string):
    """Convert a Markdown string to HTML.

    arguments:
        md_string -- The Markdown string to convert.

    return:
        A string containing the converted HTML.
    """

    log.debug(f"Converting string: {md_string}")

    result = subprocess.run(
        [
            "pandoc",
            "-f",
            "markdown+implicit_figures+tex_math_dollars",
            "-t",
            "html",
            "--mathjax",
            "--embed-resources"
        ],
        input=md_string,
        capture_output=True,
        text=True
    )

    result = result.stdout.replace('"', "\"\"")

    log.debug(f"Got: {result}")

    return result


def parse_file_string(file_string):
    """Parse a Markdown string read from a file into a dictionary structure.

    arguments:
        file_string -- The Markdown string to parse.

    return:
        A dictionary of the following form:
        {
            "toml": "string"     // The TOML metadata header.,
            "md":   [ "string" ] // A list of strings, each entry containing
                                 // one field of the parsed file.
        }

    exceptions:
        Raises a ParseException if the file doesn't parse.
    """

    log.debug(f"Parsing file contents: f{file_string}")

    match = FILE_RE.match(file_string)

    if not match:
        raise ParseException("File string did not parse.")

    result = match.groupdict()
    result["md"] = FIELD_RE.split(result["md"])

    log.debug(f"Got: f{result}")

    return result


def extract_noteid(toml_string):
    """Extract the 'noteid' attribute from TOML metadata.

    arguments:
        toml_string -- The TOML string to parse.

    return:
        A string containing the noteid.

    exceptions:
        Raises a TOMLDecodeError if the TOML is invalid (see tomllib).
        Also raises a NoteIDMissingException if the noteid isn't specified.
    """

    log.debug(f"Extracting noteid from TOML: {toml_string}")

    data = tomllib.loads(toml_string)

    if "noteid" not in data:
        raise NoteIDMissingException("No noteid given.")
    result = data["noteid"]

    log.debug(f"Got: {result}")

    return result


def assemble_file(noteid, fields):
    """Assemble the contents of an Anki line file from a noteid and
    correctly escaped note fields.

    arguments:
        noteid -- The noteid for the Anki line file.
        fields -- A list of HTML-formatted strings, with quotes correctly
        escaped.

    return:
        An Anki line file as a string.
    """

    log.info("Assembling output file")
    log.debug(f"Adding noteid: {noteid}")

    result = f"\"{noteid}\""

    for field in fields:
        log.debug(f"Adding field: {field}")
        result += f";\"{field}\""

    if result[-1] != '\n':
        log.debug("Adding trailing newline")
        result += '\n'

    return result


def convert_file(in_file, out_file):
    """Convert a Markdown file to a Anki line file.

    arguments:
        in_file  -- The filename of the file to convert.
        out_file -- The filename of the file to write to.

    returns:
        None

    exceptions:
        Raises a ParseException if the file doesn't parse.
        Also raises a TOMLDecodeError if the metadata TOML is invalid.
        Also raises a NoteIDMissingException if no noteid is specified.
        Also may raise any exception the 'open()/read()/write()' functions may
        raise.
    """

    log.info(f"Converting {in_file} -> {out_file}")

    # Read file into data structure.
    with open(in_file) as file:
        file_str = file.read()
        data_dict = parse_file_string(file_str)

    # Extract noteid from the TOML header.
    noteid = extract_noteid(data_dict["toml"])

    # Convert all fields.
    fields = []
    for md_field in data_dict["md"]:
        fields.append(convert_string(md_field))

    # Assemble and write Anki line file.
    out = assemble_file(noteid, fields)
    with open(out_file, "w") as file:
        file.write(out)


def convert(args):
    """Run the conversion stage based upon some parsed arguments.

    arguments:
        args -- The parsed arguments object (as returned by parse_args()).

    return:
        None, but note that this function will modify the 'args.in_file' field
        to the list of /output/ files it produces, so that a potential link
        phase can be run directly afterwards on the same 'args' object.
    """

    log.info("Running conversion stage …")

    out_list = []

    for file in args.in_file:
        in_file = pathlib.Path(file)
        if args.convert and args.output:
            out_file = args.output
        else:
            out_file = in_file.with_suffix(".al")
        try:
            convert_file(str(in_file), str(out_file))
            out_list.append(str(out_file))
        except ParseException:
            log.warning(f"{file} does not parse, skipping …")
            continue
        except tomllib.TOMLDecodeError:
            log.warning(f"{file} has invalid metadata, skipping …")
            continue
        except NoteIDMissingException:
            log.warning(f"{file} has no noteid, skipping …")
            continue
        except FileNotFoundError:
            log.warning(f"{file} not found, skipping …")
            continue
        except PermissionError:
            log.warning(
                f"Encountered permission error while processing {file},"
                "skipping …"
            )
            continue

    args.in_file = out_list
    log.debug(f"New arguments: {args}")
