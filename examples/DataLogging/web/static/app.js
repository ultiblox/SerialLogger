document.addEventListener("DOMContentLoaded", () => {
    const connectButton = document.getElementById("connectButton");
    const portSelect = document.getElementById("portSelect");

    // Initialize gauges
    const { temperatureGauge, humidityGauge } = initializeGauges();

    // Load available ports
    loadPorts();

    // Handle Connect/Disconnect button click
    connectButton.addEventListener("click", async () => {
        if (connectButton.textContent === "Connect") {
            console.log("Connect button clicked. Attempting to connect...");
            await handleConnection("connect");
        } else {
            console.log("Disconnect button clicked. Attempting to disconnect...");
            await handleConnection("disconnect");
        }
    });

    async function loadPorts() {
        try {
            const response = await fetch('/ports');
            const ports = await response.json();
            console.log("Available ports:", ports);
            portSelect.innerHTML = ports.map(port => `<option value="${port}">${port}</option>`).join('');
        } catch (error) {
            console.error("Failed to load ports:", error);
            portSelect.innerHTML = `<option value="Auto">Auto</option>`;
        }
    }

    async function handleConnection(action) {
        try {
            // Update button state to show action in progress
            connectButton.textContent = action === "connect" ? "Connecting..." : "Disconnecting...";
            connectButton.disabled = true;
    
            // Perform the action
            const url = action === "connect" ? "/connect" : "/disconnect";
            const method = "POST";
            const body = action === "connect" ? JSON.stringify({ port: portSelect.value }) : null;
            console.log(`Sending ${action} request to ${url} with body:`, body);
    
            const response = await fetch(url, {
                method,
                headers: { "Content-Type": "application/json" },
                body,
            });
            const result = await response.json();
    
            console.log(`${action.charAt(0).toUpperCase() + action.slice(1)} response:`, result);
    
            if (result.success) {
                if (action === "connect") {
                    connectButton.textContent = "Disconnect";
    
                    // If "Auto" was used, update the dropdown to the detected port
                    if (portSelect.value === "Auto" && result.port) {
                        const detectedPort = result.port;
                        console.log(`Detected port: ${detectedPort}`);
                        portSelect.value = detectedPort;
    
                        // Add detected port to dropdown if it doesn't exist
                        if (!Array.from(portSelect.options).some(option => option.value === detectedPort)) {
                            const newOption = document.createElement("option");
                            newOption.value = detectedPort;
                            newOption.textContent = detectedPort;
                            portSelect.appendChild(newOption);
                        }
                    }
                } else {
                    connectButton.textContent = "Connect";
                }
            } else {
                alert(`${action === "connect" ? "Connection" : "Disconnection"} failed: ${result.error}`);
                connectButton.textContent = action === "connect" ? "Connect" : "Disconnect";
            }
        } catch (error) {
            console.error(`Error during ${action}:`, error);
            alert(`An error occurred while trying to ${action}.`);
        } finally {
            connectButton.disabled = false; // Re-enable the button
        }
    }

    setInterval(async () => {
        try {
            // Check connection status
            const statusResponse = await fetch("/status");
            const statusData = await statusResponse.json();
    
            // Fetch live data if connected
            if (statusData.status === "connected") {
                const dataResponse = await fetch("/data");
                const data = await dataResponse.json();
    
                console.log("Fetched data:", data);
    
                // Safely update UI elements with correct IDs
                const temperatureElement = document.getElementById("temperatureValue");
                const humidityElement = document.getElementById("humidityValue");
                const loopCountElement = document.getElementById("loopCount");
    
                if (temperatureElement) {
                    temperatureElement.textContent = `${data.T || 0} °C`;
                }
                if (humidityElement) {
                    humidityElement.textContent = `${data.H || 0} %`;
                }
                if (loopCountElement) {
                    loopCountElement.textContent = data.L || 0;
                }
    
                // Update gauges
                temperatureGauge.set(parseFloat(data.T) || 0);
                humidityGauge.set(parseFloat(data.H) || 0);
    
                if (connectButton.textContent === "Connect") {
                    connectButton.textContent = "Disconnect";
                }
            } else {
                if (connectButton.textContent === "Disconnect") {
                    connectButton.textContent = "Connect";
                }
            }
        } catch (error) {
            console.error("Error checking status or fetching data:", error);
        }
    }, 1000);

    // Initialize gauges function
    function initializeGauges() {
        const gaugeOptions = {
            angle: 0.15, // Arc span
            lineWidth: 0.2, // Thickness
            radiusScale: 1, // Radius scale
            pointer: {
                length: 0.6,
                strokeWidth: 0.035,
                color: '#000000',
            },
            limitMax: false,
            limitMin: false,
            colorStart: '#6F6EA0',
            colorStop: '#C0C0DB',
            strokeColor: '#EEEEEE',
            generateGradient: true,
            highDpiSupport: true,
        };

        // Create Temperature Gauge
        const temperatureCanvas = document.getElementById("temperatureGauge");
        const temperatureGauge = new Gauge(temperatureCanvas).setOptions(gaugeOptions);
        temperatureGauge.maxValue = 100; // Max temperature
        temperatureGauge.setMinValue(0); // Min temperature
        temperatureGauge.animationSpeed = 32; // Animation speed
        temperatureGauge.set(0); // Initial value

        // Create Humidity Gauge
        const humidityCanvas = document.getElementById("humidityGauge");
        const humidityGauge = new Gauge(humidityCanvas).setOptions(gaugeOptions);
        humidityGauge.maxValue = 100; // Max humidity
        humidityGauge.setMinValue(0); // Min humidity
        humidityGauge.animationSpeed = 32; // Animation speed
        humidityGauge.set(0); // Initial value

        return {
            temperatureGauge,
            humidityGauge,
        };
    }
});
