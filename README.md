# here_point

# Description 📝
The idea of the project is to create a website for travelers.
Anyone who has ever used default sites with city sights knows that this is a trap and it is often boring there. The authors of such sites may have never been to this city, but at the same time they advise you to visit some museum or monument. All because these are standard entertainments in absolutely any city.

Those who travel often understand how nice it is to find places that are not accessible to tourists. Such places are known to the inhabitants of this city, while tourists have to look for them at random. . We need to give everyone the opportunity to talk about their favorite place. Let him take photos, write how to get to this place and put a mark on the map

### Main page
The site has a main page that shows random places around the world, each place has an author, rating, photos, description and coordinates.


<img src="https://user-images.githubusercontent.com/79962819/183054999-6cb97fb4-7855-4092-905d-f2ee44c5c1fe.jpg" width="800">

### User page
The user's page consists of his photo, information about him, which he can change if necessary, and of course the places he uploaded 

<img src="https://user-images.githubusercontent.com/79962819/183058870-07e293ad-2659-4db8-a904-f836c73ffc38.jpg" width="800">

<img src="https://user-images.githubusercontent.com/79962819/183056647-caa66826-dc93-42c2-a208-2eed5cf7aa74.jpg" width="800">

### Adding new places
Each user can add their place

<img src="https://user-images.githubusercontent.com/79962819/183059461-69c5b142-7ecf-4e3b-898a-deaed8eaeb30.jpg" width="800">




# Install 🔧
#### In your command line:
    git clone git@github.com:1mmo/here_point.git
    cd here_point/

# Settings ⚙️

    # create .env file
    touch .env # Linux
    
    # Open .env and write:
    DEBUG=1
    SECRET_KEY='from Dajngo settings'
    ALLOWED_HOSTS=host
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DB=your_postgres_db
    POSTGRES_USER=your_user
    POSTGRES_PASSWORD=your_password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    DATABASE=postgres

### Start Docker
  
    # docker-compose up -d --build

### Migrations

    # docker-compose exec web python manage.py migrate
    
### Note

    # To launch the site next time:
    docker-compose up -d
    
