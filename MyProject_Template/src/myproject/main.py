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


# Detect whether running from a PyInstaller .exe or from the script
if getattr(sys, 'frozen', False):
    # Running as a bundled .exe
    INSULT_FOLDER = os.path.join(sys._MEIPASS, "src")
else:
    # Running as a normal script
    INSULT_FOLDER = os.path.join(os.getcwd(), "src")



def main(argv=None):
    settings = Settings()
    return run(settings)


if __name__ == "__main__":
    raise SystemExit(main())
