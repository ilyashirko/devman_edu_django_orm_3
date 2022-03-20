import random

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid, Subject)

COMMENDATIONS = (
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
)


def find_student(student_name):
    try:
        return Schoolkid.objects.get(full_name__contains=student_name.title())
    except Schoolkid.DoesNotExist:
        print('Sorry, there is no this student.')
    except Schoolkid.MultipleObjectsReturned:
        print('Sorry, too much students found.')
        for student in Schoolkid.objects.filter(full_name__contains=student_name.title()):
            print(student.full_name)



def fix_marks(student_name):
    schoolkid = find_student(student_name)
    if schoolkid:
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        for mark in bad_marks:
            mark.points = 5
            mark.save()


def remove_chastisements(student_name):
    schoolkid = find_student(student_name)
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        for chastisement in chastisements:
            chastisement.delete()


def create_commendation(student_name, subject_title):
    schoolkid = find_student(student_name)
    if not schoolkid:
        return
    
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter

    try:
        subject = Subject.objects.get(
            title=subject_title.title(),
            year_of_study=year_of_study
        )
    except Subject.DoesNotExist:
        print('There is no such subject.')
        return

    lesson = Lesson.objects.filter(
        subject=subject,
        year_of_study=year_of_study,
        group_letter=group_letter
    ).last()

    commendation = random.choice(COMMENDATIONS)
    
    Commendation.objects.create(
        text=commendation,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=subject,
        teacher=lesson.teacher
    )
