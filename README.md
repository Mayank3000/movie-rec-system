# Movie Recommendation System

## Overview
This is a movie recommendation system built using Flask, a Python web framework. The system recommends movies based on user input and also provides a feature to browse movies by genre.

## Features
- **Movie Search:** Users can search for a movie and get recommendations based on their search query.
- **Genre-based Browsing:** Users can browse movies by genre.
- **About Page:** A simple about page with information about the project.

## How to Run
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/movie-recommendation-system.git
    ```
2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the application:**
    ```bash
    python app.py
    ```
4. **Open a web browser and navigate to:** 
    ```
    http://localhost:8000
    ```

## Files and Folders
- **app.py:** The main application file that contains the Flask app and routes.
- **templates/:** A folder that contains HTML templates for the application.
    - **about.html:** The about page template.
    - **genres.html:** The genre-based browsing template.
    - **recommend.html:** The movie recommendation template.
    - **select_genre.html:** The genre selection template.
- **movies_list.pkl, same.pkl, genre_dict.pkl:** Pickle files that contain movie data.

## API Keys
The application uses the TMDB API to fetch movie posters. You need to replace the API key in the `get_poster` function with your own API key.

## Note
This is a basic implementation of a movie recommendation system, and there are many ways to improve it. You can add more features, improve the recommendation algorithm, and enhance the user interface.

## Code Explanation
The code is divided into several sections:

### Importing Libraries
The code starts by importing the required libraries, including Flask, pickle, requests, and pandas.

### Loading Data
The movie data is loaded from three pickle files: `movies_list.pkl`, `same.pkl`, and `genre_dict.pkl`.

### Defining Functions
Two functions are defined:
- **get_poster:** This function takes a movie ID as input and returns the URL of the movie poster.
- **recommend:** This function takes a movie title as input and returns a list of recommended movie names and their corresponding posters.

### Defining Routes
Four routes are defined:
- **/about:** This route renders the about page template.
- **/:** This route handles the movie search functionality. It renders the recommendation template with a list of recommended movies based on the user's search query.
- **/genres:** This route handles the genre-based browsing functionality. It renders the genres template with a list of genres and allows the user to select a genre.

### Running the Application
The application is run using:
```python
app.run(debug=True, port=8000)
