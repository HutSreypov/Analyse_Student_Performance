// Example: Chart.js for student performance (can be used in analysis page)
document.addEventListener("DOMContentLoaded", function () {
    // Example chart container
    const ctx = document.getElementById("performanceChart");
    if (ctx) {
        const chart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["Sokha", "Dara", "Sreypov"],
                datasets: [{
                    label: "Average Score",
                    data: [85, 92, 78],
                    backgroundColor: ["#3498db", "#2ecc71", "#e74c3c"]
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true, max: 100 }
                }
            }
        });
    }
});
