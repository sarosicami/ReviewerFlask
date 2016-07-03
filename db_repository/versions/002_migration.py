from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
product = Table('product', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('brand', VARCHAR(length=200)),
    Column('product_model', VARCHAR(length=200)),
    Column('processor', VARCHAR(length=300)),
    Column('display', INTEGER),
    Column('RAM_memory', VARCHAR(length=200)),
    Column('memory_speed', INTEGER),
    Column('hard_drive', INTEGER),
    Column('video_card', VARCHAR(length=200)),
    Column('card_description', VARCHAR(length=100)),
    Column('battery_life', INTEGER),
    Column('item_weight', INTEGER),
    Column('housing_material', VARCHAR(length=100)),
    Column('color', VARCHAR(length=100)),
    Column('operating_system', VARCHAR(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['product'].columns['RAM_memory'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['product'].columns['RAM_memory'].create()
