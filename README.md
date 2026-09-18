# 🌱 EcoIntel AI

### AI-Powered Biodiversity & Environmental Intelligence Chatbot

EcoIntel AI is an AI-powered environmental intelligence chatbot developed for the **Darukaa.Earth AI Biodiversity Intelligence Chatbot Challenge**.

The system analyzes environmental indicators such as **soil health, climate, land use, biodiversity, and human impact** to identify ecological risks, understand relationships between multiple environmental factors, retrieve scientific evidence, and provide actionable recommendations.

---

## 🎯 Project Objective

The objective of EcoIntel AI is to transform environmental observations into meaningful ecological insights.

Instead of analyzing environmental parameters independently, the system considers relationships between multiple indicators.

For example:

- Low soil organic carbon + low rainfall → potential water-related ecological stress
- Monoculture + low species richness → simplified habitat and reduced ecological diversity
- Low crop diversity + low pollinator abundance → limited food and habitat resources
- High pollution + low biodiversity → potential environmental stress on ecosystems

The system combines:

1. Environmental data extraction
2. Multi-metric reasoning
3. Risk identification
4. Scientific knowledge retrieval
5. Evidence-based explanations
6. Actionable recommendations

---

## 🧠 Key Features

### 1. Multi-Metric Environmental Reasoning

EcoIntel AI evaluates multiple environmental indicators together instead of treating them as isolated values.

The system can analyze:

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

This allows the chatbot to identify relationships and possible ecological risks.

### 2. Environmental Risk Identification

The reasoning engine checks environmental conditions and identifies potential risks, including:

- Soil degradation
- Water stress
- Biodiversity loss
- Habitat simplification
- Reduced pollinator support
- Pollution-related ecological stress
- Climate-related environmental stress

The identified risks are based on predefined environmental rules and relationships.

### 3. Actionable Recommendations

After identifying potential risks, the system provides practical recommendations, such as:

- Improving soil organic matter
- Increasing crop diversity
- Supporting pollinator habitats
- Reducing excessive chemical inputs
- Improving water management
- Maintaining habitat diversity
- Monitoring environmental indicators regularly

Recommendations are generated based on the detected environmental conditions.

### 4. Scientific Knowledge Retrieval

EcoIntel AI uses a lightweight **Retrieval-Augmented Generation (RAG)** approach to connect environmental reasoning with scientific knowledge.

Scientific knowledge is stored in a structured JSON knowledge base:

```
backend/knowledge/knowledge.json
```

The system uses:

- TF-IDF vectorization
- Cosine similarity
- Relevance-based document retrieval

When a user asks an environmental question, relevant knowledge entries are retrieved from the knowledge base, including:

- Source
- Title
- Topic
- Relevant environmental information
- Relevance score

### 5. Conversational Environmental Interface

Users can interact with EcoIntel AI through a web-based chatbot interface. The interface allows users to:

- Ask environmental questions
- Provide environmental observations
- Submit structured environmental data
- Receive environmental risk analysis
- View scientific evidence
- Get actionable recommendations

### 6. Structured Environmental Input

Environmental observations can be represented using structured JSON data.

**Example:**

```json
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
```

This structured representation allows the reasoning engine to process multiple environmental dimensions together.

---

## 🏗️ System Architecture

The overall EcoIntel AI workflow is:

```
USER
 │
 ▼
Natural Language Query
 │
 ▼
FastAPI Backend
 │
 ▼
Environmental Data Extraction
 │
 ▼
Structured Environmental Input
 │
 ▼
Environmental Reasoning
 │
 ▼
Risk Identification
 │
 ▼
Multi-Metric Relationship Analysis
 │
 ▼
RAG Knowledge Retrieval
 │
 ▼
TF-IDF + Cosine Similarity
 │
 ▼
Scientific Knowledge Base
 │
 ▼
Scientific Evidence
 │
 ▼
Recommendations
 │
 ▼
Chatbot Response
```

---

## 🔬 Environmental Reasoning

The reasoning engine is implemented in:

```
backend/reasoning.py
```

The system evaluates relationships between environmental indicators.

**Example 1**

```
Low Soil Organic Carbon
        +
   Low Rainfall
        ↓
Potential Water / Soil Stress
        ↓
   Recommendation:
Improve soil organic matter and
water management practices
```

**Example 2**

```
Monoculture
        +
Low Species Richness
        ↓
Habitat Simplification
        ↓
   Recommendation:
Increase crop and habitat diversity
```

**Example 3**

```
Low Crop Diversity
        +
Low Pollinator Abundance
        ↓
Reduced Food / Habitat Resources
        ↓
   Recommendation:
Increase flowering vegetation
and habitat diversity
```

The reasoning system is currently rule-based and designed to provide interpretable environmental insights.

