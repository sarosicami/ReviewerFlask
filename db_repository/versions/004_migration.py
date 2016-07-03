from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('brand', String(length=200)),
    Column('product_model', String(length=200)),
    Column('processor', String(length=300)),
    Column('display', Integer),
    Column('ram_memory', String(length=200)),
    Column('memory_speed', Integer),
    Column('hard_drive', Integer),
    Column('video_card', String(length=200)),
    Column('card_description', String(length=100)),
    Column('battery_life', Integer),
    Column('item_weight', Integer),
    Column('housing_material', String(length=100)),
    Column('color', String(length=100)),
    Column('operating_system', String(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['product'].columns['ram_memory'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['product'].columns['ram_memory'].drop()
