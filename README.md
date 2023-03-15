# metaanchor-framework
A framework to work with Authentic Vision Meta Anchor (tm) Technology

# SETUP
1. Download the complete directory as zip and unpack it on your webserver (or git clone)
1. Replace the `backend/conf/metaanchor.json` with the `metaanchor.json` you received from us. __Make sure to never check this to public repositories or repositories at all, as it contains secret keys and API-keys that would compromise your complete collection`
1. Adapt public-exposed ports (5557 and 5558 per default) in `docker-compose.yml` 
1. Adapt `VUE_APP_BASE_URL` in `frontend/.env` to reflect your webservers public address and the backend-port (default: 5557) you configured in the step before
1. Run `sudo docker-compose build && sudo docker-compose up -d`. This takes a few minutes and builds everything as well as starts it in the background
  1. In case you need to debug, use `sudo docker logs --follow metaanchor_backend` and `sudo docker logs --follow metaanchor_frontend` respectively
