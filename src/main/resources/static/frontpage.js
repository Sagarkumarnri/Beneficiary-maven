function callApi() {
    const givenName = document.getElementById("givenName").value.trim();
    const actualName = document.getElementById("actualName").value.trim();

    if (!givenName || !actualName) {
        alert("Please enter both given and actual names.");
        return;
    }

    fetch("http://localhost:8080/api/similarity", {  // Use full API URL
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ givenName, actualName })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const responseElement = document.getElementById("response");
        responseElement.innerText = `Match Percentage: ${data.similarity_percentage}%`;

        // Reset previous color classes
        responseElement.className = "response-container";

        // Apply color based on percentage
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
        alert("Failed to fetch match percentage. Please try again later.");
    });
}
 function train() {
     const trainButton = document.querySelector(".train-button");
     trainButton.innerHTML = "Training... <span class='loader'></span>";
     trainButton.disabled = true;

     fetch("http://localhost:8080/api/train", {
         method: "POST",
         headers: {
             "Content-Type": "application/json"
         }
     })
     .then(response => {

        alert(response.data);
     })


 }
