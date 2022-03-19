import random

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

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


def fix_marks(student_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=student_name.title())
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        for mark in bad_marks:
            mark.points = 5
            mark.save()
    except ObjectDoesNotExist:
        return 'Sorry, there is no this student.'
    except MultipleObjectsReturned:
        print('Sorry, too much students found.')
        for student in Schoolkid.objects.filter(full_name__contains=student_name.title()):
            print(student.full_name)


def remove_chastisements(student_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=student_name.title())
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        for chastisement in chastisements:
            chastisement.delete()
    except ObjectDoesNotExist:
        return 'Sorry, there is no this student.'
    except MultipleObjectsReturned:
        return 'Sorry, too much students found.'


def create_commendation(student_name, subject_title):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=student_name.title())
    except ObjectDoesNotExist:
        return 'Not found requested student!'
    except MultipleObjectsReturned:
        return 'Sorry, too much students found.'

    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter

    try:
        subject = Subject.objects.get(
            title=subject_title.title(),
            year_of_study=year_of_study
        )
    except ObjectDoesNotExist:
        return 'There is no such subject.'

    lesson = random.choice(
        Lesson.objects.filter(
            year_of_study=year_of_study,
            group_letter=group_letter,
            subject=subject
        )
    )

    commendation = random.choice(COMMENDATIONS)

    Commendation.objects.create(
        text=commendation,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=subject,
        teacher=lesson.teacher
    )
