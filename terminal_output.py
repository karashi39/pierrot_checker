from typing import Any, Optional

from enums import TableHeader, MachineState, MachineType


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
    title: str = "OUTPUT"
    machine_table: dict[str, Any]

    def __init__(self, title: str, machine_table: dict[str, Any]) -> None:
        self.title = title
        self.machine_table = machine_table

    def print(self) -> None:
        print(self.title)
        for machine in self.machine_table:
            machine_type = machine[TableHeader.MACHINE_TYPE.value].value
            if machine[TableHeader.MACHINE_STATE.value] == MachineState.WAITING.value:
                value = machine[TableHeader.MACHINE_STATE.value]
                state_out = f"{bcolors.OKGREEN}{value}{bcolors.ENDC}"
            else:
                value = machine[TableHeader.REMAINING.value]
                state_out = f"{bcolors.FAIL}{MachineState.Using.value} 残り {value}分{bcolors.ENDC}"
            print(f"{machine_type} {state_out}")


def get_target_machine_types(targets: str) -> Optional[list[MachineType]]:
    target_machine_types = []
    if "w" in targets:
        if "s" in targets:
            target_machine_types += [MachineType.WASHING_S]
        if "m" in targets:
            target_machine_types += [MachineType.WASHING_M]
        if "l" in targets:
            target_machine_types += [MachineType.WASHING_L]
        if not any([x in targets for x in ("s", "m", "l")]):
            target_machine_types += [MachineType.WASHING_S]
            target_machine_types += [MachineType.WASHING_M]
            target_machine_types += [MachineType.WASHING_L]
    if "d" in targets:
        if "s" in targets:
            target_machine_types += [MachineType.DRYER_S]
        if "m" in targets:
            target_machine_types += [MachineType.DRYER_M]
        if "l" in targets:
            target_machine_types += [MachineType.DRYER_L]
        if not any([x in targets for x in ("s", "m", "l")]):
            target_machine_types += [MachineType.DRYER_S]
            target_machine_types += [MachineType.DRYER_M]
            target_machine_types += [MachineType.DRYER_L]
    if "a" in targets:
        if "s" in targets:
            target_machine_types += [MachineType.WASHING_DRYER_S]
        if "m" in targets:
            target_machine_types += [MachineType.WASHING_DRYER_M]
        if "l" in targets:
            target_machine_types += [MachineType.WASHING_DRYER_L]
        if not any([x in targets for x in ("s", "m", "l")]):
            target_machine_types += [MachineType.WASHING_DRYER_S]
            target_machine_types += [MachineType.WASHING_DRYER_M]
            target_machine_types += [MachineType.WASHING_DRYER_L]
    if "z" in targets:
        target_machine_types += [MachineType.SHOE_WASHING, MachineType.SHOE_DRYER]
    return target_machine_types