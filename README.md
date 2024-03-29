итоговое задание по курсу selenium+python (https://stepik.org/lesson/201964/step/15?unit=176022) 
запуск из терминала         
pytest -v --tb=line --language=en -m need_review


Финальный проект "Автоматизация тестирования с помощью Selenium и Python"

Данный проект создан для автоматического тестирования тестового веб-ресурса (ссылка на ресурс тестирования).
Помощь в установке окружения и запуске:

Инструкция

    Создайте новую папку, в котором будет храниться склонированный/скопированный проект:

cd *путь до вашей папки*

    Создайте новое виртуальное окружение:

py -m venv *название окружения*

    Запустите созданный приложением venv файл activate.bat, чтобы виртуальное окружение активировалось
    Установите себе данный проект одним из способов: либо скачайте и распакуйте архив, либо склонируйте репозиторий.
    Установите пакеты в окружении из файла requirements.txt. Для этого перейдите в папку со склонированным/скопированным проектом и выполните:

cd *путь до вашей папки*
pip install -r requirements.txt

    Убедитесь, что путь к chromedriver.exe прописан в PATH, либо установите драйвер для браузера. Для это перейдите на сайт и установите ту версию ChromeDriver, которая соответствует версии вашего браузера. Разархивируйте скачанный файл. Создайте в папке путь до вашей папки папку chromedriver и переместите туда файл chromedriver.exe. Для того, чтобы прописать путь к драйверу в скрипте, необходимо сделать (в данном случае не реализовано):

webdriver.Chrome(*путь к драйверу*)

    Запустите тесты в виртуальном окружении:

pytest -v --tb=line --language=*из списка реализованных на тестовом сайте* -m need_review

Последний параметр (-m) отвечает за выбор только тех тестовых сценарием, которые выбраны в качестве необходимых к показу. Если же есть необходимость запустить все тесты, достаточно просто убрать данный параметр.
Структура проекта:


    requirements.txt - список внешних зависимостей
    conftest.py - фикстура для запуска браузера (Chrome/Firefox) с выбранным параметром языка
    test_login_page.py - тесты для страницы регистрации/входа
    test_main_page.py - тесты для главной страницы
    test_product_page.py - тесты для страницы товара


    base_page.py - методы, используемые во всех других классах. Является базовым классов для работы со страницами
    basket_page.py - методы для работы со страницей корзины
    locators.py - список локаторов, используемых для поиска элементов на странице
    login_page.py - методы для работы со страницей регистрации/входа
    main_page.py - методы для работы с главной страницей
    product_page.py - методы для работы со страницей товара
