# Django upload multiple files

Upload multiple files with API and update file and upload time when file already exists.

Check more detail in my blog post [Django Multiple Files Upload](https://blueswen.github.io/2020/07/10/django-multiple-files-upload/).

## Requirements

1. django>=3.0.7
2. djangorestframework>=3.11.0

## Usage

1. Run server

    ```bash
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py run server 6001
    ````

2. Upload files in [http://localhost:6001/upload/](http://localhost:6001/upload/)
3. Check files data and download by result's url in [http://localhost:6001/api/files/](http://localhost:6001/api/files/)
