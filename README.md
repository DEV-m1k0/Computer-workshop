# <div align="center">Сервис для компьютерной мастерской</div>

<div align="center">
  <p><h2>Мои социальные сети</h2></p>
  <a href="https://vk.com/dzh_zus" target="_blank">
    <img src="https://img.shields.io/static/v1?message=vk&logo=vk&label=&color=blue&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="youtube logo"  />
  </a>
  <a href="https://t.me/m1ko_chanel" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Telegram&logo=telegram&label=&color=2CA5E0&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="telegram logo"  />
  </a>
</div>

## Роли и их возможности

#### Будет разграничение по ролям:
1. Не авторизованный пользователь;
2. Авторизованный пользователь;
3. Сотрудник;
4. Администратор.

  

_Не авторизованный пользователь_ сможет только просматривать сайт и смотреть на ассортимент запчастей.

  

_Авторизованный пользователь_ сможет подавать заявку(в которой будет рассказывать о проблеме) и покупать запчасти, а так же смотреть на статус своей заявки(в ожидании, в процессе ремонта, готов к выдаче).

  

_Сотрудник_ сможет просматривать его заявки и выставлять статус для нее(в ожидании, в процессе починки, готов к выдаче).

  

_Администратор_ будет получать заявки от авторизованных пользователей. Он сможет как откланить, так и принять заявку. Если он принимает заявку, то должен назначить на эту заявку своего сотрудника.

  

По окончании ремонта или покупки какого-либо товара, пользователю в профиль отправиться чек, который он сможет просматреть и в дальнейшем(при желании), распечатать.


А теперь, чуточку подробнее о проекте. Весь интерфейс будет разработан на bootstrap5. Навыков у меня в красивой верстке нет, поэтому попрошу сильно не ругать! 🙂
Почему именно MySql? Ответ - просто! Я еще ни разу не работал с ним(обычно разворачивал на sqlite3 или PostrgreSql), поэтому хочу попробовать развернуть все на MySql.
Последнюю неделю, я активно изучал django_rest_framework(drf), поэтому хочу закрепить свои навыки в написании api для сайта.

## Для запуска проекта

1. Нужно клонировать этот репозиторий к себе на компьютер:
```bash
git clone https://github.com/DEV-m1k0/Computer-workshop
```
2. Создать виртульную среду:
```bash
python3 -m venv .venv
```
3.  Активировать виртуальную среду:
	1. для **macos**:
		```bash
		. .venv/bin/activate
		```
	2. для **windows**:
		Перейти в папку: .venv/scripts. И в ней будет лежать активатор
			- activate.ps
		И нам нужно его запустить

4. Скачать все библиотеки из файла requirements.txt:
```bash
pip3 install -r requirements.txt
```
5. Перейти в папку core:
```bash
cd core
```
6. Создать миграции:
```bash
python3 manage.py makemigrations
```
7. Сделать миграции для создания базы данных
```bash
python3 manage.py migrate
```
8. Запустить сам сервер:
```bash
python3 manage.py runserver
```