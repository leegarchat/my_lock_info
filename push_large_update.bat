@echo off
chcp 65001

:: Получаем переданную версию через аргументы
set VERSION=%1

:: Проверка на переданную версию
if "%VERSION%"=="" (
    echo Ошибка: Не указана версия.
    exit /b 1
)

:: Инициализируем Git LFS
git lfs install

:: Добавляем файлы для Linux и Windows с переданной версией
git add .\updates\Linux_АвтозапросыГаз_А%VERSION%
git add .\updates\Win_АвтозапросыГаз_А%VERSION%.exe

:: Создаем коммит с сообщением, содержащим переданную версию
git commit -m "Настроил LFS для большого файла версии %VERSION%"

:: Отправляем изменения в основной репозиторий
git push origin main

:: Завершаем выполнение
echo Операция завершена успешно.
pause