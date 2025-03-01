function callApi() {
    const givenName = document.getElementById("givenName").value;
    const actualName = document.getElementById("actualName").value;

    fetch("/api/similarity", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ givenName, actualName })
    })
    .then(response => response.json())
    .then(data => {
        const responseElement = document.getElementById("response");
        responseElement.innerText = `Match Percentage: ${data.similarity_percentage}%`;

        // Apply color based on percentage
        responseElement.className = "response-container";
        if (data.similarity_percentage < 30) {
            responseElement.classList.add("red");
        } else if (data.similarity_percentage < 50) {
            responseElement.classList.add("orange");
        } else if (data.similarity_percentage < 80) {
            responseElement.classList.add("yellow");
        } else {
            responseElement.classList.add("green");
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