---

## 📚 Scientific Knowledge Sources

The knowledge base is designed around information from recognized environmental and scientific organizations:

- **FAO** — Food and Agriculture Organization of the United Nations
- **IPBES** — Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services
- **IPCC** — Intergovernmental Panel on Climate Change

These sources provide scientific context for environmental and biodiversity-related information used by the system.

---

## 🧠 RAG / Knowledge System

EcoIntel AI implements a lightweight Retrieval-Augmented Generation style pipeline.

The knowledge base is located at:

```
backend/knowledge/knowledge.json
```

The retrieval process works as follows:

```
User Query
    ↓
Text Processing
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Relevant Knowledge Entries
    ↓
Environmental Reasoning
    ↓
Evidence-Based Response
```

**Retrieval Method**

The current implementation uses:

- **TF-IDF** — converts text into numerical vectors based on the importance of words within the knowledge base.
- **Cosine Similarity** — measures how closely the user's query matches available scientific knowledge entries.

The most relevant entries are selected for the response.

---

## 📊 Environmental Data Schema

EcoIntel AI organizes environmental information into several major categories.

| Category | Example Indicators |
|---|---|
| Soil | pH, organic carbon, moisture |
| Climate | rainfall, temperature |
| Land | crop, land use |
| Biodiversity | species richness, pollinator abundance |
| Human Impact | pollution |

This structure allows the system to combine multiple environmental dimensions during reasoning.

---

## 🔌 API Endpoints

The backend is implemented using FastAPI.

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Provides basic information about the EcoIntel AI backend |
| `/analyze` | POST | Used for environmental analysis requests depending on the configured backend implementation |
| `/chat` | POST | Used for conversational environmental queries |

**API Documentation**

FastAPI automatically provides interactive API documentation. When the backend is running locally, open:

```
http://127.0.0.1:8000/docs
```

This provides an interactive Swagger interface for testing the API endpoints.

---

## 🛠️ Technology Stack

**Backend**
- Python
- FastAPI
- Uvicorn
- Scikit-learn
- TF-IDF
- Cosine Similarity

**Frontend**
- HTML5
- CSS3
- JavaScript

**Knowledge System**
- JSON knowledge base
- TF-IDF retrieval
- Cosine similarity

**Development Tools**
- Visual Studio Code
- Git
- GitHub
- Python Virtual Environment

---

## 📁 Project Structure

```
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
└── README.md
```

> **Note:** The local Python virtual environment (`venv/`) is not included in the GitHub repository because it is excluded using `.gitignore`.

---

## ⚙️ Local Installation

### 1. Clone the Repository

Open PowerShell and run:

```bash
git clone https://github.com/Mrunaliaher/EcoIntel-AI.git
```

Move into the project directory:

```bash
cd EcoIntel-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If activation is successful, the terminal should show:

```
(venv)
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn scikit-learn
```

---

## ▶️ Running the Backend

Move into the backend directory:

```bash
cd backend
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend should start at:

```
http://127.0.0.1:8000
```

---

## 🌐 Running the Frontend

The frontend is contained in:

```
frontend/
```

Open `frontend/index.html` in a web browser.

The frontend communicates with the deployed FastAPI backend on Render.

---

## 🧪 Testing

EcoIntel AI can be tested using the FastAPI Swagger interface.

Start the backend:

```bash
uvicorn main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

Test the available endpoints using the interactive Swagger interface.

---

## 🔍 Example Environmental Query

**Example user query:**

> The soil organic carbon is low, rainfall is low, and the field is under monoculture. Species richness and pollinator abundance are also low. What could be the environmental risks?

The system can identify relationships such as:

```
Low Soil Organic Carbon
        +
    Low Rainfall
        ↓
Potential Soil / Water Stress
```

```
Monoculture
        +
Low Species Richness
        ↓
Habitat Simplification
```

```
Low Crop Diversity
        +
Low Pollinator Abundance
        ↓
Reduced Ecological Support
```

The chatbot then provides scientific context and recommendations based on the retrieved knowledge.

---

## 🌍 Challenge Alignment

EcoIntel AI addresses the major objectives of the Darukaa.Earth AI Biodiversity Intelligence Chatbot Challenge.

| Challenge Requirement | EcoIntel AI Implementation |
|---|---|
| Biodiversity intelligence | Species richness and pollinator analysis |
| Environmental understanding | Soil, climate, land and pollution indicators |
| Multi-metric reasoning | Relationships between multiple indicators |
| AI-powered chatbot | Conversational web interface |
| Knowledge retrieval | TF-IDF + cosine similarity RAG |
| Scientific grounding | FAO, IPBES and IPCC knowledge |
| Risk identification | Rule-based environmental reasoning |
| Actionable insights | Environmental recommendations |
| Structured environmental data | JSON-based environmental schema |
| Explainability | Retrieved evidence and interpretable rules |

---

## 💡 Why This Approach?

Environmental problems are usually interconnected. For example, biodiversity loss may be influenced by:

- Land-use change
- Reduced crop diversity
- Soil degradation
- Water stress
- Pollution
- Climate conditions

Therefore, EcoIntel AI focuses on relationships between environmental indicators rather than looking at individual measurements independently.

The combination of:

```
Environmental Data
        +
    Reasoning
        +
