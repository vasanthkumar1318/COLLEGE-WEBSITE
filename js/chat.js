let currentConversationId = null;
let isWaitingForResponse = false;

document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('userInput');
    const sendBtn = document.getElementById('send-btn');
    const messagesContainer = document.getElementById('messages');

    // Enter to send
    inputField.addEventListener('keypress', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Prevent form submission or newline
            sendBtn.click();
        }
    });

    sendBtn.addEventListener('click', handleSendMessage);
});

function handleSendMessage() {
    const inputField = document.getElementById('userInput');
    const text = inputField.value.trim();
    
    if (text === '' || isWaitingForResponse) return;

    if (!currentConversationId) {
        currentConversationId = HistoryManager.createNewConversation(text);
    }

    // Add user message
    addMessageToUI('user', text);
    HistoryManager.addMessage(currentConversationId, 'user', text);
    inputField.value = '';
    
    isWaitingForResponse = true;
    showTypingIndicator();

    // Simulate API delay
    setTimeout(() => {
        removeTypingIndicator();
        const reply = generateBotResponse(text);
        addMessageToUI('bot', reply);
        HistoryManager.addMessage(currentConversationId, 'bot', reply);
        isWaitingForResponse = false;
    }, 600);
}

function addMessageToUI(sender, text) {
    const messagesContainer = document.getElementById('messages');
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender}`;
    msgDiv.innerHTML = text;
    
    const timeSpan = document.createElement('span');
    timeSpan.className = 'timestamp';
    const now = new Date();
    timeSpan.innerText = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    msgDiv.appendChild(timeSpan);
    
    messagesContainer.appendChild(msgDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function showTypingIndicator() {
    const messagesContainer = document.getElementById('messages');
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message bot typing-indicator';
    msgDiv.id = 'typing-indicator';
    msgDiv.innerHTML = 'KESAV is typing...';
    messagesContainer.appendChild(msgDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function removeTypingIndicator() {
    const el = document.getElementById('typing-indicator');
    if (el) el.remove();
}

function clearChatUI() {
    document.getElementById('messages').innerHTML = '';
}

function loadChatToUI(messages) {
    clearChatUI();
    if(messages.length === 0) {
        addMessageToUI('bot', "Hello 👋 I am <b>KESAV</b>. I can help you with Academic Information, Admission & Fees Details, Faculty & Administration, Campus & Facilities, Emergency & Important Info, Contact & Location, Events & Activities, Student Support.");
    }
    messages.forEach(msg => {
        addMessageToUI(msg.sender, msg.text);
    });
}

function generateBotResponse(input) {
    input = input.toLowerCase();
    let reply = "Sorry, I couldn't understand. Please contact the college office or check the College Details tab.";

    if (input.includes("hi") || input.includes("hello")) {
        reply = "Hello! 👋 I am KESAV. How can I assist you today?";
    }
    // 1. ACADEMIC
    else if (input.includes("academic") || input.includes("academics")) {
        reply = "I can provide information on departments, course duration, syllabus, academic calendar, exam schedule, results, and internal assessment.";
    }
    else if (input.includes("department") || input.includes("program") || input.includes("course")) {
        reply = "The college offers Science (B.Sc. in CS, Maths, Psychology, IT, AI & ML), Commerce (B.Com., B.Com CA, PA), Arts (B.A. English, Political Science), Management (BBA), and Value-Added Courses.";
    }
    else if (input.includes("duration") || input.includes("eligibility")) {
        reply = "UG courses are 3 years (10+2 required). PG courses are 2 years (relevant UG degree required).";
    }
    // 2. ADMISSION & FEES
    else if (input.includes("admission") || input.includes("apply")) {
        reply = "Admissions are done based on merit through online and offline application. Check the College Details tab for full info.";
    }
    else if (input.includes("fee") || input.includes("cost")) {
        reply = "Fee structure varies by course (e.g., B.Sc 35,000/-, B.Com 35,000/-) and is payable year-wise or semester-wise.";
    }
    // 3. FACULTY & ADMIN
    else if (input.includes("faculty") || input.includes("principal")) {
        reply = "The college is managed by an experienced Principal and qualified faculty members for each department.";
    }
    // 4. CAMPUS
    else if (input.includes("campus") || input.includes("facilities") || input.includes("library") || input.includes("hostel")) {
        reply = "We have well-equipped labs, a rich library, separate hostels, transport buses, a hygienic canteen, sports facilities, and medical support.";
    }
    // 5. SUPPORT
    else if (input.includes("placement") || input.includes("internship")) {
        reply = "ACAS provides dedicated career services. In 2024, over 1,000 job offers were made with top recruiters like Toyota, Cognizant, Accenture, Infosys.";
    }
    // 6. EVENTS
    else if (input.includes("event") || input.includes("festival") || input.includes("cultural")) {
        reply = "We host events like Onam, Pongal, Nrithya (mega cultural fest), Techno Fest, and various department symposiums.";
    }
    // 7. CONTACT
    else if (input.includes("location") || input.includes("address") || input.includes("where")) {
        reply = `The college is located at <b>Kurumbapalayam (641107), Coimbatore, Tamil Nadu</b>.<br><a href="https://maps.app.goo.gl/AJ35E65KCFsMQxYm6" target="_blank">View on Google Maps</a>`;
    }
    else if (input.includes("contact") || input.includes("phone")) {
        reply = "You can contact us at +91 6384363843 or email infoadithyacas@gmail.com. Office hours: 8:30 AM to 4:30 PM.";
    }
    else if (input.includes("thank you") || input.includes("thanks")) {
        reply = "You're welcome! If you have more questions, feel free to ask.";
    }
    
    return reply;
}