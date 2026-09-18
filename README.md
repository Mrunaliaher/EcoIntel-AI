# 🌿 EcoIntel AI

## AI Biodiversity Intelligence Chatbot

EcoIntel AI is an AI-powered environmental intelligence chatbot developed for the **Darukaa.Earth AI Biodiversity Intelligence Chatbot Challenge**.

The system analyzes environmental conditions such as **soil health, climate, land use, biodiversity and human impact**, identifies relationships between multiple environmental metrics, retrieves relevant scientific evidence from a structured knowledge base, and generates actionable biodiversity recommendations.

---

## 🎯 Project Objective

The main objective of EcoIntel AI is to provide **evidence-informed environmental recommendations** by connecting multiple environmental factors rather than analyzing each factor independently.

The system considers relationships such as:

- Soil organic carbon ↔ Water regulation
- Soil condition ↔ Water stress
- Land use ↔ Habitat diversity
- Crop diversity ↔ Pollinator support
- Habitat conditions ↔ Species richness
- Climate ↔ Land and biodiversity conditions

The goal is to help users understand environmental risks and identify practical interventions that can support biodiversity and ecosystem health.

---

# ✨ Key Features

## 1. Environmental Assessment

EcoIntel AI analyzes environmental indicators including:

- Soil pH
- Soil organic carbon
- Soil moisture
- Rainfall
- Temperature
- Land use
- Crop diversity
- Species richness
- Pollinator abundance
- Pollution

The system identifies potential environmental concerns from the provided information.

---

## 2. Multi-Metric Environmental Reasoning

The system does not only analyze individual environmental variables.

It identifies relationships between multiple indicators.

For example:

**Low soil organic carbon + low rainfall**

may indicate increased water-related ecological stress because soil condition and water availability can interact.

Another example:

**Monoculture + low species richness**

may indicate simplified habitat conditions and reduced ecological diversity.

Another example:

**Low crop diversity + low pollinator abundance**

may indicate limited food and habitat resources for pollinators.

---

## 3. Scientific Evidence Retrieval

EcoIntel AI uses a lightweight **Retrieval-Augmented Generation (RAG)** approach.

Scientific knowledge is stored in a structured JSON knowledge base:

