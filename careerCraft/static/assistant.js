// CareerCraft AI Assistant JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Initialize chat functionality
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const chatLog = document.getElementById('chat-log');
    
    // Focus on input when page loads
    if (chatInput) {
        chatInput.focus();
    }
    
    // Send message function
    function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;
        
        // Add user message to chat
        addMessageToChat('user', message);
        chatInput.value = '';
        
        // Simulate AI thinking
        setTimeout(() => {
            const aiResponse = generateAIResponse(message);
            addMessageToChat('ai', aiResponse);
            scrollToBottom();
        }, 1000);
    }
    
    // Add message to chat
    function addMessageToChat(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const avatar = document.createElement('div');
        avatar.className = 'avatar';
        avatar.textContent = sender === 'ai' ? '🤖' : '🧑';
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = message;
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);
        chatLog.appendChild(messageDiv);
        
        scrollToBottom();
    }
    
    // Scroll to bottom of chat
    function scrollToBottom() {
        chatLog.scrollTop = chatLog.scrollHeight;
    }
    
    // Generate AI response based on user input
    function generateAIResponse(userMessage) {
        const message = userMessage.toLowerCase();
        
        // Career-related responses
        if (message.includes('career') || message.includes('job') || message.includes('work')) {
            return getCareerAdvice(message);
        }
        else if (message.includes('skill') || message.includes('learn') || message.includes('study')) {
            return getSkillsAdvice(message);
        }
        else if (message.includes('resume') || message.includes('cv') || message.includes('application')) {
            return getResumeAdvice();
        }
        else if (message.includes('interview') || message.includes('hire') || message.includes('apply')) {
            return getInterviewAdvice();
        }
        else if (message.includes('mentor') || message.includes('guide') || message.includes('help')) {
            return getMentorAdvice();
        }
        else if (message.includes('hello') || message.includes('hi') || message.includes('hey')) {
            return "Hello! I'm your CareerCraft AI assistant. I can help you with career guidance, skill development, resume building, interview preparation, and connecting with mentors. What would you like to discuss today?";
        }
        else if (message.includes('thank') || message.includes('thanks')) {
            return "You're welcome! I'm here to help you succeed in your career journey. Is there anything else you'd like to know?";
        }
        else {
            return "I'm here to help you with your career development! You can ask me about career paths, skills to learn, resume tips, interview preparation, or finding mentors. What specific area would you like help with?";
        }
    }
    
    // Career advice responses
    function getCareerAdvice(message) {
        const responses = [
            "Based on current market trends, careers in technology, data science, and digital marketing are growing rapidly. What specific field are you interested in?",
            "Choosing a career depends on your interests, skills, and market demand. Have you taken our career assessment quiz to discover your strengths?",
            "Many successful careers start with identifying your passion and then building the necessary skills. What are you passionate about?",
            "Consider careers that align with both your interests and future job market trends. Tech roles like software development, AI/ML, and cybersecurity are particularly promising.",
            "Career transitions are common these days. Many people successfully switch fields by upskilling and networking. What field are you considering?"
        ];
        return responses[Math.floor(Math.random() * responses.length)];
    }
    
    // Skills advice
    function getSkillsAdvice(message) {
        const responses = [
            "Essential skills for today's job market include programming (Python, JavaScript), data analysis, communication, and problem-solving. Which skills are you looking to develop?",
            "Consider learning skills that are in high demand: cloud computing, AI/ML, digital marketing, or UX design. What industry are you targeting?",
            "Soft skills like communication, teamwork, and adaptability are just as important as technical skills. Many employers value these highly.",
            "Online platforms like Coursera, Udemy, and freeCodeCamp offer excellent courses for skill development. I can recommend specific courses based on your career goals.",
            "Building projects is one of the best ways to develop and demonstrate skills. What kind of projects interest you?"
        ];
        return responses[Math.floor(Math.random() * responses.length)];
    }
    
    // Resume advice
    function getResumeAdvice() {
        const responses = [
            "A strong resume should highlight your achievements with metrics, not just responsibilities. Use action verbs and quantify your impact whenever possible.",
            "Tailor your resume for each job application. Focus on skills and experiences that match the job description requirements.",
            "Include relevant keywords from the job description to help your resume get past automated screening systems.",
            "Keep your resume clean and professional-looking. Use consistent formatting and avoid clutter. 1-2 pages is ideal for most professionals.",
            "Consider including a skills section with both technical and soft skills. Many recruiters scan this section first."
        ];
        return responses[Math.floor(Math.random() * responses.length)];
    }
    
    // Interview advice
    function getInterviewAdvice() {
        const responses = [
            "Prepare for interviews by researching the company, practicing common questions, and preparing questions to ask the interviewer.",
            "Use the STAR method (Situation, Task, Action, Result) to structure your answers to behavioral interview questions.",
            "Practice your answers out loud. This helps you sound more natural and confident during the actual interview.",
            "Remember that interviews are a two-way street. You're also evaluating if the company is a good fit for you.",
            "Follow up after interviews with a thank-you email. This shows professionalism and keeps you top of mind."
        ];
        return responses[Math.floor(Math.random() * responses.length)];
    }
    
    // Mentor advice
    function getMentorAdvice() {
        const responses = [
            "Mentors can provide valuable guidance based on their experience. Look for mentors in your desired industry or role.",
            "You can find mentors through professional networks, LinkedIn, or our mentor matching system. What field are you looking for mentorship in?",
            "A good mentor relationship is built on mutual respect and clear communication. Be specific about what guidance you're seeking.",
            "Consider having multiple mentors for different areas: career guidance, technical skills, and industry insights.",
            "Don't be afraid to reach out to potential mentors. Most professionals are happy to help when approached respectfully."
        ];
        return responses[Math.floor(Math.random() * responses.length)];
    }
    
    // New chat function
    window.newChat = function() {
        chatLog.innerHTML = `
            <div class="message ai-message">
                <div class="avatar">🤖</div>
                <div class="message-content">
                    Hello! I'm your CareerCraft AI assistant. I can help you with career guidance, skill development, resume building, interview preparation, and connecting with mentors. What would you like to discuss today?
                </div>
            </div>
        `;
    };
    
    // Send message on button click
    if (sendBtn) {
        sendBtn.addEventListener('click', sendMessage);
    }
    
    // Send message on Enter key
    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
    
    // Call mentor function
    window.callMentor = function() {
        alert('Connecting you with a career mentor... (This would initiate a real call in production)');
    };
});
