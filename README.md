# Мониторинг сайтов

Скрипт позволяет сделать проверки о состоянии ваших сайтов, проверить ответы сервера на HTTP запрос, а также проверяет доменное имя сайта, выводит срок действия домена, и проверяет проплачен ли домен минимум на 1 месяц вперед, если нет, то выдается отдельный статус. Если домен незарегистрирован, то выдаётся соответствующий ответ.

Скрипт принимает на входе файл, где построчно вставлены ссылки на сайты, которые нужно проверять. 
Пример текстового файла:

```
https://github.com
https://devman.org
https://ru.wikipedia.org
https://yandex.ru
https://slack.com
```


**Пример использования:**
Передача пути до файла в параметрах запуска скрипта:
```
python check_sites_health.py urls.txt
```
ответ:
```
https://github.com  responds with status: 200
Status is OK domain will expire in 952  days
https://devman.org  responds with status: 200
Status is OK domain will expire in 178  days
https://ru.wikipedia.org  responds with status: 200
Status is OK domain will expire in 1777  days
https://yandex.ru  responds with status: 200
Status is OK domain will expire in 212  days
https://slack.com  responds with status: 200
Status is OK domain will expire in 596  days
```


**Установка дополнительных пакетов:**

Для корректоной работы скрипта необходимо установить следующие модули:
* **python-whois** - для запроса даты истечения срока регистрации.
* **http1** - для работы с HTTP запросом.

Пакеты устанавливаются по команде `pip install -r requirements.txt`.
