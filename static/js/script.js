function checkEnter(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    displayMessage(userInput, 'user-message');

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'user_input=' + encodeURIComponent(userInput)
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.response, 'bot-message');
        document.getElementById('user-input').value = '';
    });
}

function displayMessage(message, className) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${className}`;
    messageElement.innerText = message;
    document.getElementById('chat-messages').appendChild(messageElement);
    document.getElementById('chat-messages').scrollTop = document.getElementById('chat-messages').scrollHeight;
}

document.getElementById('game-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const userChoice = document.getElementById('user_choice').value;
    const numPlayers = document.getElementById('num_players').value;
    fetch('/play_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_choice: userChoice, num_players: numPlayers }),
    })
    .then(response => response.json())
    .then(data => {
        const chatbox = document.getElementById('chatbox');
        chatbox.innerHTML += `<p>${data.result}</p>`;
        chatbox.innerHTML += `<p>Computer Choices: ${data.computer_choices.join(', ')}</p>`;
    });
});
function scanPage() {
    window.location.href = "{{ url_for('scan') }}";
}