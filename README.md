# Project Documentation

## Table of Contents
- [🖥️ Frontend](#frontend)
- [🗃️ Backend](#backend)

## Frontend
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Build the frontend:
   ```sh
   make build-frontend
   ```
3. Start the frontend:
   ```sh
   make start-frontend
   ```

## Backend 

### Things you need before starting
1. Docker 🐳
2. Python Version 3.11 🐍

### How to add a package
```sh
   cd backend
   poetry add python <package_name>
   ```


### How to Start
1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Add `.env.local` and take the env keys from notion
3. Build the backend:
   ```sh
   make build-backend
   ```
4. Start the backend:
   ```sh
   make start-backend
   ```
