document.getElementById('health-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    
    // Get form data
    const formData = {
        weight: document.getElementById('weight').value,
        smoking: document.getElementById('smoking').value,
        diet: document.getElementById('diet').value
    };

    // Send the data to the Python script using a system call (via fetch)
    const response = await fetch('run_python_script.py', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    });

    const data = await response.json();
    document.getElementById('result').innerText = `Result: ${data.result}`;
});
