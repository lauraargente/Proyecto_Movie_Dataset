
# Elimino las columnas tagline, keywords, popularity, overview porque no aportan al análisis

CREATE TABLE proyecto_movie.movies (
    id INT PRIMARY KEY,
    budget BIGINT,
    genres TEXT,
    homepage VARCHAR(255),
    original_language VARCHAR(10),
    original_title VARCHAR(255),
    production_companies TEXT,
    production_countries TEXT,
    release_date DATE,
    revenue BIGINT,
    runtime FLOAT,
    spoken_languages TEXT,
    status VARCHAR(50),
    title VARCHAR(255),
    vote_average DECIMAL(3,1),
    vote_count INT
);

CREATE TABLE proyecto_movie.credits (
    movie_id INT PRIMARY KEY,
    title VARCHAR(255),
    cast_actors TEXT,
    crew TEXT,
    FOREIGN KEY (movie_id)
    REFERENCES proyecto_movie.movies(id)
);