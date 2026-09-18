const API_URL = "http://127.0.0.1:8000/chat";

const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const chatMessages = document.getElementById("chatMessages");


// Send message when button is clicked
sendButton.addEventListener("click", sendMessage);


// Send message when Enter is pressed
messageInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});


async function sendMessage() {

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }


    // Display user's message
    addMessage(message, "user");


    // Clear input
    messageInput.value = "";


    // Disable button while processing
    sendButton.disabled = true;
    sendButton.textContent = "Thinking...";


    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        if (!response.ok) {
            throw new Error("Backend request failed");
        }


        const data = await response.json();


        // Display backend response
        displayResponse(data);


    } catch (error) {

        addMessage(
            "⚠️ I could not connect to the EcoIntel AI backend. Please make sure the FastAPI server is running.",
            "bot"
        );

        console.error(error);

    }


    // Enable button again
    sendButton.disabled = false;
    sendButton.textContent = "Send";
}



function addMessage(text, type) {

    const messageDiv = document.createElement("div");

    messageDiv.className = `message ${type}-message`;

    messageDiv.textContent = text;

    chatMessages.appendChild(messageDiv);

    scrollToBottom();
}



function displayResponse(data) {

    const messageDiv = document.createElement("div");

    messageDiv.className = "message bot-message";


    // Clarification response
    if (data.type === "clarification") {

        messageDiv.innerHTML = `
            <strong>EcoIntel AI</strong>
            <p>${data.message}</p>
        `;

        chatMessages.appendChild(messageDiv);

        scrollToBottom();

        return;
    }


    // Environmental analysis response
    if (data.type === "environmental_analysis") {

        let html = `
            <strong>🌿 EcoIntel AI</strong>

            <p style="margin-top:10px;">
                I analyzed the environmental conditions you provided.
            </p>
        `;


        // Findings
        if (
            data.environmental_assessment &&
            data.environmental_assessment.findings.length > 0
        ) {

            html += `
                <div class="evidence">
                    <h4>⚠️ Environmental Assessment</h4>
            `;

            data.environmental_assessment.findings.forEach(
                finding => {

                    html += `
                        <div class="evidence-item">
                            ${finding}
                        </div>
                    `;

                }
            );

            html += `</div>`;
        }


        // Relationships
        if (
            data.environmental_assessment &&
            data.environmental_assessment.relationships.length > 0
        ) {

            html += `
                <div class="evidence">
                    <h4>🔗 Multi-Metric Relationships</h4>
            `;

            data.environmental_assessment.relationships.forEach(
                relationship => {

                    html += `
                        <div class="evidence-item">
                            ${relationship}
                        </div>
                    `;

                }
            );

            html += `</div>`;
        }


        // Recommendations
        if (
            data.recommendations &&
            data.recommendations.length > 0
        ) {

            html += `
                <div class="evidence">
                    <h4>💡 Recommendations</h4>
            `;


            data.recommendations.forEach(
                (recommendation, index) => {

                    html += `
                        <div class="recommendation">

                            <h4>
                                Recommendation ${index + 1}
                            </h4>

                            <p>
                                <strong>What to do:</strong>
                                ${recommendation.action}
                            </p>

                            <p>
                                <strong>Why:</strong>
                                ${recommendation.why}
                            </p>

                            <p>
                                <strong>Time horizon:</strong>
                                ${recommendation.time_horizon}
                            </p>

                            <div class="metrics">

                                <strong>
                                    Affected metrics:
                                </strong>

                    `;


                    recommendation.affected_metrics.forEach(
                        metric => {

                            html += `
                                <span class="metric">
                                    ${metric}
                                </span>
                            `;

                        }
                    );


                    html += `
                            </div>

                        </div>
                    `;

                }
            );


            html += `</div>`;
        }


        // Scientific evidence
        if (
            data.scientific_evidence &&
            data.scientific_evidence.length > 0
        ) {

            html += `
                <div class="evidence">

                    <h4>📚 Scientific Evidence</h4>
            `;


            data.scientific_evidence.forEach(
                evidence => {

                    html += `
                        <div class="evidence-item">

                            <strong>
                                ${evidence.source}
                            </strong>

                            — ${evidence.title}

                            <br>

                            <span class="score">
                                Relevance score:
                                ${evidence.relevance_score}
                            </span>

                        </div>
                    `;

                }
            );


            html += `</div>`;
        }


        messageDiv.innerHTML = html;

        chatMessages.appendChild(messageDiv);

        scrollToBottom();

        return;
    }


    // Evidence-only response
    if (data.type === "evidence_retrieval") {

        messageDiv.innerHTML = `
            <strong>🌿 EcoIntel AI</strong>

            <p style="margin-top:10px;">
                ${data.message}
            </p>
        `;

        chatMessages.appendChild(messageDiv);

        scrollToBottom();

        return;
    }


    // Fallback
    messageDiv.textContent =
        "EcoIntel AI returned a response, but it could not be displayed.";

    chatMessages.appendChild(messageDiv);

    scrollToBottom();
}



function scrollToBottom() {

    const container = document.querySelector(".chat-container");

    container.scrollTop = container.scrollHeight;

}