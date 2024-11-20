async function fetchData() {
    const response = await fetch('/data');
    const data = await response.json();
    for (const [key, value] of Object.entries(data)) {
        const element = document.getElementById(key);
        if (element) {
            element.textContent = `${key === 'T' ? 'Temperature' : key === 'H' ? 'Humidity' : 'Loop Count'}: ${value}`;
        }
    }
}

setInterval(fetchData, 1000);