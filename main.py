"""Keeb Layout Switch — Switch the keyboard layout by language tag and show the current one."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='keeb_layout_switch',
        description='Switch the keyboard layout by language tag and show the current one.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Keeb Layout Switch')
    print('EN/RU or EN/DE without the language bar hunt.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
