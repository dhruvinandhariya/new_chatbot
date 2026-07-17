document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.getElementById("send-button");
    const userInput = document.getElementById("user-input");
    const chatHistory = document.getElementById("chat-history");

    sendButton.addEventListener("click", async () => {
        const inputText = userInput.value.trim();
        if (!inputText) return;

        const userMessage = document.createElement("div");
        userMessage.className = "user";
        userMessage.innerHTML = `<strong>User:</strong> ${inputText}`;
        chatHistory.appendChild(userMessage);

        userInput.value = "";

        try {
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ input: inputText })
            });

            const data = await response.json();

            const botMessage = document.createElement("div");
            botMessage.className = "bot";
            botMessage.innerHTML = `<strong>Bot:</strong> ${data.answer || "No response."}`;
            chatHistory.appendChild(botMessage);

        } catch (error) {
            console.error("Error:", error);
            const errorMessage = document.createElement("div");
            errorMessage.className = "bot";
            errorMessage.innerHTML = `<strong>Bot:</strong> Something went wrong.`;
            chatHistory.appendChild(errorMessage);
        }

        chatHistory.scrollTop = chatHistory.scrollHeight;
    });
});
