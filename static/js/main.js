
// Readmore function in Home // 
        function toggleText() {
            const moreText = document.getElementById("moreText");
            const seeMore = document.getElementById("seeMore");

            if (moreText && seeMore) {
                if (moreText.style.display === "none") {
                    moreText.style.display = "inline";
                    seeMore.textContent = "See less";
                } else {
                    moreText.style.display = "none";
                    seeMore.textContent = "See more";
                }
            }
}
// end-Readmore function in Home // 


// Toggle mobile menu visibility
            document.addEventListener('DOMContentLoaded', () => {
                const mobileMenuButton = document.getElementById('mobile-menu-button');
                const mobileMenu = document.getElementById('mobile-menu');

                if (mobileMenuButton && mobileMenu) {
                    mobileMenuButton.addEventListener('click', () => {
                        mobileMenu.classList.toggle('hidden');
                    });
                }
            });

            function closeMobileMenu() {
                const mobileMenu = document.getElementById('mobile-menu');
                if (mobileMenu) {
                    mobileMenu.classList.add('hidden');
                }
            }

            function showSection(section) {
                const homeSection = document.getElementById('home-section');
                const aboutSection = document.getElementById('about-section');
                const contactSection = document.getElementById('contact-section');

                if (homeSection && aboutSection && contactSection) {
                    homeSection.classList.add('hidden');
                    aboutSection.classList.add('hidden');
                    contactSection.classList.add('hidden');

                    if (section === 'home') {
                        homeSection.classList.remove('hidden');
                    } else if (section === 'about') {
                        aboutSection.classList.remove('hidden');
                    } else if (section === 'contact') {
                        contactSection.classList.remove('hidden');
                    }
                }

                // Toggle active class on links
                const link = document.getElementById(`${section}-link`);
                if (link) {
                    document.getElementById('home-link').classList.remove('active');
                    document.getElementById('about-link').classList.remove('active');
                    document.getElementById('contact-link').classList.remove('active');
                    link.classList.add('active');
                }

                closeMobileMenu();
            }


// end- Toggle mobile menu visibility







document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggle-button');
    if (toggleButton) {
        toggleButton.addEventListener('click', function () {
            const sidebar = document.getElementById('sidebar');
            if (sidebar) {
                sidebar.classList.toggle('collapsed');

                const icon = this.querySelector('svg');
                if (icon) {
                    icon.classList.toggle('rotate-90');
                }
            }
        });
    }
});

// Initialize sentiment pie chart
document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('sentimentPieChart');
    if (ctx) {
        new Chart(ctx.getContext('2d'), {
            type: 'pie',
            data: {
                labels: ['Positive', 'Neutral', 'Negative'],
                datasets: [{
                    data: [30, 50, 20],
                    backgroundColor: ['#38a169', '#a0aec0', '#e53e3e'],
                    hoverOffset: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    }
                }
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const notificationToggle = document.getElementById('notification-toggle');
    const profileMenuToggle = document.getElementById('profile-menu-toggle');

    if (notificationToggle) {
        notificationToggle.addEventListener('change', function () {
            document.body.style.overflow = this.checked ? 'hidden' : 'auto';
        });
    }

    if (profileMenuToggle) {
        profileMenuToggle.addEventListener('change', function () {
            document.body.style.overflow = this.checked ? 'hidden' : 'auto';
        });
    }
});

// Mobile View for sidebar display 

document.getElementById('mobile-menu-button').addEventListener('click', function() {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('show');
});


//mobile exit in headers
function toggleMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    mobileMenu.classList.toggle('hidden');
  }
