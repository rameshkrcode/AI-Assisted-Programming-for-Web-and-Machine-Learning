fetch("https://api.example.com/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ features: [1.2, 3.4, 5.6] })
})
.then(res => res.json())
.then(data => console.log("Prediction:", data.prediction));
