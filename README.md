# Tidyup - a Todo list with a twist

Tidyup is a simple todo list application. however the completion has to be signed off with a picture of the completed task. Users can also see the memories of the tasks they completed in a scrapbook type UI.

https://savetimewithus.herokuapp.com/

## Installation

git clone the repository to create a local deployment.

```bash
git clone https://github.com/vijay-jaisankar/tidy-up.git
pipenv shell 
pipenv install
cd tidyhacks
python manage.py makemigrations
python manage.py migrate 
python manage.py createsuperuser
python manage.py runserver
```

## Tech Stack
<ul>
  <li><strong>Backend:</strong> Django,Django-rest-framework</li>
  <li><strong>Frontend:</strong> HTML5,CSS,JS,Bootstrap5</li>
</ul>


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
