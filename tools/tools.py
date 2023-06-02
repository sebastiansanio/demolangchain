

from langchain import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for Linkedin for profile page"""
    search=SerpAPIWrapper(search_engine="google")

    res=search.run(f"{text}")

    print(res)
    return res