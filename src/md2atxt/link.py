import logging

log=logging.getLogger(__name__)

def link(args):
    """Run the link stage based upon some parsed arguments.

    arguments:
        args -- The parsed arguments object (as returned by parse_args()).
        log  -- The logger object with which to produce log messages.

    return:
        None
    """

    log.info("Running link stage …")
