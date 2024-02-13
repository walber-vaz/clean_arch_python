from src.infra.db.settings.connection import DBConnectionHandler


def test_create_database_engine():
    engine = DBConnectionHandler().get_engine()

    assert engine is not None
