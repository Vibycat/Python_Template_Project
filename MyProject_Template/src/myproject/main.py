"""
#-------------------------------------------;
# Project : MyProject                      ;
# Script  : main.py                        ;
# Purpose : Application entrypoint          ;
# Creator : Vibycat                         ;
# Created : 03/01/2026                      ;
# Version : 1.0                             ;
#-------------------------------------------;
"""

import sys
from .config import Settings
from .core.logic import run


def main(argv=None):
    settings = Settings()
    return run(settings)


if __name__ == "__main__":
    raise SystemExit(main())