from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":

    linkedin_data_1 = scrape_linkedin_profile("PLACEHOLDER")

    linkedin_data_2 = scrape_linkedin_profile("PLACEHOLDER")

    summary_template = """
        given the information {linkedin_data_1} about a person and {linkedin_data_2} about another one
        I need to hire a virtual CISO for the startup where I work
        Please enumarate pros and cons of each one
        Finally, given pros and cons, tell me which you would hire
    """

    summary_prompt_template = PromptTemplate(input_variables=["linkedin_data_1","linkedin_data_2"], template=summary_template)

    llm = ChatOpenAI(temperature=0.6, model_name="gpt-4")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(linkedin_data_1=linkedin_data_1, linkedin_data_2=linkedin_data_2))
