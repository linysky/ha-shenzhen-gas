from __future__ import annotations

from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import ShenzhenGasApi, ShenzhenGasApiError
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class ShenzhenGasCoordinator(DataUpdateCoordinator):
    """Shenzhen Gas data coordinator."""

    def __init__(self, hass, api: ShenzhenGasApi) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=30),
        )
        self.api = api

    async def _async_update_data(self):
        try:
            data = await self.api.async_get_all()
            if data.get("failed_parts"):
                _LOGGER.warning("Gas data partially unavailable: %s", ", ".join(data["failed_parts"]))
            return data
        except ShenzhenGasApiError as err:
            raise UpdateFailed(str(err)) from err

    @property
    def latest_day(self) -> dict | None:
        days = self.days_by_date
        return days[max(days)] if days else None

    @property
    def days_by_date(self) -> dict:
        datas = (
            self.data
            .get("day_data", {})
            .get("datas", [])
            if self.data
            else []
        )

        today = datetime.now(ZoneInfo("Asia/Shanghai")).date()
        result = {}
        for row in datas:
            try:
                raw = str(row.get("readingDate", ""))
                day = date.fromisoformat(raw[:10])
            except (ValueError, AttributeError):
                continue
            if day <= today:
                result[day] = row
        return result

    def day_for(self, day: date) -> dict:
        return self.days_by_date.get(day, {})

    @property
    def internet_things(self) -> dict:
        balance = self.data.get("balance", {}) if self.data else {}

        # 接口返回结构可能是：
        # {"internetThings": {...}}
        # 也可能后续抓到的是其它嵌套，这里先兼容一层。
        return balance.get("internetThings") or balance

    @property
    def valve_status(self) -> dict:
        return self.data.get("valve_status", {}) if self.data else {}

    @property
    def bill_data(self) -> dict:
        return self.data.get("bill_data", {}) if self.data else {}
