# opgraph
Веб-сервис для получения Open Graph произвольной страницы в интернете в формате JSON

### usage
Запрос через GET-запрос: ?url=http://

### Примеры:
Запрос: http://localhost:5000/?url=http://github.com/
Результат:
{"url": "https://github.com", "site_name": "GitHub", "title": "Build software better, together", "description": "GitHub is where people build software. More than 50 million people use GitHub to discover, fork, and contribute to over 100 million projects.", "image": "https://github.githubassets.com/images/modules/open_graph/github-octocat.png", "image:type": "image/png", "image:width": "1200", "image:height": "620"}

Запрос: http://localhost:5000/?url=https://stackoverflow.com/questions/
Результат:
{"type": "website", "url": "https://stackoverflow.com/questions/", "site_name": "Stack Overflow", "image": "https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded", "title": "Newest Questions", "description": "Stack Overflow | The World’s Largest Online Community for Developers"}

### Для тестирования доступна Online-версия: http://139.59.210.125:5000/
