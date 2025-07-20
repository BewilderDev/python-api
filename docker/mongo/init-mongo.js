// This script initializes the MongoDB database with a root user and a specific user for the ChatBot database.
db = db.getSiblingDB('admin');
db.createUser({
    user: 'root',
    pwd: 'root',
    roles: [
        { role: 'userAdminAnyDatabase', db: 'admin' },
        { role: 'readWriteAnyDatabase', db: 'admin' },
        { role: 'dbAdminAnyDatabase', db: 'admin' }
    ]
});

db.auth('root', 'root');

// Switch to ChatBot database
db = db.getSiblingDB('ChatBot');
db.chatbot.createIndex(
    { "question": 1 },
    {
        collation: { locale: "en", strength: 2 },
        background: true
    }
);

// Create specific user for ChatBot database if needed
db.createUser({
    user: 'chatbot_user',
    pwd: 'root',
    roles: [
        {
            role: 'readWrite',
            db: 'ChatBot'
        }
    ]
});
