const ctx = document.getElementById('healthChart').getContext('2d');
const healthChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: Array.from({length: 63}, (_, i) => i + 18), // Ages 18–80
        datasets: [
            {
                label: 'Average Score by Age',
                data: Array.from({length: 63}, () => Math.floor(Math.random() * 40 + 60)), // Random scores
                borderColor: '#406e8e',
                backgroundColor: 'transparent',
                borderWidth: 2,
                tension: 0.3
            },
            {
                label: 'Your Score',
                data: [{
                    x: {{ session['age'] }},
                    y: {{ session.get('health_score', 75) }}
                }],
                backgroundColor: '#ff3b3b',
                pointRadius: 6,
                pointHoverRadius: 8,
                type: 'scatter'
            }
        ]
    },
    options: {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Age'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Health Score'
                },
                beginAtZero: true,
                max: 100
            }
        },
        plugins: {
            legend: {
                display: true
            }
        }
    }
});