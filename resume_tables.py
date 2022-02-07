from ast import Delete
from database_engine import engine
from sqlalchemy import Column, Integer, ForeignKey, Text, delete
from sqlalchemy.orm import declarative_base



table_base = declarative_base()

class basics_information(table_base):
    __tablename__ = 'basics_information'
    id = Column(Integer, primary_key=True, autoincrement=True)
    coverLetter = Column(Text)
    name = Column(Text)
    label = Column(Text)
    image = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    address = Column(Text)
    postalCode = Column(Text)
    city = Column(Text)
    countryCode = Column(Text)
    region = Column(Text)
    url = Column(Text)
    summary = Column(Text)
    

class basics_profiles(table_base):
    __tablename__ = 'basics_profiles'
    profileId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    network = Column(Text)
    username= Column(Text)
    url = Column(Text)
    
class work(table_base):
    __tablename__ = 'work'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    workId = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text)
    location = Column(Text)
    description = Column(Text)
    position = Column(Text)
    url = Column(Text)
    startDate = Column(Text)
    endDate = Column( Text)
    summary = Column(Text)
    highlights = Column(Text)
    keywords = Column(Text)

class volunteer(table_base):
    __tablename__ = 'volunteer'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    volunteerId = Column(Integer,primary_key=True, nullable=False)
    organization = Column(Text)
    position = Column(Text)
    url = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    summary = Column(Text)
    highlights = Column(Text)

class education(table_base):
    __tablename__ = 'education'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    educationId = Column(Integer,primary_key=True, nullable=False)
    institution = Column(Text)
    url = Column(Text)
    area = Column(Text)
    studyType = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    score = Column(Text)

class education_courses(table_base):
    __tablename__ = 'education_courses'
    coursesId = Column(Integer, primary_key=True, autoincrement=True)
    educationId = Column(Integer, ForeignKey("education.educationId"), nullable=False)
    value = Column(Text)

class awards(table_base):
    __tablename__ = 'awards'
    awardsId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    title = Column(Text)
    date = Column(Text)
    awarder = Column(Text)
    summary = Column(Text)

class certificates(table_base):
    __tablename__ = 'certificates'
    certificatesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    name = Column(Text)
    date = Column(Text)
    url = Column(Text)
    issuer = Column(Text)

class publications(table_base):
    __tablename__ = 'publications'
    publicationsId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    name = Column(Text)
    publisher = Column(Text)
    releaseDate = Column(Text)
    url = Column(Text)
    summary = Column(Text)

class skills(table_base):
    __tablename__ = 'skills'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    skillsId = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text)
    level = Column(Text)
    keywords = Column(Text)

class languages(table_base):
    __tablename__ = 'languages'
    languagesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    language = Column(Text)
    fluency = Column(Text)

class interests(table_base):
    __tablename__ = 'interests'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    interestsId = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text)
    keywords = Column(Text)

class references(table_base):
    __tablename__ = 'references'
    referenecesId = Column(Integer, primary_key=True, autoincrement=True)
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    name = Column(Text)
    reference = Column(Text)

class projects(table_base):
    __tablename__ = 'projects'
    resumeId = Column(Integer, ForeignKey("basics_information.id"), nullable=False)
    projectsId = Column(Integer, primary_key=True, nullable=False)
    name= Column(Text)
    description = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    url = Column(Text)
    entity = Column(Text)
    type = Column(Text)
    highlights = Column(Text)
    keywords = Column(Text)
    roles = Column(Text)



table_base.metadata.create_all(engine)