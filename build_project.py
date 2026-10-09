import os

files = {
    'index.html': """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KESAV - AI Student Assistant | Adithya College of Arts and Science</title>
    <link rel="stylesheet" href="css/style.css">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div id="app-container">
        <!-- Sidebar: Navigation & History -->
        <aside id="sidebar" class="sidebar">
            <div class="sidebar-header">
                <h2>🤖 KESAV</h2>
                <button id="close-sidebar-btn" class="mobile-only"><i class="fas fa-times"></i></button>
            </div>
            
            <nav class="main-nav">
                <button class="nav-btn active" data-target="chat-view"><i class="fas fa-comments"></i> Chat</button>
                <button class="nav-btn" data-target="gallery-view"><i class="fas fa-images"></i> Gallery</button>
                <button class="nav-btn" data-target="details-view"><i class="fas fa-info-circle"></i> College Details</button>
            </nav>

            <div class="history-section">
                <div class="history-header">
                    <h3>Chat History</h3>
                    <button id="new-chat-btn"><i class="fas fa-plus"></i> New</button>
                </div>
                <div class="search-history">
                    <input type="text" id="search-history-input" placeholder="Search chats...">
                </div>
                <ul id="conversation-list">
                    <!-- History items injected here -->
                </ul>
                <button id="clear-history-btn" class="danger-btn"><i class="fas fa-trash"></i> Clear All</button>
            </div>
        </aside>

        <!-- Main Content Area -->
        <main id="main-content">
            <!-- Header -->
            <header class="app-header">
                <div class="header-left">
                    <button id="toggle-sidebar-btn"><i class="fas fa-bars"></i></button>
                    <div>
                        <h1>Adithya College of Arts and Science</h1>
                        <p>Official AI Student Support Website</p>
                    </div>
                </div>
                <div class="header-right">
                    <button id="theme-toggle-btn"><i class="fas fa-moon"></i></button>
                </div>
            </header>

            <!-- Views Container -->
            <div id="views-container">
                
                <!-- Chat View -->
                <div id="chat-view" class="view active">
                    <div id="chat-container">
                        <div id="messages">
                            <!-- Messages will be injected here -->
                        </div>
                        
                        <!-- Quick Questions -->
                        <div id="quick-questions" class="quick-questions">
                            <button class="quick-q-btn">College Location</button>
                            <button class="quick-q-btn">Courses Offered</button>
                            <button class="quick-q-btn">Admission Process</button>
                            <button class="quick-q-btn">Fees Details</button>
                        </div>

                        <!-- Input Area -->
                        <div id="inputArea">
                            <input type="text" id="userInput" placeholder="Ask your question here... (Press Enter to send)" autocomplete="off" />
                            <button id="mic-btn" title="Voice Input"><i class="fas fa-microphone"></i></button>
                            <button id="send-btn" title="Send Message"><i class="fas fa-paper-plane"></i></button>
                        </div>
                        <div id="voice-status" class="hidden">Listening... <button id="stop-mic-btn">Stop</button></div>
                    </div>
                </div>

                <!-- Gallery View -->
                <div id="gallery-view" class="view hidden">
                    <div class="view-header">
                        <h2>College Gallery</h2>
                        <div class="gallery-filters" id="gallery-filters">
                            <button class="filter-btn active" data-filter="all">All Photos</button>
                            <button class="filter-btn" data-filter="campus">Campus</button>
                            <button class="filter-btn" data-filter="library">Library</button>
                            <button class="filter-btn" data-filter="events">Events</button>
                        </div>
                    </div>
                    <div class="gallery-grid" id="gallery-grid">
                        <!-- Images injected here -->
                    </div>
                </div>

                <!-- College Details View -->
                <div id="details-view" class="view hidden">
                    <div class="view-header">
                        <h2>College Details Dashboard</h2>
                    </div>
                    <div class="dashboard-grid" id="dashboard-content">
                        <!-- Content injected here via JS -->
                    </div>
                </div>

            </div>
        </main>
        
        <!-- Lightbox for Gallery -->
        <div id="lightbox" class="lightbox hidden">
            <span id="lightbox-close">&times;</span>
            <img class="lightbox-content" id="lightbox-img">
            <div id="lightbox-caption"></div>
            <a id="lightbox-prev">&#10094;</a>
            <a id="lightbox-next">&#10095;</a>
        </div>
    </div>

    <!-- Scripts -->
    <script src="data/college-info.js"></script>
    <script src="data/gallery-manifest.js"></script>
    <script src="js/history.js"></script>
    <script src="js/voice.js"></script>
    <script src="js/chat.js"></script>
    <script src="js/gallery.js"></script>
    <script src="js/college-details.js"></script>
    <script src="js/app.js"></script>
</body>
</html>
""",
    'css/style.css': """
:root {
    --primary-color: #4b6cb7;
    --primary-dark: #2c3e50;
    --secondary-color: #e3e8ff;
    --text-color: #333;
    --bg-color: #f4f7f6;
    --sidebar-bg: #ffffff;
    --card-bg: #ffffff;
    --border-color: #e0e0e0;
    --hover-color: #f0f0f0;
    --danger-color: #e74c3c;
    --shadow: 0 4px 6px rgba(0,0,0,0.1);
}

[data-theme="dark"] {
    --primary-color: #5c7cfa;
    --primary-dark: #1a1a2e;
    --secondary-color: #2a2a4a;
    --text-color: #f1f1f1;
    --bg-color: #121212;
    --sidebar-bg: #1e1e1e;
    --card-bg: #1e1e1e;
    --border-color: #333;
    --hover-color: #2c2c2c;
    --shadow: 0 4px 6px rgba(0,0,0,0.5);
}

* { margin: 0; padding: 0; box-sizing: border-box; font-family: "Segoe UI", Arial, sans-serif; }

body {
    background: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.55)), url("../images/adithya_college.png");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: var(--text-color);
    height: 100vh;
    overflow: hidden;
}

#app-container {
    display: flex;
    height: 100vh;
    width: 100%;
    background: rgba(var(--bg-color), 0.85); /* fallback if needed */
}

[data-theme="dark"] #app-container {
    background: rgba(18, 18, 18, 0.9);
}
[data-theme="light"] #app-container {
    background: rgba(244, 247, 246, 0.9);
}

/* Sidebar */
.sidebar {
    width: 300px;
    background-color: var(--sidebar-bg);
    border-right: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease;
    z-index: 100;
}

.sidebar-header {
    padding: 20px;
    background: linear-gradient(135deg, var(--primary-dark), var(--primary-color));
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.main-nav {
    display: flex;
    flex-direction: column;
    padding: 10px;
    border-bottom: 1px solid var(--border-color);
}

.nav-btn {
    padding: 12px 15px;
    margin-bottom: 5px;
    background: none;
    border: none;
    text-align: left;
    font-size: 16px;
    color: var(--text-color);
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.2s;
}

.nav-btn:hover { background: var(--hover-color); }
.nav-btn.active { background: var(--secondary-color); color: var(--primary-color); font-weight: bold; }
.nav-btn i { width: 25px; }

/* History Section */
.history-section {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 10px;
    overflow: hidden;
}

.history-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 5px;
}

#new-chat-btn {
    padding: 6px 12px;
    background: var(--primary-color);
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.search-history input {
    width: 100%;
    padding: 8px;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    background: var(--bg-color);
    color: var(--text-color);
    margin-bottom: 10px;
}

#conversation-list {
    flex: 1;
    overflow-y: auto;
    list-style: none;
}

.history-item {
    padding: 10px;
    margin-bottom: 5px;
    border-radius: 6px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.history-item:hover { background: var(--hover-color); }
.history-item.active { background: var(--secondary-color); border-left: 4px solid var(--primary-color); }

.history-title {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    flex: 1;
}
.history-actions button {
    background: none;
    border: none;
    color: var(--text-color);
    cursor: pointer;
    padding: 5px;
    opacity: 0.5;
}
.history-actions button:hover { opacity: 1; color: var(--danger-color); }

.danger-btn {
    margin-top: 10px;
    padding: 10px;
    background: var(--danger-color);
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

/* Main Content */
#main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.app-header {
    padding: 15px 20px;
    background: var(--sidebar-bg);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.header-left { display: flex; align-items: center; gap: 15px; }
.header-left h1 { font-size: 20px; color: var(--primary-color); }
.header-left p { font-size: 12px; opacity: 0.8; }

#toggle-sidebar-btn, #theme-toggle-btn {
    background: none;
    border: none;
    font-size: 20px;
    color: var(--text-color);
    cursor: pointer;
}

#views-container {
    flex: 1;
    position: relative;
    overflow: hidden;
}

.view {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    display: flex;
    flex-direction: column;
    background: var(--bg-color);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
    overflow-y: auto;
}
.view.active {
    opacity: 1;
    pointer-events: auto;
}

/* Chat View */
#chat-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    max-width: 900px;
    margin: 0 auto;
    width: 100%;
    padding: 20px;
}

#messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    background: var(--card-bg);
    border-radius: 12px;
    box-shadow: var(--shadow);
    margin-bottom: 15px;
    display: flex;
    flex-direction: column;
}

.message {
    max-width: 80%;
    padding: 12px 16px;
    margin: 8px 0;
    border-radius: 15px;
    font-size: 15px;
    line-height: 1.4;
    word-wrap: break-word;
    position: relative;
}

.message.user {
    background: var(--primary-color);
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 5px;
}

.message.bot {
    background: var(--secondary-color);
    color: var(--text-color);
    margin-right: auto;
    border-bottom-left-radius: 5px;
}

.timestamp {
    font-size: 10px;
    opacity: 0.7;
    margin-top: 5px;
    display: block;
    text-align: right;
}

.quick-questions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 15px;
}

.quick-q-btn {
    padding: 8px 15px;
    background: var(--card-bg);
    border: 1px solid var(--primary-color);
    color: var(--primary-color);
    border-radius: 20px;
    cursor: pointer;
    font-size: 13px;
    transition: all 0.2s;
}
.quick-q-btn:hover { background: var(--primary-color); color: white; }

#inputArea {
    display: flex;
    gap: 10px;
    padding: 15px;
    background: var(--card-bg);
    border-radius: 30px;
    box-shadow: var(--shadow);
    align-items: center;
}

#userInput {
    flex: 1;
    padding: 12px 20px;
    border: none;
    outline: none;
    background: transparent;
    color: var(--text-color);
    font-size: 15px;
}

#inputArea button {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    border: none;
    background: var(--primary-color);
    color: white;
    cursor: pointer;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s;
}
#inputArea button:hover { background: var(--primary-dark); }
#mic-btn.listening { background: var(--danger-color); animation: pulse 1.5s infinite; }

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

#voice-status {
    text-align: center;
    font-size: 12px;
    color: var(--danger-color);
    margin-top: 5px;
}
.hidden { display: none !important; }

/* Gallery View */
.view-header {
    padding: 20px;
    background: var(--sidebar-bg);
    border-bottom: 1px solid var(--border-color);
}
.gallery-filters {
    display: flex;
    gap: 10px;
    margin-top: 15px;
    overflow-x: auto;
    padding-bottom: 5px;
}
.filter-btn {
    padding: 8px 16px;
    border: none;
    border-radius: 20px;
    background: var(--secondary-color);
    color: var(--text-color);
    cursor: pointer;
    white-space: nowrap;
}
.filter-btn.active { background: var(--primary-color); color: white; }

.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    padding: 20px;
}
.gallery-item {
    background: var(--card-bg);
    border-radius: 10px;
    overflow: hidden;
    box-shadow: var(--shadow);
    cursor: pointer;
    transition: transform 0.2s;
}
.gallery-item:hover { transform: translateY(-5px); }
.gallery-item img {
    width: 100%;
    height: 180px;
    object-fit: cover;
}
.gallery-info { padding: 12px; }
.gallery-info h4 { margin-bottom: 5px; font-size: 16px; }
.gallery-info p { font-size: 12px; color: gray; }
.gallery-info .category { font-size: 10px; background: var(--secondary-color); padding: 3px 8px; border-radius: 10px; display: inline-block; margin-top: 5px;}

/* Lightbox */
.lightbox {
    position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%;
    background-color: rgba(0,0,0,0.9);
    display: flex; flex-direction: column; justify-content: center; align-items: center;
}
.lightbox-content { max-width: 90%; max-height: 80%; object-fit: contain; }
#lightbox-caption { color: #ccc; padding: 10px 0; font-size: 16px; text-align: center; }
#lightbox-close { position: absolute; top: 15px; right: 35px; color: #f1f1f1; font-size: 40px; font-weight: bold; cursor: pointer; }
#lightbox-prev, #lightbox-next { cursor: pointer; position: absolute; top: 50%; width: auto; padding: 16px; margin-top: -50px; color: white; font-weight: bold; font-size: 20px; transition: 0.6s ease; border-radius: 0 3px 3px 0; user-select: none; background-color: rgba(0,0,0,0.5);}
#lightbox-next { right: 0; border-radius: 3px 0 0 3px; }
#lightbox-prev { left: 0; }

/* Dashboard View */
.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
    padding: 20px;
}
.dash-card {
    background: var(--card-bg);
    border-radius: 12px;
    padding: 20px;
    box-shadow: var(--shadow);
}
.dash-card h3 { color: var(--primary-color); border-bottom: 2px solid var(--secondary-color); padding-bottom: 10px; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;}
.dash-card ul { list-style-position: inside; margin-bottom: 15px; }
.dash-card li { margin-bottom: 8px; font-size: 14px; }
.dash-card p { font-size: 14px; margin-bottom: 10px; line-height: 1.5; }
.btn-primary { display: inline-block; padding: 8px 16px; background: var(--primary-color); color: white; text-decoration: none; border-radius: 5px; font-size: 14px; }
.btn-primary:hover { background: var(--primary-dark); }

/* Mobile Responsive */
.mobile-only { display: none; }
@media (max-width: 768px) {
    .sidebar { position: fixed; height: 100%; transform: translateX(-100%); }
    .sidebar.open { transform: translateX(0); }
    .mobile-only { display: block; background: none; border: none; color: white; font-size: 20px; }
    .message { max-width: 90%; }
}
""",
    'js/app.js': """
document.addEventListener('DOMContentLoaded', () => {
    // Theme toggle
    const themeBtn = document.getElementById('theme-toggle-btn');
    const root = document.documentElement;
    
    // Check saved theme
    if(localStorage.getItem('theme') === 'dark') {
        root.setAttribute('data-theme', 'dark');
        themeBtn.innerHTML = '<i class="fas fa-sun"></i>';
    }

    themeBtn.addEventListener('click', () => {
        if(root.getAttribute('data-theme') === 'dark') {
            root.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            themeBtn.innerHTML = '<i class="fas fa-moon"></i>';
        } else {
            root.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            themeBtn.innerHTML = '<i class="fas fa-sun"></i>';
        }
    });

    // Sidebar Toggle
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggle-sidebar-btn');
    const closeBtn = document.getElementById('close-sidebar-btn');

    toggleBtn.addEventListener('click', () => sidebar.classList.toggle('open'));
    closeBtn.addEventListener('click', () => sidebar.classList.remove('open'));

    // Navigation
    const navBtns = document.querySelectorAll('.nav-btn');
    const views = document.querySelectorAll('.view');

    navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active from all
            navBtns.forEach(b => b.classList.remove('active'));
            views.forEach(v => v.classList.add('hidden'));
            views.forEach(v => v.classList.remove('active'));
            
            // Add active to clicked
            btn.classList.add('active');
            const targetId = btn.getAttribute('data-target');
            const targetView = document.getElementById(targetId);
            targetView.classList.remove('hidden');
            targetView.classList.add('active');
            
            if(window.innerWidth <= 768) sidebar.classList.remove('open');
        });
    });

    // Quick Questions
    document.querySelectorAll('.quick-q-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const input = document.getElementById('userInput');
            input.value = btn.innerText;
            document.getElementById('send-btn').click();
        });
    });
});
""",
    'js/chat.js': """
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
""",
    'js/voice.js': """
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
""",
    'js/history.js': """
const HistoryManager = {
    conversations: [],
    
    init() {
        this.loadFromStorage();
        this.renderList();
        this.setupListeners();
        
        // Load latest or new
        if(this.conversations.length > 0) {
            this.loadConversation(this.conversations[0].id);
        } else {
            this.startNew();
        }
    },

    loadFromStorage() {
        try {
            const data = localStorage.getItem('kesav_history');
            if (data) {
                this.conversations = JSON.parse(data);
            }
        } catch(e) {
            console.error("Failed to load history", e);
            this.conversations = [];
        }
    },

    saveToStorage() {
        localStorage.setItem('kesav_history', JSON.stringify(this.conversations));
    },

    createNewConversation(firstMessage) {
        const id = 'conv_' + Date.now();
        let title = firstMessage.substring(0, 30);
        if(firstMessage.length > 30) title += '...';
        
        const conv = {
            id: id,
            title: title,
            created: new Date().toISOString(),
            messages: []
        };
        
        this.conversations.unshift(conv); // add to top
        this.saveToStorage();
        this.renderList();
        return id;
    },

    addMessage(id, sender, text) {
        const conv = this.conversations.find(c => c.id === id);
        if (conv) {
            conv.messages.push({
                sender,
                text,
                timestamp: new Date().toISOString()
            });
            this.saveToStorage();
        }
    },

    loadConversation(id) {
        const conv = this.conversations.find(c => c.id === id);
        if (conv) {
            currentConversationId = id;
            loadChatToUI(conv.messages);
            this.renderList(); // update active state
        }
    },

    startNew() {
        currentConversationId = null;
        clearChatUI();
        loadChatToUI([]); // loads default welcome message
        this.renderList();
    },

    deleteConversation(id) {
        if(confirm("Are you sure you want to delete this chat?")) {
            this.conversations = this.conversations.filter(c => c.id !== id);
            this.saveToStorage();
            if(currentConversationId === id) {
                this.startNew();
            } else {
                this.renderList();
            }
        }
    },

    clearAll() {
        if(confirm("Are you sure you want to delete ALL chat history?")) {
            this.conversations = [];
            this.saveToStorage();
            this.startNew();
        }
    },

    renderList(filter = '') {
        const list = document.getElementById('conversation-list');
        list.innerHTML = '';
        
        this.conversations.forEach(conv => {
            if(filter && !conv.title.toLowerCase().includes(filter.toLowerCase())) return;

            const li = document.createElement('li');
            li.className = `history-item ${conv.id === currentConversationId ? 'active' : ''}`;
            
            li.innerHTML = `
                <div class="history-title" title="${conv.title}">${conv.title}</div>
                <div class="history-actions">
                    <button class="del-btn" data-id="${conv.id}" title="Delete"><i class="fas fa-trash-alt"></i></button>
                </div>
            `;
            
            // Click title to load
            li.querySelector('.history-title').addEventListener('click', () => {
                this.loadConversation(conv.id);
                if(window.innerWidth <= 768) document.getElementById('sidebar').classList.remove('open');
            });

            // Delete
            li.querySelector('.del-btn').addEventListener('click', (e) => {
                e.stopPropagation();
                this.deleteConversation(conv.id);
            });

            list.appendChild(li);
        });
    },

    setupListeners() {
        document.getElementById('new-chat-btn').addEventListener('click', () => this.startNew());
        document.getElementById('clear-history-btn').addEventListener('click', () => this.clearAll());
        
        document.getElementById('search-history-input').addEventListener('input', (e) => {
            this.renderList(e.target.value);
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    HistoryManager.init();
});
""",
    'js/gallery.js': """
document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('gallery-grid');
    const filterBtns = document.querySelectorAll('.filter-btn');
    
    // Lightbox elements
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const closeBtn = document.getElementById('lightbox-close');
    const prevBtn = document.getElementById('lightbox-prev');
    const nextBtn = document.getElementById('lightbox-next');
    
    let currentImageIndex = 0;
    let filteredImages = [];

    function renderGallery(filter = 'all') {
        grid.innerHTML = '';
        
        filteredImages = filter === 'all' 
            ? GalleryManifest 
            : GalleryManifest.filter(img => img.category === filter);
            
        if(filteredImages.length === 0) {
            grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; color: gray;">No images available for this category yet.</p>';
            return;
        }

        filteredImages.forEach((img, index) => {
            const div = document.createElement('div');
            div.className = 'gallery-item';
            div.innerHTML = `
                <img src="${img.path}" alt="${img.title}" loading="lazy" onerror="this.src='images/adithya_college.png'; this.onerror=null;">
                <div class="gallery-info">
                    <h4>${img.title}</h4>
                    <p>${img.caption}</p>
                    <span class="category">${img.category.toUpperCase()}</span>
                </div>
            `;
            
            div.addEventListener('click', () => openLightbox(index));
            grid.appendChild(div);
        });
    }

    function openLightbox(index) {
        currentImageIndex = index;
        updateLightbox();
        lightbox.classList.remove('hidden');
    }

    function updateLightbox() {
        const img = filteredImages[currentImageIndex];
        lightboxImg.src = img.path;
        lightboxCaption.innerHTML = `<strong>${img.title}</strong><br>${img.caption}`;
    }

    function closeLightbox() {
        lightbox.classList.add('hidden');
    }

    // Listeners
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderGallery(btn.dataset.filter);
        });
    });

    closeBtn.addEventListener('click', closeLightbox);
    
    lightbox.addEventListener('click', (e) => {
        if(e.target === lightbox) closeLightbox();
    });

    prevBtn.addEventListener('click', () => {
        currentImageIndex = (currentImageIndex - 1 + filteredImages.length) % filteredImages.length;
        updateLightbox();
    });

    nextBtn.addEventListener('click', () => {
        currentImageIndex = (currentImageIndex + 1) % filteredImages.length;
        updateLightbox();
    });

    document.addEventListener('keydown', (e) => {
        if (!lightbox.classList.contains('hidden')) {
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft') prevBtn.click();
            if (e.key === 'ArrowRight') nextBtn.click();
        }
    });

    // Initialize
    if(typeof GalleryManifest !== 'undefined') {
        renderGallery();
    }
});
""",
    'js/college-details.js': """
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('dashboard-content');
    
    if (typeof CollegeInfo === 'undefined') return;

    // Render About
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-university"></i> About College</h3>
            <p><strong>${CollegeInfo.about.name}</strong></p>
            <p>${CollegeInfo.about.intro}</p>
            <a href="${CollegeInfo.about.website}" target="_blank" class="btn-primary">Official Website</a>
        </div>
    `;

    // Render Courses
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-book"></i> Courses Offered</h3>
            <p><strong>Undergraduate:</strong></p>
            <ul>${CollegeInfo.courses.ug.map(c => `<li>${c}</li>`).join('')}</ul>
            <p><strong>Postgraduate:</strong></p>
            <ul>${CollegeInfo.courses.pg.map(c => `<li>${c}</li>`).join('')}</ul>
        </div>
    `;

    // Render Admission & Fees
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-file-signature"></i> Admission & Fees</h3>
            <p><strong>Process:</strong> ${CollegeInfo.admission.process}</p>
            <p><strong>Eligibility:</strong> ${CollegeInfo.admission.eligibility}</p>
            <p><strong>Fees:</strong> ${CollegeInfo.admission.fees}</p>
            <p><em>* ${CollegeInfo.admission.note}</em></p>
        </div>
    `;

    // Render Facilities
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-building"></i> Facilities</h3>
            <ul>${CollegeInfo.facilities.map(f => `<li>${f}</li>`).join('')}</ul>
        </div>
    `;

    // Render Contact
    container.innerHTML += `
        <div class="dash-card">
            <h3><i class="fas fa-address-book"></i> Contact & Location</h3>
            <p><i class="fas fa-map-marker-alt"></i> ${CollegeInfo.contact.address}</p>
            <p><i class="fas fa-phone"></i> ${CollegeInfo.contact.phone}</p>
            <p><i class="fas fa-envelope"></i> ${CollegeInfo.contact.email}</p>
            <div style="margin-top: 15px; display: flex; gap: 10px;">
                <a href="${CollegeInfo.contact.mapUrl}" target="_blank" class="btn-primary"><i class="fas fa-map"></i> Open Maps</a>
            </div>
        </div>
    `;
});
""",
    'data/college-info.js': """
const CollegeInfo = {
    about: {
        name: "Adithya College of Arts and Science",
        intro: "Adithya College of Arts and Science (ACAS) is a dynamic institution situated in Kurumbapalayam, Coimbatore. It aims to provide holistic education focusing on outcome-based learning and career readiness.",
        website: "https://adithyacas.edu.in/"
    },
    courses: {
        ug: [
            "B.Sc. Computer Science",
            "B.Sc. Mathematics",
            "B.Sc. Information Technology",
            "B.Sc. Artificial Intelligence & Machine Learning",
            "B.Sc. Psychology",
            "B.Com.",
            "B.Com. (Computer Applications)",
            "B.Com. (Professional Accounting)",
            "B.A. English Literature",
            "B.A. Political Science",
            "BBA"
        ],
        pg: [
            "M.Com",
            "M.Sc Computer Science"
        ]
    },
    admission: {
        process: "Merit-based through online and offline applications.",
        eligibility: "UG: 10+2 passing certificate. PG: Relevant UG Degree.",
        fees: "Approx. ₹35,000/- per year for UG (varies by specific course).",
        note: "Please contact the college administration for the exact latest fee details and scholarship opportunities."
    },
    facilities: [
        "Well-equipped Digital Library",
        "Advanced Computer & Science Laboratories",
        "Separate Hostels for Boys & Girls (Nutritious food, Wi-Fi)",
        "Spacious Cafeteria & Food Court",
        "Transport Fleet covering major routes",
        "Sports Ground (Basketball, Volleyball, Football)",
        "Auditorium & Seminar Halls",
        "Medical First-Aid Room"
    ],
    contact: {
        address: "Kurumbapalayam, Coimbatore, Tamil Nadu 641107",
        phone: "+91 6384363843",
        email: "infoadithyacas@gmail.com",
        mapUrl: "https://maps.app.goo.gl/AJ35E65KCFsMQxYm6"
    }
};
""",
    'data/gallery-manifest.js': """
// Will be dynamically updated or serve as fallback if python script doesn't fetch enough
const GalleryManifest = [
    {
        path: "images/adithya_college.png",
        title: "Main Campus View",
        caption: "A view of the main building of Adithya College of Arts and Science.",
        category: "campus"
    }
];
"""
}

# Ensure directories exist
os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)
os.makedirs('data', exist_ok=True)
os.makedirs('images/gallery', exist_ok=True)

for filepath, content in files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip())
        print(f"Written {filepath}")

