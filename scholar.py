from scholarly import scholarly
from serpapi import GoogleSearch

def searchAuthor(authorName):
    query = scholarly.search_author(authorName)
    author = next(query)
    return author['scholar_id']

def getAuthorArticles(authorID):
    params = {
        "engine": "google_scholar_author",
        "author_id": authorID,
        "api_key": "743c96402f3f2e96e9f7e87c9c06d115041284720be7c26bcb144d106f0d035b"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    articles = results['articles']
    print(articles)


def main():
    getAuthorArticles(searchAuthor('Arnold Meijster'))
main()