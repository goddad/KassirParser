#KassirParser парсер для https://kassir.ru events

<h3>Установка:</h3>
<h5>1. Скачать файлы в одну директорию;</h5>
<h5>2. Сделать файлы .py и .sh исполняемыми:</h5>
chmod +x kassir_funzone_parser.py<br/>
chmod +x run_parser.sh
<h5>3. В файле run_parser.sh поменять параметры запуска *.py скрипта(на url мероприятия и наименование сектора)</h5>
например, если есть желание узнать, когда появятся билеты в фан-зону на концерт металлики, нужно будет прописать:<br/>
#!/bin/bash<br/>
python3 kassir_funzone_parser.py https://metallica.kassir.ru/koncert/metallica ФАН >> log.txt 2>> error_log.txt

то же на металлику, только в сектор D 223:<br/>
#!/bin/bash<br/>
python3 kassir_funzone_parser.py https://metallica.kassir.ru/koncert/metallica 'D 223' >> log.txt 2>> error_log.txt

<h5>4. Задать интервал в кроне:</h5>
crontab -e<br/>
*/20 * * * * /path/to/run_parser.sh - парсер будет запускаться каждые 20 минут<br/>
нажать Esc и прописать :wq

<h3>Принцип работы:</h3>
В случае добавления новой партии билетов в интересующий вас сектор, в системе сработает широковещательное сообщение
с информацией о них.
