from typing import Optional

from main.models.phone import PhoneModel


def find_phone_by_uuid(uuid: str) -> Optional[PhoneModel]:
    return PhoneModel.query.filter(PhoneModel.uuid == uuid).first()
