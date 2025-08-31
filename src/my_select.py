from configuration import engine
from sqlalchemy import text, select, func
from sqlalchemy.orm import Session

from models import Point, Course, Student, Teacher


def get_top_students(session: Session, limit: int = 5):
    sql = (
        select(Point.student_id, func.avg(Point.value))
        .group_by(Point.student_id)
        .order_by(func.avg(Point.value).desc())
        .limit(limit)
    )
    result = session.execute(sql).all()
    return result


def get_top_student_by_course(session: Session, course_id: int):
    sql = (
        select(Course.title, Student.name, func.avg(Point.value))
        .join(Course, Course.id == Point.course_id)
        .join(Student, Student.id == Point.student_id)
        .where(Point.course_id == course_id)
        .group_by(Course.title, Student.name)
        .order_by(func.avg(Point.value).desc())
    )
    result = session.execute(sql).first()
    return result


def get_avg_points_by_course(session: Session, course_id: int):
    sql = (
        select(Course.title, func.avg(Point.value))
        .join(Course, Course.id == Point.course_id)
        .where(Point.course_id == course_id)
        .group_by(Course.title)
    )
    result = session.execute(sql).first()
    return result


def get_avg_for_all_courses(session: Session):
    sql = (
        select(Course.title, func.avg(Point.value))
        .join(Course, Course.id == Point.course_id)
        .group_by(Course.title)
    )
    result = session.execute(sql).all()
    return result


def get_teacher_courses(session: Session, teacher_id: int):
    sql = (
        select(Teacher.name, Course.title)
        .join(Course, Course.teacher_id == Teacher.id)
        .where(Teacher.id == teacher_id)
    )
    result = session.execute(sql).all()
    return result


def get_students_list_by_course(session: Session, course_id: int):
    sql = (
        select(Course.title, Student.name)
        .join(Point, Course.id == Point.course_id)
        .join(Student, Student.id == Point.student_id)
        .where(Point.course_id == course_id)
        .group_by(Course.title, Student.name)
    )
    result = session.execute(sql).all()
    return result


def get_scores_in_group_by_course(session: Session, group_id: int, course_id: int):
    sql = (
        select(Student.name, Course.title, Point.value)
        .join(Point, Student.id == Point.student_id)
        .join(Course, Course.id == Point.course_id)
        .where(Student.group_id == group_id, Point.course_id == course_id)
    )
    result = session.execute(sql).all()
    return result


def get_avg_score_by_teacher(session: Session, teacher_id: int):
    sql = (
        select(Teacher.name, func.avg(Point.value))
        .join(Course, Course.teacher_id == Teacher.id)
        .join(Point, Point.course_id == Course.id)
        .where(Teacher.id == teacher_id)
        .group_by(Teacher.name)
    )
    result = session.execute(sql).first()
    return result


def get_list_of_courses_by_student(session: Session, student_id: int):
    sql = (
        select(Student.name, Course.title)
        .join(Point, Student.id == Point.student_id)
        .join(Course, Course.id == Point.course_id)
        .where(Student.id == student_id)
        .group_by(Student.name, Course.title)
    )
    result = session.execute(sql).all()
    return result


def get_list_of_courses_for_student_by_teacher(
    session: Session, student_id: int, teacher_id: int
):
    sql = (
        select(Student.name, Teacher.name, Course.title)
        .join(Point, Student.id == Point.student_id)
        .join(Course, Course.id == Point.course_id)
        .join(Teacher, Teacher.id == Course.teacher_id)
        .where(Student.id == student_id, Teacher.id == teacher_id)
        .group_by(Student.name, Teacher.name, Course.title)
    )
    result = session.execute(sql).all()
    return result


if __name__ == "__main__":

    with Session(engine) as session:
        result1 = get_top_students(session)
        print(result1)
        print("-----" * 20)
        result2 = get_top_student_by_course(session, course_id=1)
        print(result2)
        print("-----" * 20)
        result3 = get_avg_points_by_course(session, course_id=2)
        print(result3)
        print("-----" * 20)
        result4 = get_avg_for_all_courses(session)
        print(result4)
        print("-----" * 20)
        result5 = get_teacher_courses(session, teacher_id=2)
        print(result5)
        print("-----" * 20)
        result6 = get_students_list_by_course(session, course_id=1)
        print(result6)
        print("-----" * 20)
        result7 = get_scores_in_group_by_course(session, group_id=3, course_id=1)
        print(result7)
        print("-----" * 20)
        result8 = get_avg_score_by_teacher(session, teacher_id=2)
        print(result8)
        print("-----" * 20)
        result9 = get_list_of_courses_by_student(session, student_id=1)
        print(result9)
        print("-----" * 20)
        result10 = get_list_of_courses_for_student_by_teacher(
            session, student_id=1, teacher_id=2
        )
        print(result10)
        print("-----" * 20)
