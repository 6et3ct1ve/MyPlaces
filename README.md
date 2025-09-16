# My Favorite Places

A Django web application for managing and discovering personal favorite places.

## Description

This application allows users to:
- View and manage a list of favorite places
- Add new places with ratings and descriptions
- Get random place suggestions based on rating weights
- View detailed information about each place

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd MyPlaces
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

6. Open browser and navigate to
```
http://127.0.0.1:8000/
```

## Project Structure

```
MyPlaces/
├── MyPlaces/          # Project configuration
├── places/            # Main application
│   ├── templates/     # HTML templates
│   ├── static/        # CSS and images
│   ├── forms.py       # Form definitions
│   ├── views.py       # Request handlers
│   ├── data.py        # Default places
│   └── random_place.py # Randomizer logic
└── manage.py
```
