from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('brand', String(length=200)),
    Column('product_model', String(length=200)),
    Column('model_number', String(length=200)),
    Column('processor', String(length=300)),
    Column('display', String(length=100)),
    Column('RAM_memory', String(length=200)),
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

review = Table('review', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String),
    Column('timestamp', DateTime),
    Column('product_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    post_meta.tables['product'].create()
    post_meta.tables['review'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    post_meta.tables['product'].drop()
    post_meta.tables['review'].drop()
