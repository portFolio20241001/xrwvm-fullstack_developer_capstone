FROM node:18.12.1-bullseye-slim

RUN npm install -g npm@9.1.3

COPY package.json .
COPY app.js .
COPY review.js .
COPY dealership.js .
COPY data/ ./data/

COPY . .

RUN npm install

EXPOSE 3030

CMD ["node", "app.js"]
