FROM node:20-alpine

RUN adduser -D appuser

WORKDIR /app

COPY package.json ./

RUN npm install --omit=dev

COPY . .

USER appuser

HEALTHCHECK CMD wget --spider -q http://localhost:3000 | exit 1

CMD ["npm", "start"]


