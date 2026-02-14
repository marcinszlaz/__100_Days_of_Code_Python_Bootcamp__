`Polish version`
### INSTRUKCJA DO TWORZENIA DOCKERFILE i URUCHAMIANIA KONTENERA

### komendy w markdown :)
- `#` - naglowek, ## mniejszy naglowek itp
- `*` - myslnik, w sensie lista
- `-` - myslnik, w sensie lista
- `bactick` - to co siedzi miedzy dwoma backtickami to kod
- `akapit` - musisz klepnac 2x enter, czyli miec jedna wolna
- `**bold**` - **bold**
- `__bold__` - __bold__
- `~~strikethrough~~` - ~~strikethrough~~
- `*italic*` - *italic*
- `***italic&bold***` - ***italic&bold***
- `<u>underscore</u>` - <u>unserscore</u> nie ma natywnie<br>
trzeba pożyczyć z html

linie pomiedzy dwiema linijkami tekstu, zeby zrobic \n :)
- `2x spacja 1x enter` - nastepna linia
- `<br>` - jak z html, wymuszony enter
* ```dlugi ciag kodu``` - dlugi ciag kodu podobnie jak w python 

### komendy do stworzenia image i uruchomienia kontenera
* `docker build iss_tracker` - buduje image o nazwie None xD,iss_tracker to FOLDER
* `docker tag <id_obraza> <nazwa>:<wersja>` - zeby nadac temu nazwe robisz wlasnie tak xD
- 'docker buld -t iss_tracker:latest .` - tak sie to robi, kropka to folder bieżący, lub wpisujesz path
* `docker run -d --name iss-service --restart always -v $(pwd)/.env:/app/.env iss_tracker `  - odpala  
w trybie detach nazywa iss-service, restartuje zawsze przy error, podpina volume z .env $(pwd)  
to wyrażenie $(pwd) wkleja w path wynik komendy, NAZWA IMAGE NA KONCU ! inaczej docker bd  
probowal wykonac komendy w dockerze a nie przed jego odpaleniem
* `docker logs -f iss-service` - pokazuje logi z odpalonego kontenera

### komendy do Dockerfile
* w folderze z ktorego bedziesz tworzyl image, musi znajdować się plik Dockerfile, bez rozszerzenia  
w tym pliku ma znajdowac sie seria komend budujacych obraz warstwami
* `FROM python:3.11-slim` - FROM <nazwa_image>:<wersja_image> - kopiuje obraz z docker.hub, chyba domyslnie
* `WORKDIR /app` - ustawia workdir w dockerze - z reguly /app 
* `COPY requirements.txt .` - ta kropka na koncu to folder z WORKDIR, mozna zrobic . . wtedy wszystko w folderze
* `RUN pip install -r requirements.txt --no-cache-dir --break-system-packages` - odpala komendy inside docker :)  
, mozna miec multiple RUN(s), nocachedir - usuwa sciagniete bibsy po instalacji, --break... olewa komunikaty  
np z pip, zeby nie instalowac bibliotek na system tylko zeby to zrobic w venv ale w kontenerze to bez sensu
* `COPY main.py .env` - kopiujemy pozostale pliki, skrypt, plik z zmiennymi itp, kopiowanie env to zly zwyczaj
* `-v $(pwd)/.env:/app/.env` - tak powinno sie dodawac .env przy uruchomieniu dockera, wtedy nie masz hasel w doc
* `CMD ["python","-u","main.py"]` - mozna miec tylko jedn CMD w dockerfile, to jest ostateczne uruchomienie :)

*
*
