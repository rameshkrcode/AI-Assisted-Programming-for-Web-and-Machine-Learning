
async function optimizedFunction() {
    await new Promise(resolve => setTimeout(resolve, 5000)); // ✅ Non-blocking delay
}
