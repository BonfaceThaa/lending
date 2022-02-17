###########
# BUILDER #
###########

# pull official base image
FROM node:14.19-alpine3.15 as builder

# set work directory
WORKDIR /usr/src/app

# install dependencies and avoid `node-gyp rebuild` errors
COPY ./auth/package.json .

# copy our react project
COPY ./auth .

# perform npm build
ARG API_SERVER
ENV REACT_APP_API_SERVER=${API_SERVER}
RUN REACT_APP_API_SERVER=${API_SERVER} \
  npm run build


# pull official base image
FROM node:14.19-alpine3.15

# set work directory
WORKDIR /usr/src/app

# install serve - deployment static server suggested by official create-react-app
RUN npm install -g serve

# copy our build files from our builder stage
COPY --from=builder /usr/src/app/build ./build