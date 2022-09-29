from enums import MachineType


def get_target_machine_types(targets: str) -> list[MachineType]:
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
