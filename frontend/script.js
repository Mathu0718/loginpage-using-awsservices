const apiUrl = "https://2rem4j59ti.execute-api.ap-south-1.amazonaws.com/prod"; // Replace with API Gateway URL

async function login() {
    const email = document.getElementById("email").value;

    if (!email) {
        alert("Please enter your email.");
        return;
    }

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            mode: "cors", // Ensures cross-origin requests work
            body: JSON.stringify({ action: "login", email })
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
    }
}

async function logout() {
    const email = document.getElementById("email").value;

    if (!email) {
        alert("Please enter your email.");
        return;
    }

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            mode: "cors",
            body: JSON.stringify({ action: "logout", email })
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
    }
}
