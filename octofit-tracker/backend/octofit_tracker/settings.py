# Add 'djongo' to the INSTALLED_APPS list to enable MongoDB support
INSTALLED_APPS += [
    'djongo',
    'rest_framework',
    'corsheaders',
    'octofit_tracker',
    'populate_db'
]

# Add middleware for CORS headers
MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

# Configure the database to use MongoDB
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

# Allow all origins for CORS (adjust as needed for production)
CORS_ALLOW_ALL_ORIGINS = True