```text
backend/knowledge/knowledge.json

The system uses:

TF-IDF vectorization
Cosine similarity
Relevance-based document retrieval

The retrieved evidence is displayed with:

Scientific source
Report/research title
Topic
Relevance score
Supporting scientific explanation

This makes the evidence retrieval process transparent.

4. Actionable Recommendations

The system generates environmental recommendations based on identified risks and relationships.

Each recommendation contains:

Recommended action
Scientific reasoning
Affected environmental metrics
Expected time horizon
Supporting scientific evidence

Example:

Introduce appropriate soil-cover practices and diversified vegetation.

The system then explains why the recommendation may address the identified environmental conditions.

5. Conversational Environmental Interface

Users can describe environmental situations using natural language.

Example:

My farm has low soil carbon, low rainfall, monoculture wheat and very few pollinators. What should I do?

The system extracts relevant environmental information from the message and performs environmental reasoning.

6. Structured Environmental Input

The system also supports structured JSON environmental information through the /analyze API endpoint.

Example:

{
  "soil": {
    "ph": 6.2,
    "organic_carbon": 0.3,
    "moisture": 18
  },
  "climate": {
    "rainfall": 450,
    "temperature": 29
  },
  "land": {
    "crop": "wheat",
    "land_use": "monoculture"
  },
  "biodiversity": {
    "species_richness": "low",
    "pollinator_abundance": "low"
  },
  "human_impact": {
    "pollution": "moderate"
  }
}
🏗️ System Architecture
                         USER
                           │
                           ▼
                Natural Language Query
                           │
                           ▼
                    FastAPI Backend
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
        Environmental           Structured JSON
          Extraction                 Input
                │                     │
                └──────────┬──────────┘
                           ▼
                 Environmental Reasoning
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
          Risk Identification   Multi-Metric
                                Relationships
                 │                   │
                 └─────────┬─────────┘
                           ▼
                     RAG Retrieval
                           │
                           ▼
                TF-IDF + Cosine Similarity
                           │
                           ▼
                Scientific Knowledge Base
                    knowledge.json
                           │
                           ▼
                Scientific Evidence
                           │
                           ▼
                  Recommendations
                           │
                           ▼
                    Chatbot Response
🧠 RAG / Knowledge System

EcoIntel AI implements a lightweight RAG pipeline.

The scientific knowledge base is stored in:

backend/knowledge/knowledge.json

Each document follows a structured format:

{
  "id": "soil_carbon",
  "topic": "soil organic carbon",
  "source": "FAO",
  "title": "Recarbonizing Global Soils",
  "content": "Scientific evidence..."
}
Retrieval Process

The retrieval pipeline works as follows:

Scientific knowledge is loaded from knowledge.json.
Document content is converted into TF-IDF vectors.
The user's environmental query is converted into a TF-IDF vector.
Cosine similarity is calculated between the query and stored documents.
The most relevant documents are selected.
Retrieved scientific evidence is returned with the environmental recommendations.

This allows the chatbot to provide evidence that is directly connected to the user's environmental query.

📚 Scientific Knowledge Sources

The current curated knowledge base contains information from recognized environmental organizations and scientific assessment sources, including:

FAO — Food and Agriculture Organization
IPBES — Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services
IPCC — Intergovernmental Panel on Climate Change

Current knowledge topics include:

Soil organic carbon
Soil cover
Agroforestry
Crop diversification
Biodiversity
Climate and land
Habitat diversity
Water and ecosystems
📊 Environmental Data Schema

The system organizes environmental information into the following major categories:

Environment
│
├── soil
│   ├── ph
│   ├── organic_carbon
│   └── moisture
│
├── climate
│   ├── rainfall
│   └── temperature
│
├── land
│   ├── crop
│   └── land_use
│
├── biodiversity
│   ├── species_richness
│   └── pollinator_abundance
│
└── human_impact
    └── pollution
🔌 API Endpoints
GET /

Returns the basic project status.

Example response:

{
  "project": "EcoIntel AI",
  "description": "AI Biodiversity Intelligence System",
  "status": "running"
}
POST /analyze

Analyzes structured environmental data.

The endpoint returns:

Environmental findings
Environmental relationships
Risk factors
Retrieved scientific evidence
Recommendations
Affected environmental metrics
Time horizon
POST /chat

Accepts a natural-language environmental question.

Example:

My farm has low soil carbon, low rainfall, monoculture wheat and very few pollinators. What should I do?

The chatbot performs the following steps:

User Question
      ↓
Environmental Information Extraction
      ↓
Environmental Risk Analysis
      ↓
Multi-Metric Reasoning
      ↓
Scientific Evidence Retrieval
      ↓
Recommendation Generation
      ↓
Evidence-Backed Response
🛠️ Technology Stack
Backend
Python
FastAPI
Uvicorn
Pydantic
RAG / Knowledge Retrieval
Scikit-learn
TF-IDF Vectorization
Cosine Similarity
JSON Knowledge Base
Frontend
HTML5
CSS3
JavaScript
Development Tools
Visual Studio Code
Git
GitHub
FastAPI Swagger UI
📁 Project Structure
EcoIntel-AI/
│
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── reasoning.py
│   │
│   └── knowledge/
│       └── knowledge.json
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
├── README.md
│
└── venv/
Important

The venv/ directory is excluded from Git using .gitignore.

Python cache files and environment variable files are also excluded.

💻 Local Setup
1. Clone the Repository

After the GitHub repository is created:

git clone <YOUR_GITHUB_REPOSITORY_URL>

Navigate into the project:

cd EcoIntel-AI
2. Create a Virtual Environment

On Windows PowerShell:

python -m venv venv

Activate the virtual environment:

.\venv\Scripts\Activate.ps1
3. Install Dependencies

Install the required Python packages:

python -m pip install fastapi uvicorn scikit-learn
▶️ Running the Backend

Open PowerShell and navigate to the backend:

cd backend

If the virtual environment is not activated:

..\venv\Scripts\Activate.ps1

Start the FastAPI server:

python -m uvicorn main:app --reload

The backend will run at:

http://127.0.0.1:8000
📖 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

http://127.0.0.1:8000/docs

The Swagger interface can be used to test:

GET /
POST /analyze
POST /chat
🌐 Running the Frontend

The frontend is a lightweight HTML/CSS/JavaScript interface.

Open:

frontend/index.html

in a web browser.

The frontend communicates with the FastAPI backend through:

http://127.0.0.1:8000/chat

The chatbot interface displays:

Environmental assessment
Risk factors
Multi-metric relationships
Recommendations
Affected environmental metrics
Scientific evidence
🧪 Testing and Validation

The backend was tested using the FastAPI Swagger interface.

A test environment included:

Soil organic carbon: 0.3
Soil moisture: 18
Soil pH: 6.2
Rainfall: 450
Temperature: 29
Land use: monoculture
Species richness: low
Pollinator abundance: low
Pollution: moderate

The system successfully identified environmental concerns including:

Low soil organic carbon
Low soil moisture
Potential water stress
Monoculture / low crop diversity
Low species richness
Low pollinator abundance

The system also identified multi-metric relationships and returned relevant scientific evidence and recommendations.

💬 Example Chatbot Query
User Input
My farm has low soil carbon, low rainfall, monoculture wheat and very few pollinators. What should I do?
Environmental Assessment

The system identifies:

Low soil organic carbon
Low rainfall / potential water stress
Monoculture / low crop diversity
Low pollinator abundance
Multi-Metric Reasoning

The system identifies relationships such as:

Low soil organic carbon
        +
Low rainfall
        ↓
Potential water-related ecological stress

and:

Low crop diversity
        +
Low pollinator abundance
        ↓
Limited food and habitat resources
Example Recommendations
1. Introduce appropriate soil-cover practices
   and diversified vegetation.

2. Create flowering habitat strips using locally
   appropriate plant species.

The system also retrieves supporting scientific evidence from the knowledge base.

🔐 API Keys and Credentials

The current MVP does not require an external AI API key.

The project currently does not depend on:

OpenAI API
Gemini API
Claude API
Paid AI APIs

No secret credentials should be committed to GitHub.

The .gitignore file excludes environment variable files such as:

.env
.env.*
🚀 CI/CD

CI/CD is not configured yet for the current MVP.

The project has been developed, tested and validated locally.

Future versions can use GitHub Actions to automate:

Dependency installation
Backend testing
API validation
Code checks
Deployment
⚠️ Current Limitations

The current MVP is intentionally lightweight.

1. Natural Language Extraction

Environmental information extraction from natural-language queries currently uses rule-based keyword matching.

For example, phrases such as:

low soil carbon
low rainfall
monoculture
few pollinators

are recognized by the environmental extraction module.

2. Knowledge Base Size

The current knowledge base contains a curated collection of scientific evidence.

A larger production system would require more research papers, reports and environmental datasets.

3. Retrieval Method

The current RAG implementation uses:

TF-IDF + Cosine Similarity

rather than neural embeddings or a dedicated vector database.

This lightweight approach was selected to keep the MVP simple, fast and easy to run locally.

4. Local Environmental Conditions

Environmental recommendations depend on local conditions.

Actual outcomes may vary depending on:

Soil type
Local climate
Species
Geography
Land-management practices
Water availability
Existing habitat conditions

Therefore, recommendations should be considered evidence-informed decision support rather than guaranteed outcomes.

🔮 Future Improvements

Future versions of EcoIntel AI could include:

Neural embedding-based retrieval
Vector database integration
Larger scientific document collection
Research-paper and PDF ingestion
Improved environmental entity extraction
Geographic coordinate support
Real-time weather data
Climate datasets
Satellite and land-cover data
Biodiversity datasets
Improved conversational memory
Automated evaluation
GitHub Actions CI/CD
Cloud deployment
Optional LLM integration
More advanced biodiversity impact prediction
🌍 Challenge Alignment

EcoIntel AI addresses the major requirements of the Darukaa.Earth challenge.

Challenge Requirement	EcoIntel AI Implementation
Structured environmental knowledge	knowledge.json
Soil health	pH, organic carbon, moisture
Land use / land cover	Land-use analysis
Biodiversity indicators	Species richness, pollinator abundance
Climate	Rainfall and temperature
Human impact	Pollution
RAG / retrieval	TF-IDF + cosine similarity
Scientific evidence	FAO, IPBES and IPCC knowledge
Multi-metric reasoning	Environmental relationship analysis
Actionable recommendations	Recommendation generation
Natural-language interaction	/chat endpoint
Structured input	/analyze endpoint
Evidence transparency	Retrieved source and relevance score
📌 Project Links
GitHub Repository
[ADD FINAL GITHUB REPOSITORY LINK HERE]
Live Demo
[ADD LIVE DEMO URL HERE IF DEPLOYED]
Submission Document

The final submission document contains the project overview, repository information, setup instructions and challenge submission details.

👩‍💻 Project Information

Project Name: EcoIntel AI

Project Type: AI Biodiversity Intelligence Chatbot

Challenge: Darukaa.Earth AI Biodiversity Intelligence Chatbot Challenge

Primary Goal: Evidence-informed environmental intelligence and biodiversity recommendations

📋 Final Submission Checklist
 GitHub repository created
 Source code uploaded
 .gitignore configured
 README.md added
 Backend tested successfully
 Frontend tested successfully
 /analyze endpoint tested
 /chat endpoint tested
 RAG retrieval demonstrated
 Scientific evidence included
 Multi-metric reasoning demonstrated
 Recommendations generated
 GitHub repository link added to submission document
 Live demo link added if deployed
 Final Word submission document completed
 Repository checked for API keys and sensitive files
 Final project submitted through the challenge platform