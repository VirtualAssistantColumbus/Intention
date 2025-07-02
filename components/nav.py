from utils.html_ import html

def nav() -> str:
    """
    Renders a minimal sticky bottom navigation bar.
    Only include this on pages where navigation is needed.
    """
    return html("""
        <!-- Sticky Bottom Navigation -->
        <nav class="fixed bottom-0 left-0 right-0 bg-black border-t border-gray-800 z-50">
            <div class="flex justify-center items-center px-8 py-4">
                <div class="flex gap-12">
                    <a href="/" class="text-lg font-medium text-white hover:text-gray-300 transition-colors">
                        Home
                    </a>
                    <a href="/principles" class="text-lg font-medium text-white hover:text-gray-300 transition-colors">
                        Principles
                    </a>
                    <a href="/team" class="text-lg font-medium text-white hover:text-gray-300 transition-colors">
                        About
                    </a>
                </div>
            </div>
        </nav>
        
        <!-- Bottom padding to prevent content from being hidden behind nav -->
        <div class="h-16"></div>
    """) 