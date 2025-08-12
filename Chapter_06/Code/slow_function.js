
function slowFunction() {
    let start = Date.now();
    while (Date.now() - start < 5000) {}  // 🚨 Freezes UI for 5 seconds
}
