# Мониторинг сайтов

Скрипт позволяет сделать проверки о состоянии ваших сайтов, проверить ответы сервера на HTTP запрос, а также проверяет доменное имя сайта, выводит срок действия домена, и проверяет проплачен ли домен минимум на 1 месяц вперед, если нет, то выдается отдельный статус. Если домен незарегистрирован, то выдаётся соответствующий ответ.

Скрипт принимает на входе файл, где построчно вставлены ссылки на сайты, которые нужно проверять. 
Пример текстового файла:

```
https://devman.org
https://gith45433534b.com
http://krovatka.ru
```


**Пример использования:**
Передача пути до файла в параметрах запуска скрипта:
```
python check_sites_health.py urls.txt
```
ответ:
```
https://devman.org  responds with status 200: True
Status is OK: True domain will expire in 167 days.
Cant find https://gith45433534b.com
http://krovatka.ru  responds with status 200: True
Status is OK: True domain will expire in 232 days.
```


**Установка дополнительных пакетов:**

Для корректоной работы скрипта необходимо установить следующие модули:
* **python-whois** - для запроса даты истечения срока регистрации.
* **http1** - для работы с HTTP запросом.

Пакеты устанавливаются по команде `pip install -r requirements.txt`.
