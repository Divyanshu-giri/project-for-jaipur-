// Dashboard Interactive Features
document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations and interactive elements
    initDashboardFeatures();
    initProgressTracking();
    initJobRecommendations();
    initLearningResources();
});

function initDashboardFeatures() {
    // Add hover effects to cards
    const cards = document.querySelectorAll('.dashboard-card, .job-card, .course-card, .action-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-5px)';
            card.style.boxShadow = '0 10px 30px rgba(30, 144, 255, 0.3)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
            card.style.boxShadow = '0 4px 20px rgba(30, 144, 255, 0.2)';
        });
    });

    // Add click animations to buttons
    const buttons = document.querySelectorAll('button, .btn, .btn-small');
    buttons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
}

function initProgressTracking() {
    // Simulate progress animation
    const progressScore = document.querySelector('.progress-score');
    if (progressScore) {
        let currentXP = parseInt(progressScore.textContent);
        let targetXP = currentXP;
        let animationSpeed = 50;
        
        // Animate XP counter
        const animateXP = () => {
            if (currentXP < targetXP) {
                currentXP += Math.ceil((targetXP - currentXP) / 10);
                progressScore.textContent = currentXP + ' XP';
                setTimeout(animateXP, animationSpeed);
            }
        };
        
        // Start animation after a short delay
        setTimeout(animateXP, 1000);
    }
}

function initJobRecommendations() {
    // Add job application functionality
    const applyButtons = document.querySelectorAll('.job-card .btn-small');
    applyButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const jobTitle = this.closest('.job-card').querySelector('h4').textContent;
            showApplicationModal(jobTitle);
        });
    });
}

function initLearningResources() {
    // Track course progress
    const courseCards = document.querySelectorAll('.course-card');
    courseCards.forEach(card => {
        card.addEventListener('click', function() {
            const courseTitle = this.querySelector('h4').textContent;
            trackCourseProgress(courseTitle);
        });
    });
}

function showApplicationModal(jobTitle) {
    // Create application modal
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal-content">
            <h3>Apply for: ${jobTitle}</h3>
            <p>This feature is coming soon! In the meantime, you can:</p>
            <ul>
                <li>📝 Review your resume</li>
                <li>🎯 Practice interview questions</li>
                <li>🤝 Connect with mentors</li>
            </ul>
            <div class="modal-actions">
                <button class="btn-small" onclick="closeModal()">Got it!</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.querySelector('.modal-overlay');
    if (modal) {
        modal.remove();
        document.body.style.overflow = 'auto';
    }
}

function trackCourseProgress(courseTitle) {
    // Simulate course progress tracking
    console.log(`Course started: ${courseTitle}`);
    // In a real app, this would send data to a backend
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Escape key closes modals
    if (e.key === 'Escape') {
        closeModal();
    }
    
    // Ctrl/Cmd + / shows keyboard shortcuts
    if ((e.ctrlKey || e.metaKey) && e.key === '/') {
        e.preventDefault();
        showKeyboardShortcuts();
    }
});

function showKeyboardShortcuts() {
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal-content">
            <h3>🎮 Keyboard Shortcuts</h3>
            <div class="shortcuts-list">
                <div class="shortcut-item">
                    <span class="key">Esc</span>
                    <span class="description">Close modal</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Ctrl/Cmd + /</span>
                    <span class="description">Show shortcuts</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Ctrl/Cmd + S</span>
                    <span class="description">Save progress</span>
                </div>
            </div>
            <div class="modal-actions">
                <button class="btn-small" onclick="closeModal()">Close</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';
}

// Local storage for user preferences
function saveUserPreferences(preferences) {
    localStorage.setItem('careerCraft_preferences', JSON.stringify(preferences));
}

function loadUserPreferences() {
    const preferences = localStorage.getItem('careerCraft_preferences');
    return preferences ? JSON.parse(preferences) : {};
}

// Theme management
function initTheme() {
    const preferences = loadUserPreferences();
    if (preferences.theme === 'dark') {
        document.body.classList.add('dark-theme');
    }
}

// Responsive design helpers
function checkMobileView() {
    return window.innerWidth <= 768;
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add CSS for modals
const style = document.createElement('style');
style.textContent = `
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    backdrop-filter: blur(5px);
}

.modal-content {
    background: #222;
    padding: 2rem;
    border-radius: 12px;
    border: 2px solid #00ff99;
    max-width: 500px;
    width: 90%;
    max-height: 80vh;
    overflow-y: auto;
}

.modal-content h3 {
    color: #ff9800;
    margin-bottom: 1rem;
}

.modal-actions {
    margin-top: 1.5rem;
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
}

.shortcuts-list {
    margin: 1rem 0;
}

.shortcut-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem;
    border-bottom: 1px solid #333;
}

.shortcut-item:last-child {
    border-bottom: none;
}

.key {
    background: #00ff99;
    color: #181818;
    padding: 0.3rem 0.8rem;
    border-radius: 4px;
    font-weight: bold;
    font-size: 0.9rem;
}

.description {
    color: #e0e0e0;
}
`;
document.head.appendChild(style);

// Initialize theme when page loads
initTheme();

// Additional interactive functions
function quickTour() {
    showModal(`
        <h3>🚀 Welcome to CareerCraft!</h3>
        <p>Here's a quick tour of your dashboard:</p>
        <ol>
            <li><strong>Progress Tracking</strong> - Monitor your career development journey</li>
            <li><strong>Job Recommendations</strong> - Find opportunities matching your skills</li>
            <li><strong>Learning Resources</strong> - Access curated courses and tutorials</li>
            <li><strong>Quick Actions</strong> - Fast access to key features</li>
        </ol>
        <p>Start exploring and building your career path!</p>
    `);
}

function showTips() {
    showModal(`
        <h3>💡 Career Success Tips</h3>
        <ul>
            <li>🎯 Set clear career goals and track your progress</li>
            <li>📚 Continuously learn new skills relevant to your field</li>
            <li>🤝 Network with mentors and professionals in your industry</li>
            <li>💼 Tailor your resume for each job application</li>
            <li>🎤 Practice interviews regularly to build confidence</li>
        </ul>
        <p>Remember: Consistency is key to career growth!</p>
    `);
}

function showModal(content) {
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal-content">
            ${content}
            <div class="modal-actions">
                <button class="btn-small" onclick="closeModal()">Got it!</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';
}

// Close modal when clicking outside
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('modal-overlay')) {
        closeModal();
    }
});

// Add CSS for welcome actions
const welcomeStyle = document.createElement('style');
welcomeStyle.textContent = `
.welcome-actions {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
    flex-wrap: wrap;
}

.course-card {
    cursor: pointer;
    transition: all 0.3s ease;
}

.course-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 25px rgba(0, 255, 153, 0.3);
}
`;
document.head.appendChild(welcomeStyle);
