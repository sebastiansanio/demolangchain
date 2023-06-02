

import requests
import os

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from Linkedin profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": 'Bearer ' + os.environ.get('NUBELA_API_KEY','')}

    response = requests.get(api_endpoint, headers=header_dic, params={"url": linkedin_profile_url})

    data = response.json()

    data = {
        k: v
        for k,v in data.items()
            if v not in ([], "", "", None) and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for groups_dict in data.get("groups"):
            groups_dict.pop("profile_pic_url")

    if data.get("experiences"):
        for experience_dict in data.get("experiences"):
            experience_dict.pop("company_linkedin_profile_url")

    if data.get("education"):
        for education_dict in data.get("education"):
            education_dict.pop("school_linkedin_profile_url")
            education_dict.pop("logo_url")

    if data.get("experiences"):
        for experience_dict in data.get("experiences"):
            experience_dict.pop("logo_url")

    if data.get("activities"):
        for activities_dict in data.get("activities"):
            activities_dict.pop("link")

    return data