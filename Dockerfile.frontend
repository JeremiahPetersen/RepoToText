# Start from a Node image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy over the react files and package.json
COPY ./src /app/src
COPY ./public /app/public
COPY ./package.json /app

# Install the node dependencies
RUN npm install

# Expose the port for the server
EXPOSE 3000

# Start the server
CMD ["npm", "start"]
