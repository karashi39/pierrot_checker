import sys
from typing import Optional

from enums import TableHeader
from pierrot_page import PierrotPage
from terminal_output import TerminalOutput
from utils import get_target_machine_types


def main(store_number: int, targets: Optional[str] = None) -> None:
    pierrot_page = PierrotPage(store_number)
    title = pierrot_page.get_store_name()
    machine_table = pierrot_page.get_machines_table()
    if targets:
        target_machine_types = get_target_machine_types(targets)
        machine_table = [
            row
            for row in machine_table
            if row[str(TableHeader.MACHINE_TYPE.value)] in target_machine_types
        ]
    terminal_output = TerminalOutput(title, machine_table)
    terminal_output.print()


if __name__ == "__main__":
    args = sys.argv
    store_number = int(args[1])
    targets = args[2] if len(args) >= 3 else None
    main(store_number, targets)
