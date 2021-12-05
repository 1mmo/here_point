# here_point


# Install
#### In your command line:
    git clone git@github.com:1mmo/here_point.git
    cd here_point/

# Settings

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

# Start Docker
  
    # docker-compose up -d --build
    

# Note

    # To launch the site next time:
    docker-compose up -d
    
