from models import Student, Course, Teacher, Point, Group
from faker import Faker
from sqlalchemy.orm import Session
from configuration import engine


def seed_data(session):
    fake = Faker()

    # Create groups
    groups = [
        Group(name="Group A", student_count=0),
        Group(name="Group B", student_count=0),
        Group(name="Group C", student_count=0),
    ]
    session.add_all(groups)
    session.flush()

    # Create teachers
    teachers = [Teacher(name=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.flush()

    # Create courses
    courses = [
        Course(
            title=fake.word(),
            description=fake.text(),
            teacher_id=teachers[i % len(teachers)].id,
        )
        for i in range(8)
    ]
    session.add_all(courses)
    session.flush()

    # Create students
    students = []
    for _ in range(50):
        group = groups[fake.random_int(min=0, max=2)]
        student = Student(
            name=fake.name(), age=fake.random_int(min=18, max=30), group_id=group.id
        )
        students.append(student)
    session.add_all(students)
    session.flush()

    # Update group student_count
    for group in groups:
        group.student_count = (
            session.query(Student).filter_by(group_id=group.id).count()
        )

    # Create points (up to 20 per student per course)
    points = []
    for student in students:
        for course in courses:
            for _ in range(fake.random_int(min=1, max=20)):
                point = Point(
                    value=fake.random_int(min=0, max=100),
                    date=fake.date_time_this_year(),
                    student_id=student.id,
                    course_id=course.id,
                )
                points.append(point)
    session.add_all(points)

    session.commit()
    print("Database seeded successfully.")


if __name__ == "__main__":
    seed_data(session=Session(engine))
