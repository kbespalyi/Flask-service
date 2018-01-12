# Flask-service
# Demo on Python ecosystems

# Deployment to Codeship
`pip install -r ./product/requirements.txt`

# Build for Docker
`docker-compose up --build`
`docker-compose stop`

# Run in Docker
`docker-compose up -d`

# Deployment to Heroku

# Install the Heroku CLI
`heroku login`

# Init local
`cd Flask-service/`
`git init`

# Connect to Heroku
`heroku git:remote -a product-api-server`

# Deploy your application
`git add .`
`git commit -am "make it better"`
`git push heroku master`

`heroku container:push web -a product-api-server`
