FROM node:16-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy application
COPY . .

# Expose port
EXPOSE 3000

# Run application
CMD ["npm", "start"]
