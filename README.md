# Запуск тестов (runtests.sh)
Для запуска скирпта "runtests.sh" нужно сначала сделать его исполняемым, выполнив команду "chmod u+x ./runtests.sh", затем запустить с помощью команды "./runtests.sh". В директории, из которой происходит запуск скрипта должна находится папака "Tests" с тестовыми данными.
# Запуск генератора тестов (generator.py)
Порграмма генерирует диреткории и пустые файлы в заданном количестве, затем заполняет файлы заданными данными. На вход подаются 5 чисел, каждое с новой строки: 
1. Количество файлов в каждой директории
2. Количество вложенных директорий (содержат только папки, файлов не содержат)
3. Количество директорий, которые содержатся в каждой вложенной директории
4. Номер файла, с которого нужно будет начать поиск файла-минотавра (допустимые рамки значений номера файла будут выведены на экран)
5. Номер файла, содержащего адреса каждого уже созданного пустого файла и содержимое, которым заполнятся эти пустые файлы. Название файла, содержащего адреса и содержимое всех файлов, отвечает следующей структуре: input_file#.txt, где # - номер файла.
На выходе программы будет информация о том, удалось ли создать корневую папку с файлами или нет.
Запуск программы происходит с помощью команды "python ./generator.py"
# Запуск поиска файла-минотавра (minotaur.py)
Программа запускается командой "python ./minotaur.py"
Для поиска файла-минотавра в директории, из которой запускается программа должна существовать корневая папка root, содержащая папки и файлы. Входных данных нет, на выходе - последовательность путей файлов, которая привела к поимке файла-минотавра.
