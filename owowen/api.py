from enum import Enum
from typing import List

import objectrest
from owowen.classes import Movie, MovieList

API_BASE = "https://owen-wilson-wow-api.herokuapp.com/wows"


class SortDirection(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


def _valid_sort(sort: str) -> bool:
    if sort not in ["movie", "release_date", "year", "director", "num_current_wow"]:
        raise ValueError("Invalid sort parameter.")
    return True


class API:
    def __init__(self):
        self.api = objectrest.RequestHandler(base_url=API_BASE)

    def get_random_wow(self, count: int = 1, year: int = None, movie: str = None, director: str = None,
                       wow_count: int = None, sort: str = None,
                       sort_direction: SortDirection = SortDirection.ASCENDING) -> List[Movie]:
        """
        Get a random wow from the API.
        :param count: How many wows to get.
        :param year: Specific year to get.
        :param movie: Specific movie to get.
        :param director: Specific director to get.
        :param wow_count: Specific wow occurrence to get.
        :param sort: Sort the results by.
        :param sort_direction: Sort direction.
        :return: List of wows.
        """
        params = {"results": count}
        if year:
            params["year"] = year
        if movie:
            params["movie"] = movie
        if director:
            params["director"] = director
        if wow_count:
            params["wow_in_movie"] = wow_count
        if sort and _valid_sort(sort):
            params["sort"] = sort
        if sort_direction:
            params["direction"] = sort_direction.value
        return self.api.get_object(url="/random", params=params, model=Movie, extract_list=True)

    def get_chronological_wows(self, start: int = 0, end: int = None) -> List[Movie]:
        """
        Get chronological wows from the API.
        :param start: Which wow to start at.
        :param end: Which wow to end at.
        :return: A wow.
        """
        wow = f"{start}"
        if end:
            wow += f"-{end}"
            return self.api.get_object(url=f"/ordered/{wow}", model=Movie, extract_list=True)
        else:
            movie = self.api.get_object(url=f"/ordered/{wow}", model=Movie)
            return [movie]

    def get_all_movies(self) -> List[str]:
        """
        Get all movies from the API.
        :return: A list of movies titles.
        """
        return self.api.get_json(url="/movies")

    def get_all_directors(self) -> List[str]:
        """
        Get all directors from the API.
        :return: A list of director names.
        """
        return self.api.get_json(url="/directors")
