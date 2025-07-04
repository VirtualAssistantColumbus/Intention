from utils.html_ import html

def nav() -> str:
    """
    Renders a responsive sticky bottom navigation bar.
    Shows full nav on larger screens, hamburger menu on smaller screens.
    Only include this on pages where navigation is needed.
    """
    return html("""
        <!-- Sticky Bottom Navigation -->
        <nav class="fixed bottom-0 left-0 right-0 bg-black border-t border-gray-800 z-50">
            <!-- Full Navigation (visible on md+ screens) -->
            <div class="hidden md:flex justify-start items-center px-8 py-4 md:px-16 lg:px-24">
                <div class="flex gap-12">
                    <a href="/" class="text-lg font-medium text-white hover:text-gray-300 transition-colors">
                        Home
                    </a>
                    <a href="/principles" class="text-lg font-medium text-white hover:text-gray-300 transition-colors">
                        Principles
                    </a>
                    <a href="/more-less" class="text-lg font-medium text-white hover:text-gray-300 transition-colors">
                        More/Less
                    </a>
                    <a href="/team" class="text-lg font-medium text-white hover:text-gray-300 transition-colors">
                        About
                    </a>
                </div>
            </div>
            
            <!-- Hamburger Menu (visible on small screens) -->
            <div class="md:hidden">
                <!-- Hamburger Button -->
                <div class="flex justify-center items-center px-8 py-4">
                    <button id="mobile-menu-toggle" class="text-white hover:text-gray-300 transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
                
                <!-- Mobile Menu Overlay -->
                <div id="mobile-menu" class="absolute bottom-full left-0 right-0 bg-black border-t border-gray-800 transform translate-y-full opacity-0 transition-all duration-300 ease-in-out pointer-events-none">
                    <div class="flex flex-col">
                        <a href="/" class="text-lg font-medium text-white hover:text-gray-300 transition-colors py-3 px-8 border-b border-gray-800">
                            Home
                        </a>
                        <a href="/principles" class="text-lg font-medium text-white hover:text-gray-300 transition-colors py-3 px-8 border-b border-gray-800">
                            Principles
                        </a>
                        <a href="/more-less" class="text-lg font-medium text-white hover:text-gray-300 transition-colors py-3 px-8 border-b border-gray-800">
                            More/Less
                        </a>
                        <a href="/team" class="text-lg font-medium text-white hover:text-gray-300 transition-colors py-3 px-8">
                            About
                        </a>
                    </div>
                </div>
            </div>
        </nav>
        
        <!-- Bottom padding to prevent content from being hidden behind nav -->
        <div class="h-16"></div>
        
        <!-- JavaScript for mobile menu toggle -->
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const toggle = document.getElementById('mobile-menu-toggle');
                const menu = document.getElementById('mobile-menu');
                let isOpen = false;
                
                if (toggle && menu) {
                    toggle.addEventListener('click', function() {
                        isOpen = !isOpen;
                        
                        if (isOpen) {
                            menu.classList.remove('translate-y-full', 'opacity-0', 'pointer-events-none');
                            menu.classList.add('translate-y-0', 'opacity-100', 'pointer-events-auto');
                        } else {
                            menu.classList.remove('translate-y-0', 'opacity-100', 'pointer-events-auto');
                            menu.classList.add('translate-y-full', 'opacity-0', 'pointer-events-none');
                        }
                    });
                    
                    // Close menu when clicking on a link
                    const menuLinks = menu.querySelectorAll('a');
                    menuLinks.forEach(link => {
                        link.addEventListener('click', function() {
                            isOpen = false;
                            menu.classList.remove('translate-y-0', 'opacity-100', 'pointer-events-auto');
                            menu.classList.add('translate-y-full', 'opacity-0', 'pointer-events-none');
                        });
                    });
                }
            });
        </script>
    """) 