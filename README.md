# metaanchor-framework
A framework to work with Authentic Vision Meta Anchor (tm) Technology

# SETUP
1. Download the complete directory as zip and unpack it on your webserver (or git clone)
  1. `curl https://github.com/tbergmueller/metaanchor-framework/archive/refs/heads/stub.zip && unzip stub.zip`
  1. Rename directory if needed  
1. Replace the `backend/conf/metaanchor.json` with the `metaanchor.json` you received from us. __Make sure to never check this to public repositories or repositories at all, as it contains secret keys and API-keys that would compromise your complete collection`
1. Adapt public-exposed ports (5557 and 5558 per default) in `docker-compose.yml` 
1. Adapt `VUE_APP_BASE_URL` in `frontend/.env` to reflect your webservers public address and the backend-port (default: 5557) you configured in the step before
1. Run `sudo docker-compose build && sudo docker-compose up -d`. This takes a few minutes and builds everything as well as starts it in the background
  1. In case you need to debug, use `sudo docker logs --follow metaanchor_backend` and `sudo docker logs --follow metaanchor_frontend` respectively


## Making NFTs
1. For demo only, there is a temporary database in `backend/conf/tmpdb.json` ... Fill it
1. Copy images into the `backend/assets` folder (image paths are relative from there, so if an image `blub.jpg` is directly in the frontend/assets folder, the image shall be listed as `blub.jpg` in `backend/conf/tmpdb.json`)
1. Thats it ;) 