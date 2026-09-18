from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional

from rag import retrieve
from reasoning import (
    analyze_environment,
    extract_environment_from_text,
    generate_recommendations
)

app = FastAPI(
    title="EcoIntel AI",
    description="AI Biodiversity Intelligence System for Darukaa.Earth",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Environment(BaseModel):
    soil: Dict[str, Any] = {}
    climate: Dict[str, Any] = {}
    land: Dict[str, Any] = {}
    biodiversity: Dict[str, Any] = {}
    human_impact: Dict[str, Any] = {}

class ChatRequest(BaseModel):
    message: str
    environment: Optional[Environment] = None

@app.get("/")
def home():
    return {
        "project": "EcoIntel AI",
        "description": "AI Biodiversity Intelligence System",
        "status": "running"
    }


@app.post("/analyze")
def analyze(data: Environment):

    # Convert input into dictionary
    environment = data.model_dump()

    # -----------------------------------
    # 1. ENVIRONMENTAL REASONING
    # -----------------------------------

    reasoning = analyze_environment(environment)

    # -----------------------------------
    # 2. BUILD RAG QUERY
    # -----------------------------------

    query = f"""
    Analyze this environmental situation:

    Soil:
    {environment["soil"]}

    Climate:
    {environment["climate"]}

    Land:
    {environment["land"]}

    Biodiversity:
    {environment["biodiversity"]}

    Human impact:
    {environment["human_impact"]}

    Find scientific evidence related to:
    soil health, soil organic carbon, water availability,
    biodiversity, habitat diversity, pollinators,
    climate stress, land use and vegetation management.
    """

    # -----------------------------------
    # 3. RETRIEVE SCIENTIFIC EVIDENCE
    # -----------------------------------

    evidence = retrieve(query)

    # -----------------------------------
    # 4. CREATE RECOMMENDATIONS
    # -----------------------------------

    recommendations = []

    risks = reasoning["risk_factors"]

    # Recommendation 1:
    # Low soil carbon + water stress
    if (
        "low_soil_carbon" in risks
        and "water_stress" in risks
    ):

        recommendations.append({
            "action": (
                "Introduce appropriate soil-cover practices "
                "and diversified vegetation."
            ),

            "why": (
                "Low soil organic carbon and low rainfall indicate "
                "combined soil-health and water-related ecological "
                "stress. Improving soil cover and vegetation diversity "
                "can address both conditions."
            ),

            "affected_metrics": [
                "soil organic carbon",
                "soil structure",
                "water regulation",
                "habitat diversity",
                "biodiversity"
            ],

            "time_horizon": "medium to long term",

            "scientific_evidence": [
                {
                    "source": "FAO",
                    "title": "Recarbonizing Global Soils",
                    "reason": (
                        "Supports the relationship between soil organic "
                        "carbon, soil health, soil structure and "
                        "water-related functions."
                    )
                },
                {
                    "source": "FAO",
                    "title": "Soil Organic Cover",
                    "reason": (
                        "Supports the use of soil cover to reduce "
                        "soil degradation and support soil organisms "
                        "and biodiversity."
                    )
                },
                {
                    "source": "FAO",
                    "title": "Water and Soil Management",
                    "reason": (
                        "Supports the relationship between soil organic "
                        "matter, vegetation management and water "
                        "retention."
                    )
                }
            ]
        })

    # Recommendation 2:
    # Monoculture + low species richness
    if (
        "low_land_diversity" in risks
        and "low_species_richness" in risks
    ):

        recommendations.append({
            "action": (
                "Introduce suitable crop diversification "
                "and habitat strips."
            ),

            "why": (
                "Monoculture and low species richness suggest "
                "simplified habitat conditions. Increasing vegetation "
                "diversity can provide additional habitat and "
                "ecological resources."
            ),

            "affected_metrics": [
                "crop diversity",
                "habitat diversity",
                "species richness",
                "pollinator support"
            ],

            "time_horizon": "short to medium term",

            "scientific_evidence": [
                {
                    "source": "FAO",
                    "title": "Conservation Agriculture",
                    "reason": (
                        "Supports crop diversification and soil-cover "
                        "practices as components of conservation "
                        "agriculture."
                    )
                },
                {
                    "source": "IPBES",
                    "title": "Global Assessment Report on Biodiversity",
                    "reason": (
                        "Supports the relationship between land-use "
                        "change, habitat condition and biodiversity."
                    )
                },
                {
                    "source": "IPBES",
                    "title": "Biodiversity and Ecosystem Services",
                    "reason": (
                        "Supports the relationship between habitat "
                        "modification and biodiversity."
                    )
                }
            ]
        })

    # Recommendation 3:
    # Monoculture + low pollinators
    if (
        "low_land_diversity" in risks
        and "low_pollinator_support" in risks
    ):

        recommendations.append({
            "action": (
                "Create flowering habitat strips using locally "
                "appropriate plant species."
            ),

            "why": (
                "Low crop diversity combined with low pollinator "
                "abundance suggests limited food and habitat "
                "resources for pollinators."
            ),

            "affected_metrics": [
                "pollinator abundance",
                "habitat diversity",
                "plant diversity",
                "biodiversity"
            ],

            "time_horizon": "short to medium term",

            "scientific_evidence": [
                {
                    "source": "IPBES",
                    "title": "Biodiversity and Ecosystem Services",
                    "reason": (
                        "Supports the importance of habitat availability "
                        "and ecological conditions for biodiversity."
                    )
                },
                {
                    "source": "FAO",
                    "title": "Agroforestry",
                    "reason": (
                        "Supports vegetation diversity and habitat "
                        "provision as components of biodiversity-friendly "
                        "land management."
                    )
                }
            ]
        })

    # -----------------------------------
    # 5. DEFAULT RECOMMENDATION
    # -----------------------------------

    if not recommendations:

        recommendations.append({
            "action": (
                "Increase habitat and vegetation diversity using "
                "locally appropriate species."
            ),

            "why": (
                "Increasing habitat diversity can provide resources "
                "for different organisms and support ecosystem functions."
            ),

            "affected_metrics": [
                "habitat diversity",
                "species richness"
            ],

            "time_horizon": "medium to long term",

            "scientific_evidence": [
                {
                    "source": "IPBES",
                    "title": "Biodiversity and Ecosystem Services",
                    "reason": (
                        "Supports the relationship between habitat "
                        "conditions and biodiversity."
                    )
                }
            ]
        })

    # -----------------------------------
    # 6. FINAL RESPONSE
    # -----------------------------------

    return {
        "environmental_assessment": reasoning,

        "retrieved_scientific_evidence": evidence,

        "recommendations": recommendations,

        "note": (
            "Recommendations are evidence-informed decision support. "
            "Actual outcomes depend on local soil, climate, species "
            "and management conditions."
        )
    }

@app.post("/chat")
def chat(request: ChatRequest):

    message = request.message.strip()

    # -----------------------------------
    # CHECK USER MESSAGE
    # -----------------------------------

    if not message:
        return {
            "type": "clarification",
            "message": (
                "Please describe the environmental situation "
                "you want me to analyze."
            )
        }

    # -----------------------------------
    # USE STRUCTURED DATA IF PROVIDED
    # -----------------------------------

        # Extract environmental information from natural language
    if not request.environment:
        extracted_environment = extract_environment_from_text(message)

        has_data = any(
            extracted_environment[category]
            for category in extracted_environment
        )

        if has_data:
            reasoning = analyze_environment(extracted_environment)
            recommendations = generate_recommendations(reasoning)

            query = f"""
            User question:
            {message}

            Extracted environmental data:
            Soil: {extracted_environment["soil"]}
            Climate: {extracted_environment["climate"]}
            Land: {extracted_environment["land"]}
            Biodiversity: {extracted_environment["biodiversity"]}
            Human impact: {extracted_environment["human_impact"]}

            Find scientific evidence relevant to the environmental
            conditions and recommended management actions.
            """

            evidence = retrieve(query)

            return {
                "type": "environmental_analysis",
                "user_question": message,
                "extracted_environment": extracted_environment,
                "environmental_assessment": reasoning,
                "recommendations": recommendations,
                "scientific_evidence": evidence,
                "message": (
                    "I extracted environmental variables from your "
                    "question, analyzed the conditions, and retrieved "
                    "relevant scientific evidence."
                )
            }
        
    if request.environment:

        environment = request.environment.model_dump()

        reasoning = analyze_environment(environment)

        query = f"""
        User question:
        {message}

        Environmental data:
        Soil: {environment["soil"]}
        Climate: {environment["climate"]}
        Land: {environment["land"]}
        Biodiversity: {environment["biodiversity"]}
        Human impact: {environment["human_impact"]}

        Find scientific evidence relevant to the user's question
        and the environmental conditions.
        """

        evidence = retrieve(query)

        return {
            "type": "environmental_analysis",
            "user_question": message,
            "environmental_assessment": reasoning,
            "scientific_evidence": evidence,
            "message": (
                "I analyzed the environmental variables and "
                "retrieved relevant scientific evidence."
            )
        }

    # -----------------------------------
    # TEXT-ONLY QUERY
    # -----------------------------------

    query = f"""
    Environmental biodiversity question:

    {message}

    Find scientific evidence related to soil health,
    biodiversity, habitat diversity, climate,
    water availability, land use and ecological management.
    """

    evidence = retrieve(query)

    # -----------------------------------
    # CLARIFICATION
    # -----------------------------------

    environmental_keywords = [
        "soil",
        "carbon",
        "ph",
        "moisture",
        "rainfall",
        "temperature",
        "climate",
        "biodiversity",
        "species",
        "pollinator",
        "habitat",
        "land",
        "forest",
        "deforestation",
        "water",
        "crop",
        "agriculture",
        "pollution",
        "ecosystem"
    ]

    message_lower = message.lower()

    has_environmental_context = any(
        keyword in message_lower
        for keyword in environmental_keywords
    )

    if not has_environmental_context:

        return {
            "type": "clarification",
            "message": (
                "I can help analyze biodiversity and environmental "
                "conditions. Please provide information such as "
                "soil health, rainfall, temperature, land use, "
                "biodiversity or human impact."
            ),
            "example": (
                "Example: My farm has low soil carbon, "
                "450 mm rainfall, monoculture crops and "
                "low pollinator abundance. What should I do?"
            )
        }

    # -----------------------------------
    # TEXT RESPONSE
    # -----------------------------------

    return {
        "type": "evidence_retrieval",
        "user_question": message,
        "scientific_evidence": evidence,
        "message": (
            "I found scientific evidence relevant to your "
            "environmental question. For a more specific "
            "recommendation, provide structured information "
            "such as soil carbon, soil moisture, rainfall, "
            "temperature, land use and biodiversity indicators."
        )
    }