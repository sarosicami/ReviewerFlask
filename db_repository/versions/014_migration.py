from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
opinion = Table('opinion', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR),
    Column('aspect', VARCHAR),
    Column('category', VARCHAR),
    Column('emotion', VARCHAR),
    Column('polarity', VARCHAR),
    Column('review_id', INTEGER),
)

opinion = Table('opinion', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String),
    Column('aspect', String),
    Column('attribute', String),
    Column('emotion', String),
    Column('polarity', String),
    Column('review_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['opinion'].columns['category'].drop()
    post_meta.tables['opinion'].columns['attribute'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['opinion'].columns['category'].create()
    post_meta.tables['opinion'].columns['attribute'].drop()
