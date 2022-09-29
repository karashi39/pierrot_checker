import enum


class TableHeader(enum.Enum):
    MACHINE_NUMBER = "機械番号"
    MACHINE_TYPE = "機種名"
    MACHINE_STATE = "稼働状況"
    REMAINING = "残り運転時間"
    SIZE = "容量"
    MACHINE = "機器"
    HOGE = "機別"


class MachineState(enum.Enum):
    WAITING = "空き"
    USING = "使用中"


class MachineType(enum.Enum):
    DRYER_S = "小型乾燥機"
    DRYER_M = "中型乾燥機"
    DRYER_L = "大型乾燥機"
    WASHING_DRYER_S = "小型洗濯乾燥機"
    WASHING_DRYER_M = "中型洗濯乾燥機"
    WASHING_DRYER_L = "大型洗濯乾燥機"
    WASHING_S = "小型洗濯機"
    WASHING_M = "中型洗濯機"
    WASHING_L = "大型洗濯機"
    SHOE_DRYER = "スニーカードライヤー"
    SHOE_WASHING = "スニーカーウォッシャー"
