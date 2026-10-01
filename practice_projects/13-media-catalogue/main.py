# Custom exception for errors specific to the media catalogue
class MediaError(Exception):
    """Custom exception for media-related errors."""
    
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj


# Parent class representing a movie
class Movie:
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        # Validate the movie information before creating the object
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    
    # Controls how a Movie object is displayed as a string
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'


# Child class that inherits the common properties of Movie
class TVSeries(Movie):
    """Child class representing an entire TV series."""
    
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        # Reuse Movie's initialization and validation
        super().__init__(title, year, director, duration)
        
        # Validate TV series-specific information
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        self.seasons = seasons
        self.total_episodes = total_episodes
    
    # Provides a different string representation for TV series
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'


# Manages and stores different types of media objects
class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    
    def __init__(self):
        self.items = []
    
    # Adds a media object after checking that it is a Movie or TVSeries
    def add(self, media_item):
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)
    
    # Returns only objects that are exactly Movie instances
    def get_movies(self):
        return [item for item in self.items if type(item) is Movie]
    
    # Returns all TVSeries objects in the catalogue
    def get_tv_series(self):
        return [item for item in self.items if isinstance(item, TVSeries)]
    
    # Creates a formatted display of the entire catalogue
    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        
        movies = self.get_movies()
        series = self.get_tv_series()
        
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        
        # Display movies in their own section
        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
        
        # Display TV series in their own section
        if series:
            result += '=== TV SERIES ===\n'
            for i, serie in enumerate(series, 1):
                result += f'{i}. {serie}\n'        
        
        return result


# Create the catalogue and add sample media
catalogue = MediaCatalogue()

try:
    # Create and add movies
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    catalogue.add(movie1)
    
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    catalogue.add(movie2)
    
    # Create and add TV series
    series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
    catalogue.add(series1)
    
    series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series2)
    
    # Display the complete catalogue
    print(catalogue)

# Handle invalid movie or TV series data
except ValueError as e:
    print(f'Validation Error: {e}')

# Handle invalid objects being added to the catalogue
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')