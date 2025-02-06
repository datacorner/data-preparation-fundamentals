import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, initialize_agent

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import get_gemini_response, clean_gemini_response, DATASET_FOLDER

# Step 1: Load Titanic Dataset
df = pd.read_csv(DATASET_FOLDER + "titanic/train.csv")

# Step 2: Define Tools for Feature Engineering

# Tool 1: Add a "FamilySize" feature
def add_family_size(data: pd.DataFrame) -> pd.DataFrame:
	data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
	return data

family_size_tool = Tool(
	name="AddFamilySize",
	func=lambda query: add_family_size(df),
	description="Adds a FamilySize column to the dataset by summing siblings/spouses and parents/children aboard."
)

# Tool 2: Add an "IsAlone" feature
def add_is_alone(data: pd.DataFrame) -> pd.DataFrame:
	if 'FamilySize' not in data.columns:
		data = add_family_size(data)
	data['IsAlone'] = (data['FamilySize'] == 1).astype(int)
	return data

is_alone_tool = Tool(
	name="AddIsAlone",
	func=lambda query: add_is_alone(df),
	description="Adds an IsAlone column indicating if a passenger was traveling alone."
)

# Tool 3: Add "FarePerPerson" feature
def add_fare_per_person(data: pd.DataFrame) -> pd.DataFrame:
	if 'FamilySize' not in data.columns:
		data = add_family_size(data)
	data['FarePerPerson'] = data['Fare'] / data['FamilySize']
	return data

fare_per_person_tool = Tool(
	name="AddFarePerPerson",
	func=lambda query: add_fare_per_person(df),
	description="Adds a FarePerPerson column by dividing the fare by FamilySize."
)

# Step 3: Initialize Google Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", 
                            temperature=0.7,
                            api_key=os.getenv('GEMINI_KEY', ""))

# Step 4: Initialize LangChain Agent with Tools
tools = [family_size_tool, is_alone_tool, fare_per_person_tool]

agent_chain = initialize_agent(
	tools=tools,
	llm=llm,
	agent="zero-shot-react-description",
	verbose=True
)

# Step 5: Execute Feature Engineering Tasks Using the Agent
print("Original DataFrame:")
print(df.head())

# Add FamilySize feature
response_family_size = agent_chain.run("Add a FamilySize column to the Titanic dataset.")
print("\nDataFrame with FamilySize:")
print(df.head())

# Add IsAlone feature
response_is_alone = agent_chain.run("Add an IsAlone column to the Titanic dataset.")
print("\nDataFrame with IsAlone:")
print(df.head())

# Add FarePerPerson feature
response_fare_per_person = agent_chain.run("Add a FarePerPerson column to the Titanic dataset.")
print("\nDataFrame with FarePerPerson:")
print(df.head())