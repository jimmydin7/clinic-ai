function showFlashNotification(message, category) {
    const notification = document.createElement('div');
    notification.className = `flash-notification ${category}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 4000);
}
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            showFlashNotification("{{ message }}", "{{ category }}");
        {% endfor %}
    {% endif %}
{% endwith %}