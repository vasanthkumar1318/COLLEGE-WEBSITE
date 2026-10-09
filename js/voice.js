document.addEventListener('DOMContentLoaded', () => {
    const micBtn = document.getElementById('mic-btn');
    const stopBtn = document.getElementById('stop-mic-btn');
    const inputField = document.getElementById('userInput');
    const statusDiv = document.getElementById('voice-status');

    // Web Speech API
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    let recognition = null;

    if (SpeechRecognition) {
        recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US'; // Could add language toggle

        recognition.onstart = function() {
            micBtn.classList.add('listening');
            statusDiv.classList.remove('hidden');
        };

        recognition.onresult = function(event) {
            const text = event.results[0][0].transcript;
            const currentVal = inputField.value;
            inputField.value = currentVal ? currentVal + ' ' + text : text;
            inputField.focus(); // Allow user to edit or send
        };

        recognition.onerror = function(event) {
            console.error('Speech recognition error', event.error);
            alert('Voice recognition error: ' + event.error);
            resetVoiceUI();
        };

        recognition.onend = function() {
            resetVoiceUI();
        };

        micBtn.addEventListener('click', () => {
            if (micBtn.classList.contains('listening')) {
                recognition.stop();
            } else {
                try {
                    recognition.start();
                } catch(e) {
                    console.error("Already started");
                }
            }
        });

        stopBtn.addEventListener('click', () => {
            if(recognition) recognition.stop();
        });

    } else {
        micBtn.addEventListener('click', () => {
            alert('Voice recognition is not supported in this browser. Please use Chrome or Edge.');
        });
    }

    function resetVoiceUI() {
        micBtn.classList.remove('listening');
        statusDiv.classList.add('hidden');
    }
});