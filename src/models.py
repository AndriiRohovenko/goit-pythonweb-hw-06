from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    student_count: Mapped[int]
    students: Mapped[list["Student"]] = relationship(back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    age: Mapped[int]
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(back_populates="students")
    points: Mapped[list["Point"]] = relationship(back_populates="student")


class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    courses: Mapped[list["Course"]] = relationship(back_populates="teacher")


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    teacher: Mapped["Teacher"] = relationship(back_populates="courses")
    points: Mapped[list["Point"]] = relationship(back_populates="course")


class Point(Base):
    __tablename__ = "points"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    value: Mapped[int]
    date: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    student: Mapped["Student"] = relationship(back_populates="points")
    course: Mapped["Course"] = relationship(back_populates="points")
