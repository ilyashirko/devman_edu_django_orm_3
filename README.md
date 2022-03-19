# hack_it.py 
Скрипт редактирует пользовательские данные в локальной базе данных [сайта электронного дневника](https://github.com/devmanorg/e-diary).  
Для работы скрипта необходимо иметь доступ к корневой директории вышеуказанного сайта в развернутом виде.

## Как установить скрипт

Для работы скрипта, необходимо клонировать его с репозитория git и поместить рядом с `manage.py` (зависимости должны быть уже установлены, поскольку скрипт исользует те же библиотеки, которые используются в проекте сайта):
```
$ git clone https://github.com/ilyashirko/devman_edu_django_orm_3
$ mv devman_edu_django_orm_3/hack_it.py /корневая/директория/сайта
```

## Как работать со скриптом
Перейдите в корневую директорию проекта, активируйте виртуальное окружение и запустите django shell
```
$ cd /корневая/директория/проекта
$ source env/bin/activate
$ python3 manage.py shell
```
Затем импортируйте функции скрипта. Для этого скопируйте в shell следующий код и нажмите Enter:
```
from hack_it import fix_marks, remove_chastisements, create_commendation
```
Скрипт готов к работе.  

Для того чтобы исправить оценки скопируйте следующую строку в shell указав необходимое имя ученика в формате "Фамилия Имя" и нажмите Enter:
```
fix_marks("Петров Иван")
```  
Для того чтобы удалить все замечания, скопируйте следующую строку в shell указав необходимое имя ученика в формате "Фамилия Имя" и нажмите Enter:

```
remove_chastisements("Петров Иван")
```  
Для того чтобы добавить похвалу, скопируйте следующую строку в shell указав необходимое имя ученика в формате "Фамилия Имя", предмет по которому необходим положительный комментарий и нажмите Enter:

```
create_commendation("Петров Иван", "Математика")
```

## Возможные ошибки
1. Не найдено ученика. - Вероятно вы допустили опечатку. Перезапустите функцию исправив имя или фамилию.
2. Найдено слишком много учеников. - функции работают только если нашли одного ученика, если по введенным параметрам найдено несколько учеников, возможно вам потребуется добавить в запрос отчество.
3. Не найдено предмета. - Вероятно вы допустили опечатку, проверьте правильно ли введен предмет и перезапустите функцию с исправленным предметом.