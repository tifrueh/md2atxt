import logging
import pathlib

# =============================================================================
# = GLOBALS ===================================================================

log = logging.getLogger(__name__)

# =============================================================================
# = FUNCTIONS =================================================================


def assemble_header(header_list):
    """Produce a Anki import-file header.

    arguments:
        header_list -- List of strings containing additional key:value pairs.

    return:
        A string containing a correctly formatted Anki import-file header.
    """

    log.debug(f"Assembling header from: {header_list}")

    full_header_list = ["#separator:semicolon", "#html:true"]
    full_header_list += map(lambda x: f"#{x}", header_list)
    output = '\n'.join(full_header_list)
    output += '\n'

    log.debug(f"Got: {output}")

    return output


def link(args):
    """Run the link stage based upon some parsed arguments.

    arguments:
        args -- The parsed arguments object (as returned by parse_args()).

    return:
        None
    """

    log.info("Running link stage …")

    line_list = []
    out_file = args.output if args.output else "md2atxt.txt"

    for file in args.in_file:
        in_file = pathlib.Path(file)
        try:
            with open(str(in_file)) as line_file:
                line = line_file.read()
            line_list.append(line)
        except FileNotFoundError:
            log.warning(f"{file} not found, skipping …")
            continue
        except PermissionError:
            log.warning(
                f"Encountered permission error while processing {file},"
                "skipping …"
            )
            continue

    line_list = map(lambda x: x if x[-1] == '\n' else x[:-1], line_list)
    import_file_str = assemble_header(args.header if args.header else [])
    import_file_str += "".join(line_list)

    try:
        with open(out_file, "w") as import_file:
            import_file.write(import_file_str)
    except PermissionError:
        log.critical(
            f"Could not write output file {out_file}"
            "due to permission error, aborting …"
        )
        exit(1)
