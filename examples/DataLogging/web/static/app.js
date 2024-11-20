// Define gauges
let temperatureGauge;
let humidityGauge;

// Initialize gauges
function initializeGauges() {
    const temperatureCanvas = document.getElementById('temperatureGauge');
    const humidityCanvas = document.getElementById('humidityGauge');

    if (!temperatureCanvas || !humidityCanvas) {
        console.error("Gauge canvas elements not found in DOM.");
        return;
    }

    // Temperature gauge
    temperatureGauge = new Gauge(temperatureCanvas).setOptions({
        angle: 0, // Full circle
        lineWidth: 0.2,
        radiusScale: 1,
        pointer: {
            length: 0.6,
            strokeWidth: 0.035,
            color: '#000000'
        },
        limitMax: false,
        limitMin: false,
        colorStart: '#6FADCF',
        colorStop: '#8FC0DA',
        strokeColor: '#E0E0E0',
        generateGradient: true
    });
    temperatureGauge.maxValue = 50;
    temperatureGauge.setMinValue(0);
    temperatureGauge.set(0);

    // Humidity gauge
    humidityGauge = new Gauge(humidityCanvas).setOptions({
        angle: 0, // Full circle
        lineWidth: 0.2,
        radiusScale: 1,
        pointer: {
            length: 0.6,
            strokeWidth: 0.035,
            color: '#000000'
        },
        limitMax: false,
        limitMin: false,
        colorStart: '#6FADCF',
        colorStop: '#8FC0DA',
        strokeColor: '#E0E0E0',
        generateGradient: true
    });
    humidityGauge.maxValue = 100;
    humidityGauge.setMinValue(0);
    humidityGauge.set(0);
}

// Fetch data and update gauges
async function fetchData() {
    try {
        const response = await fetch('/data');
        if (!response.ok) {
            throw new Error(`API responded with status ${response.status}`);
        }
        const data = await response.json();

        // Update gauges
        if (temperatureGauge) {
            temperatureGauge.set(data.T || 0);
        }
        if (humidityGauge) {
            humidityGauge.set(data.H || 0);
        }

        // Update textual values
        document.getElementById('temperatureValue').textContent = `${data.T?.toFixed(1) || 0} °C`;
        document.getElementById('humidityValue').textContent = `${data.H?.toFixed(1) || 0} %`;
        document.getElementById('loopCount').textContent = data.L || 0;
    } catch (error) {
        console.error('Fetch error:', error);
        document.getElementById('temperatureValue').textContent = 'Error';
        document.getElementById('humidityValue').textContent = 'Error';
        document.getElementById('loopCount').textContent = 'Error';
    }
}

// Initialize and start fetching data
document.addEventListener("DOMContentLoaded", () => {
    initializeGauges();
    setInterval(fetchData, 1000);
});