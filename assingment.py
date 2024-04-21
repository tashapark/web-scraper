import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]



for movie_id in movie_ids:
    url = f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
      title = data.get('title')
      overview = data.get('overview')
      vote_average =  str(data.get('vote_average'))
      print("Title: " + title, "\nOverview: " + overview , "\nVote average: " + vote_average +"\n")
    else:
      print(f"Failed to fetch movie with ID {movie_id}")
 
    # response = requests.get(movie_ids)
    