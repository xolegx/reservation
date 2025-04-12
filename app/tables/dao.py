from app.dao.base import BaseDAO

from app.tables.models import Table


class TablesDAO(BaseDAO):
    model = Table
