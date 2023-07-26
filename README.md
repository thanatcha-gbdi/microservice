# Microservice FastAPI Demo

## run
- docker compose up --build

## services

                            ┌───────────┐
                            │           │
                            │  Browser  │
                            │           │
                            └─────┬─────┘
                                  │
                                  │ (1) /movies or /books
                                  │
                                  ▼
                            ┌───────────┐
                            │           │
                            │   NGINX   │
                            │           │
                            └─────┬─────┘
                ┌───────────────┴───────────────┐
                │ (2) /movies                   │ (3) /books
                │                               │
        ┌───────▼───────┐               ┌───────▼───────┐
        │               │               │               │
        │  Movie Service│               │  Book Service │
        │               │               │               │
        └───────┬───────┘               └───────┬───────┘
                │ (4) /auth_service             │ (5) /auth_service
                │                               │
                └──────────────────────┬────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                              │                 │
                              │  Auth Service   │
                              │                 │
                              └─────────────────┘
