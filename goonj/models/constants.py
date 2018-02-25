from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase


class DatabaseType(object):
    """The supported batabase type"""

    MYSQL_DATABASE = "mysql"
    POSTGRESQL_DATABASE = "postgresql"
    SQLITE_DATABASE = "sqlite"

    db_mapping = {
        MYSQL_DATABASE: MySQLDatabase,
        POSTGRESQL_DATABASE: PostgresqlDatabase,
        SQLITE_DATABASE: SqliteDatabase
    }