Scientific Knowledge Retrieval
        +
     Evidence
        +
 Recommendations
```

allows the system to provide more meaningful environmental intelligence.

---

## 🔐 Privacy and API Keys

The current project does not require external API keys. No secret credentials should be committed to the repository. Environment variables and sensitive files are excluded through `.gitignore`.

---

## ⚠️ Current Limitations

1. **Rule-Based Reasoning** — Environmental reasoning currently relies on predefined rules rather than a fully trained environmental intelligence model.
2. **Small Knowledge Base** — The scientific knowledge base is currently limited to a curated set of environmental information.
3. **TF-IDF Retrieval** — The RAG system currently uses TF-IDF and cosine similarity instead of modern embedding-based retrieval.
4. **Limited Data Sources** — The current prototype does not yet directly integrate live weather APIs, satellite imagery, GIS data, biodiversity databases, or IoT sensor streams.
5. **Natural Language Extraction** — Environmental values provided in natural language are currently extracted using lightweight logic rather than a large language model.
6. **Geographic Context** — The current prototype does not yet perform detailed location-specific environmental analysis.

---

## 🚀 Future Improvements

**Advanced RAG**
- Sentence embeddings
- Vector databases
- Semantic search
- Larger scientific document collections
- PDF-based knowledge ingestion

**Environmental Data Integration**
- Weather APIs
- Climate datasets
- Satellite imagery
- GIS information
- Soil databases
- Biodiversity datasets
- IoT environmental sensors

**Advanced AI**
- Large Language Models
- Machine learning-based environmental risk prediction
- Explainable AI
- Time-series environmental forecasting

**Geographic Intelligence**

Future versions could support:

```
Location
   ↓
Environmental Data
   ↓
Climate + Soil + Land Use
   ↓
Biodiversity Information
   ↓
Risk Analysis
   ↓
Location-Specific Recommendations
```

**Deployment**

The system can later be deployed using:

- Cloud hosting
- Docker
- CI/CD pipelines
- Production database
- Scalable vector database
- Cloud-based AI services

---

## 🧪 Validation Strategy

The system can be validated using different environmental scenarios.

**Scenario 1 — Soil Stress**

- Low soil organic carbon
- Low rainfall
- Low soil moisture

Expected analysis: *Potential soil and water stress*

**Scenario 2 — Biodiversity Stress**

- Monoculture
- Low species richness
- Low crop diversity

Expected analysis: *Potential habitat simplification and reduced ecological diversity*

**Scenario 3 — Pollinator Stress**

- Low crop diversity
- Low pollinator abundance

Expected analysis: *Potential reduction in food and habitat resources for pollinators*

**Scenario 4 — Pollution Stress**

- Moderate / high pollution
- Low biodiversity

Expected analysis: *Potential environmental stress requiring further monitoring*

---

## 📈 Development Roadmap

```
Phase 1
│
├── Project setup
├── Backend development
├── Frontend development
└── Environmental knowledge base
        ↓
Phase 2
│
├── Environmental reasoning
├── Risk identification
├── RAG retrieval
└── Scientific evidence
        ↓
Phase 3
│
├── Testing
├── Validation
├── UI improvements
└── Documentation
        ↓
Phase 4
│
├── Embedding-based RAG
├── Larger knowledge base
├── External environmental datasets
└── Cloud deployment
```

---

## 🔗 Project Links

- **GitHub Repository:** https://github.com/Mrunaliaher/EcoIntel-AI
- **Live Demo:** https://ecointel-ai.vercel.app/
- **Backend API:** https://ecointel-ai.onrender.com/

---


## 🌱 Conclusion

EcoIntel AI demonstrates how artificial intelligence, environmental reasoning, and scientific knowledge retrieval can be combined to support biodiversity and environmental intelligence.

The system connects:

```
Environmental Observations
          ↓
Multi-Metric Reasoning
          ↓
Risk Identification
          ↓
Scientific Knowledge Retrieval
          ↓
Evidence-Based Insights
          ↓
Actionable Recommendations
```

The current prototype provides a lightweight and interpretable foundation that can be extended with larger scientific datasets, semantic RAG, real-time environmental information, geospatial intelligence, and advanced AI models.
