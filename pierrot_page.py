from typing import Any

from bs4 import BeautifulSoup

PIERROT_URL = "https://laundry.senkaq.com/shop/tokyo/tachikawa-shi"

from enums import MachineType, TableHeader
from get_page_body import get_page_body


class PierrotPage:

    store_number: int
    url: str
    body_soup: BeautifulSoup

    def __init__(self, store_number: int):
        self.store_number = store_number
        self.url = f"{PIERROT_URL}/{str(store_number + 1219)}/"
        self.body_soup = BeautifulSoup(get_page_body(self.url), "html.parser")

    def get_store_name(self) -> str:
        return self.body_soup.find("h1").get_text(strip=True)

    def get_machines_table(self) -> list[dict[str, Any]]:
        div = self.body_soup.select_one("div#kado_status")
        if div is None:
            div = self.body_soup.select_one("div.kado-table")
        trs = div.select_one("table").select("tr")

        headers = [th.get_text(strip=True) for th in trs[0].select("th")]
        trs.pop(0)  # omit header row

        machine_table = []
        for tr in trs:
            tds = tr.select("td")
            row = {}
            for i, td in enumerate(tds):
                header = TableHeader(headers[i]).value
                if header == TableHeader.MACHINE_TYPE.value:
                    row[header] = MachineType(
                        td.get_text(strip=True).split(" ")[0].split("　")[0]
                    )
                else:
                    row[header] = td.get_text(strip=True)
            machine_table.append(row)
        return machine_table
