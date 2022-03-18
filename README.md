# hack_it.py 
Скрипт редактирует пользовательские данные в локальной базе данных сайта

Для работы скрипт поместить рядом с `manage.py`, активировать виртуальное окружение и открыть django shell:
```
$ python3 manage.py shell
```
импортируйте необходимые команды в открывшейся командной строке и запустите их с необходимыми параметрами:  
```
from hack_it import fix_marks, remove_chastisements, create_commendation

fix_marks("Петров Иван")
remove_chastisements("Петров Иван")
create_commendation("Петров Иван", "Математика")
```