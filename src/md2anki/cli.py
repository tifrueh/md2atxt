import logging
import argparse as ap
from md2anki._version import __version__

def main():

    # Initialise the argument parser.
    parser = ap.ArgumentParser(
        prog = "md2anki",
        description = "convert Markdown notes to Anki notes",
        epilog = "For more information, see the md2anki(1) manual page.",
        add_help = False,
    )

    # Add mutually exclusive group for stage selectors.
    stage_selector_parser = parser.add_mutually_exclusive_group( required = False )

    # Add our arguments.
    parser.add_argument(
        "-h",
        "--help",
        action = "help",
        help = "Show help message.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action = "version",
        help = "Show version information.",
        version=f"%(prog)s v{__version__}"
    )
    stage_selector_parser.add_argument(
        "-c",
        "--convert",
        action = "store_true",
        required = False,
        help = "Only run conversion stage.",
    )
    stage_selector_parser.add_argument(
        "-l",
        "--link",
        action = "store_true",
        required = False,
        help = "Only run link stage.",
    )
    parser.add_argument(
        "-L",
        "--loglevel",
        action = "store",
        required = False,
        help = "Set the logging level.",
        metavar = "LOGLEVEL",
        type = str,
        choices = [ "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL" ],
        default = "INFO"
    )
    parser.add_argument(
        "-H",
        "--header",
        action = "append",
        required = False,
        help = "Set \"key\" header to \"value\". Can be specified multiple times.",
        metavar = "KEY:VALUE",
        type = str,
    )
    parser.add_argument(
        "-o",
        "--output",
        action = "store",
        required = False,
        help = "Specify an output file.",
        metavar = "OUT_FILE",
        type = str
    )
    parser.add_argument(
        "in_file",
        action = "store",
        help = "The input file(s) to process.",
        metavar = "IN_FILE",
        type = str,
        nargs = "+"
    )

    # Parse arguments.
    args = parser.parse_args()

    # Initialise logging system.
    log = logging.getLogger(__name__)
    logging.basicConfig(level = args.loglevel)

    # Log parsed arguments to the debug log.
    log.debug(args)
