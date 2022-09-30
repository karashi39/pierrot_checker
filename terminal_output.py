from typing import Any

import prettytable

from enums import MachineState, TableHeader


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class TerminalOutput:
    title: str
    machine_table: list[dict[str, Any]]
    pretty_table: prettytable.PrettyTable

    def __init__(self, title: str, machine_table: list[dict[str, Any]]) -> None:
        self.title = title
        self.machine_table = machine_table
        self.set_pretty_table()

    def set_pretty_table(self) -> None:
        pretty_table = prettytable.PrettyTable()
        pretty_table.field_names = [
            TableHeader.MACHINE_TYPE.value,
            TableHeader.STATE.value,
        ]
        for machine in self.machine_table:
            machine_type = machine[TableHeader.MACHINE_TYPE.value].value
            if machine[TableHeader.MACHINE_STATE.value] == MachineState.WAITING.value:
                value = machine[TableHeader.MACHINE_STATE.value]
                state_out = f"{bcolors.OKGREEN}{value}{bcolors.ENDC}"
            else:
                value = machine[TableHeader.REMAINING.value]
                state_out = f"{bcolors.FAIL}{MachineState.USING.value} 残り {value}分{bcolors.ENDC}"
            pretty_table.add_row([machine_type, state_out])
        self.pretty_table = pretty_table

    def print(self) -> None:
        self.pretty_table.align = "l"
        self.pretty_table.hrules = prettytable.HEADER
        self.pretty_table.vrules = prettytable.NONE
        print()
        print(f"{bcolors.BOLD}{self.title}{bcolors.ENDC}")
        print()
        print(self.pretty_table)
        print()

    def print_simple(self) -> None:
        self.pretty_table.align = "l"
        self.pretty_table.hrules = prettytable.HEADER
        self.pretty_table.header = False
        self.pretty_table.border = False
        print(self.title)
        print(self.pretty_table)
