FROM node

ENV INSTALL_PATH /frontend
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

RUN npm install -g yarn

COPY package.json package.json
COPY yarn.lock yarn.lock
RUN yarn

COPY . .
RUN npm run build
