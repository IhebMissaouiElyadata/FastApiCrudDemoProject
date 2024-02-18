# Use the official Node.js image as the base image
FROM node:16-alpine as build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files into the container
COPY package*.json ./

# Install dependencies
RUN npm install
RUN npm install react-scripts

# Copy the rest of the application code into the container
COPY . .
# Change working directory to the React app directory
WORKDIR /app/react-front

# Build the React app
RUN npm run build

# Use a smaller, lighter image for the production build
FROM nginx:alpine
# Copy the built app from the previous stage into the nginx web server directory
RUN ls
COPY --from=build  /app/react-front/build /usr/share/nginx/html
# Expose port 80 to the outside world
EXPOSE 80

# Start the nginx web server
CMD ["nginx", "-g", "daemon off;"]
