`Ярощук Александр Михайлович ИПЗ 4.04`
## Docker

## Start the project
Для начала склонируем проект todo.
```
git clone https://github.com/docker/getting-started-todo-app
```
Дальше перейдем в папку с проектом.
```
cd getting-started-todo-app
```
Дальше разворачиваем приложение и запускаем контейнер, с помощью watch можно отслеживать изменение в проекте и автоматически обновлять службы.
```
docker compose watch
```
![ScreenShot1](screenshots/Screenshot_1.jpg)

После успешного запуска контейнеров, мы сможем зайти на http://localhost.

![ScreenShot2](screenshots/Screenshot_2.jpg)

Можно для примера добавить пару заданий.

![ScreenShot3](screenshots/Screenshot_3.jpg)

## Make changes to the app

Теперь когда проект успешно заработал, мы можем изменять его как хотим.

Например:

Открыв файл `backend/src/routes/getGreeting.js`

Мы можем изменить стандартное приветсвие "Hello world!"
```
const GREETINGS = [
    "Whalecome!",
    "All hands on deck!",
    "Charting the course ahead!",
];
module.exports = async (req, res) => {
    res.send({
        greeting: GREETINGS[ Math.floor( Math.random() * GREETINGS.length )],
    });
};
```
![ScreenShot4](screenshots/Screenshot_4.jpg)

Теперь у нас рандомно будут выбираться приветсвие из списка.

![ScreenShot5](screenshots/Screenshot_5.jpg)

Так же мы можем изменить например цвет фона сайта.

Открыв файл `client/src/index.scss`

![ScreenShot6](screenshots/Screenshot_6.jpg)
![ScreenShot7](screenshots/Screenshot_7.jpg)

## Build and push the image

1. Для начала зайдем на https://hub.docker.com/.
2. Теперь создаем репозиторий с название `getting-started-todo-app` 

![ScreenShot9](screenshots/Screenshot_9.jpg)

Теперь можем сделать образ нашего проекта

```docker build -t babykiwii/getting-started-todo-app .```

![ScreenShot8](screenshots/Screenshot_8.jpg)

Для проверки уже сужествующих билдов можем написать команду

`docker image ls`

Дальше мы отправляем наш образ на docker hub.

`docker push DOCKER_USERNAME/getting-started-todo-app`

После успешной отправки наш образ появляется на раннее созданном репозитории, и теперь мы можем передавать.

![ScreenShot10](screenshots/Screenshot_10.jpg)

