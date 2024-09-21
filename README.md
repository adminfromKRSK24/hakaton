# hakaton
- installed and available on your PYTHONPATH

```bash
source ~/.bash_profile  # или source ~/.zshrc для zsh

export PYTHONPATH=$PYTHONPATH:/Users/yourusername/Library/Python/3.12/lib/python/site-packages

```
- запуск сервера django

```bash
python3 manage.py runserver 
```

[команды с md](https://gist.github.com/Jekins/2bf2d0638163f1294637)

[репозиторий с проектом GitHub](https://github.com/adminfromKRSK24/hakaton)



python3 -m venv .venv --prompt VirtualEnv
source .venv/bin/activate
python3 -m pip install -U beautifulsoup4