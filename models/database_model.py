from peewee import *
import config


class DatabaseModel(Model):
    class Meta:
        database = config.DATABASE