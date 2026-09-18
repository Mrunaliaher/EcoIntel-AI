def extract_environment_from_text(message):
    text = message.lower()

    environment = {
        "soil": {},
        "climate": {},
        "land": {},
        "biodiversity": {},
        "human_impact": {}
    }

    # Soil
    if "low soil carbon" in text or "low organic carbon" in text:
        environment["soil"]["organic_carbon"] = 0.5

    if "low soil moisture" in text:
        environment["soil"]["moisture"] = 15

    if "acidic soil" in text:
        environment["soil"]["ph"] = 5.0

    if "alkaline soil" in text:
        environment["soil"]["ph"] = 9.0

    # Climate
    if "low rainfall" in text:
        environment["climate"]["rainfall"] = 450

    if "high rainfall" in text:
        environment["climate"]["rainfall"] = 1200

    if "high temperature" in text or "heat stress" in text:
        environment["climate"]["temperature"] = 35

    # Land use
    if "monoculture" in text:
        environment["land"]["land_use"] = "monoculture"

    if "agroforestry" in text:
        environment["land"]["land_use"] = "agroforestry"

    # Biodiversity
    if (
        "very few pollinators" in text
        or "low pollinator" in text
        or "few pollinators" in text
    ):
        environment["biodiversity"]["pollinator_abundance"] = "low"

    if "low species richness" in text:
        environment["biodiversity"]["species_richness"] = "low"

    if "high species richness" in text:
        environment["biodiversity"]["species_richness"] = "high"

    # Human impact
    if "high pollution" in text:
        environment["human_impact"]["pollution"] = "high"

    if "moderate pollution" in text:
        environment["human_impact"]["pollution"] = "moderate"

    return environment

def analyze_environment(data):
    soil = data.get("soil", {})
    climate = data.get("climate", {})
    land = data.get("land", {})
    biodiversity = data.get("biodiversity", {})
    human_impact = data.get("human_impact", {})

    findings = []
    relationships = []
    risk_factors = []

    # Environmental variables
    soc = soil.get("organic_carbon")
    ph = soil.get("ph")
    moisture = soil.get("moisture")

    rainfall = climate.get("rainfall")
    temperature = climate.get("temperature")

    land_use = land.get("land_use", "").lower()

    species_richness = biodiversity.get(
        "species_richness", ""
    ).lower()

    pollinators = biodiversity.get(
        "pollinator_abundance", ""
    ).lower()

    # -----------------------------
    # SOIL ANALYSIS
    # -----------------------------

    if soc is not None and soc < 1:
        findings.append(
            "Soil organic carbon is low, indicating a potential soil-health concern."
        )
        risk_factors.append("low_soil_carbon")

    if ph is not None and (ph < 5.5 or ph > 8.5):
        findings.append(
            "Soil pH is outside a broadly favorable range for many crops."
        )
        risk_factors.append("unfavorable_ph")

    if moisture is not None and moisture < 20:
        findings.append(
            "Low soil moisture may indicate water stress."
        )
        risk_factors.append("low_soil_moisture")

    # -----------------------------
    # CLIMATE ANALYSIS
    # -----------------------------

    if rainfall is not None and rainfall < 600:
        findings.append(
            "Annual rainfall is relatively low, indicating potential water stress."
        )
        risk_factors.append("water_stress")

    if temperature is not None and temperature > 30:
        findings.append(
            "High temperature may increase climate-related ecological stress."
        )
        risk_factors.append("heat_stress")

    # -----------------------------
    # LAND USE ANALYSIS
    # -----------------------------

    if land_use == "monoculture":
        findings.append(
            "Monoculture indicates relatively low crop diversity "
            "and potentially simplified habitat."
        )
        risk_factors.append("low_land_diversity")

    # -----------------------------
    # BIODIVERSITY ANALYSIS
    # -----------------------------

    if species_richness == "low":
        findings.append(
            "Low species richness indicates biodiversity pressure."
        )
        risk_factors.append("low_species_richness")

    if pollinators == "low":
        findings.append(
            "Low pollinator abundance indicates reduced pollinator "
            "habitat or resource availability."
        )
        risk_factors.append("low_pollinator_support")

    # -----------------------------
    # MULTI-METRIC REASONING
    # -----------------------------

    if (
        "low_soil_carbon" in risk_factors
        and "water_stress" in risk_factors
    ):
        relationships.append(
            "Low soil organic carbon combined with low rainfall "
            "may increase water-related ecological stress because "
            "soil condition and water availability interact."
        )

    if (
        "low_land_diversity" in risk_factors
        and "low_species_richness" in risk_factors
    ):
        relationships.append(
            "Monoculture combined with low species richness suggests "
            "habitat simplification and reduced ecological diversity."
        )

    if (
        "low_land_diversity" in risk_factors
        and "low_pollinator_support" in risk_factors
    ):
        relationships.append(
            "Low crop diversity and low pollinator abundance indicate "
            "a potential lack of diverse food and habitat resources "
            "for pollinators."
        )

    return {
        "findings": findings,
        "relationships": relationships,
        "risk_factors": risk_factors
    }

def generate_recommendations(reasoning):
    recommendations = []

    risks = reasoning["risk_factors"]

    # Soil carbon + water stress
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
            "time_horizon": "medium to long term"
        })

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
            "time_horizon": "short to medium term"
        })

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
            "time_horizon": "short to medium term"
        })

    # General recommendation
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
            "time_horizon": "medium to long term"
        })

    return recommendations