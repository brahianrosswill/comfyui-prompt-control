import logging
import os

log = logging.getLogger("comfyui-prompt-control")

if os.environ.get("PC_USE_OLD_PARSER", "0") != "1":
    from .parser_parsy import parse_prompt_schedules  # noqa
else:
    log.warning("Using old Lark parser (UNSUPPORTED)")
    from .parser_lark import parse_prompt_schedules  # noqa
