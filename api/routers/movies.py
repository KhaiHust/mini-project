from fastapi import APIRouter, Response
import repository.movies as movies_repository
import schemas.movies as schemas_movies

router = APIRouter(tags=['Movies'])


@router.get('/movies', response_model=schemas_movies.MovieListResponse)
async def get_all_movies():
    movies = movies_repository.getAllMovies()
    return schemas_movies.MovieListResponse(msg='get all movies success', data=movies)


@router.get('/movies/now', response_model=schemas_movies.MovieListResponse)
async def get_movie_now():
    msg, movies = movies_repository.getMovieShowNow()
    return schemas_movies.MovieListResponse(msg=msg, data=movies)


@router.get('/movies/{id}', response_model=schemas_movies.MovieListResponse)
async def get_movie_by_id(id: int):
    msg, movie = movies_repository.getMoviesById(id)
    return schemas_movies.MovieListResponse(msg=msg, data=movie)





@router.post('/movies', response_model=schemas_movies.MovieListResponse)
async def create_a_movie(request: schemas_movies.Movies):
    msg, movie = movies_repository.createMovie(request)
    return schemas_movies.MovieListResponse(msg=msg, data=movie)


@router.patch('/movies/{id}', response_model=schemas_movies.MovieListResponse)
async def update_a_movie(id, request: schemas_movies.Movies):
    movie = movies_repository.updateAMovie(id, request)
    return schemas_movies.MovieListResponse(msg=f'update movie {id} success', data=[movie])


@router.delete('/movies/{id}', response_model=schemas_movies.MovieListResponse)
async def delete_a_movie(id: int):
    movies_repository.deleteAMovieById(id=id)
    return schemas_movies.MovieListResponse(msg=f'delete movie {id} success', data=[])
