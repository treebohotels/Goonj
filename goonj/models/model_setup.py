from goonj.models.constants import DatabaseType
from goonj.models.models import Tag, SmartAlert

models_list = [SmartAlert, Tag]


def init_database(db_settings, app_name="default"):
    """
    Initialze the database
    :param db_settings: 
    :param app_name
    :return: 
    """

    db_handler = DatabaseType.db_mapping.get(db_settings.db_type)

    if not db_handler:
        raise KeyError("Invalid db type: {}".format(db_settings.db_type))

    db = db_handler(db_settings.db_name, db_settings.db_configuration)

    for model in models_list:
        model._meta.database = db
        model._meta.db_table = model.__name__.lower()

    db.connect()

    db.create_tables(models_list, safe=True)

    return db
