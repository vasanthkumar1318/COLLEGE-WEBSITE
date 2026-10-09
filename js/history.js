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