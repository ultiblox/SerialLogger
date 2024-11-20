async function fetchData() {
    try {
        const response = await fetch('/data');
        const data = await response.json();

        // Update gauges by refreshing their images
        document.getElementById('temperatureGauge').src = `/gauge/T?time=${Date.now()}`;
        document.getElementById('humidityGauge').src = `/gauge/H?time=${Date.now()}`;

        // Update Loop Count
        if (data.L) {
            document.getElementById('loopCount').textContent = parseInt(data.L, 10);
        }
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

setInterval(fetchData, 1000);