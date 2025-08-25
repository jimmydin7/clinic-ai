// Question form handling
document.addEventListener('DOMContentLoaded', function() {
    // Handle scale type questions
    const scaleBoxes = document.querySelectorAll('.scale-box');
    if (scaleBoxes.length > 0) {
        scaleBoxes.forEach(box => {
            box.addEventListener('click', function() {
                // Remove active class from all boxes
                scaleBoxes.forEach(b => b.classList.remove('bg-blue-500', 'text-white'));
                // Add active class to clicked box
                this.classList.add('bg-blue-500', 'text-white');
                // Set the hidden input value
                document.getElementById('scale-value').value = this.dataset.value;
            });
        });
    }
    
    // Form validation
    const form = document.getElementById('question-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const answer = document.querySelector('input[name="answer"], select[name="answer"]');
            if (!answer || !answer.value) {
                e.preventDefault();
                alert('Please provide an answer before continuing.');
                return false;
            }
        });
    }
});
