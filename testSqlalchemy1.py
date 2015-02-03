#-------------------------------------------------------------------------------
# Name:        testSqlalchemy1
# Purpose:
#
# Author:      Administrator
#
# Created:     03/02/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#------------------------------------------------------------------------------gr
from sqlalchemy import create_engine,ForeignKey,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,Integer,String,DateTime,Boolean

import sqlalchemy.orm as o


engine = create_engine('mssql+pymssql://sa:123456@localhost:1433/test',echo=True)

Base = declarative_base()
metadata=Base.metadata

class User(Base):
    __tablename__='user'
    id = Column(Integer,primary_key=True)
    name = Column(String(200),nullable=False)

    def __repr__(self):
        return "<User(id='%s' , name='%s')>" % \
        (self.id,self.name)

metadata.create_all(bind=engine)

Session=o.sessionmaker(bind=engine)
s=Session()


#lucy=User(name='lucy')
#s.add(lucy)
#s.commit()

#users=[User(name='maven'),User(name='fang')]
#s.add_all(users)
#s.commit()
#
#fang=s.query(User).filter(User.name=='fang').first()
#print fang
#users=fang=s.query(User.name=='fang').count()
#print count


