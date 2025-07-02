from utils.html_ import html
from static.static_dir import StaticDir

def social_proof() -> str:
    """
    Renders a horizontal scrolling social proof section with all sign images.
    """
    
    # Get all the sign image paths
    sign_images = [
        StaticDir.SIGN_1, StaticDir.SIGN_2, StaticDir.SIGN_3, StaticDir.SIGN_4,
        StaticDir.SIGN_5, StaticDir.SIGN_6, StaticDir.SIGN_7, StaticDir.SIGN_8,
        StaticDir.SIGN_9, StaticDir.SIGN_10, StaticDir.SIGN_11, StaticDir.SIGN_12
    ]
    
    # Generate the image elements
    image_elements = ""
    for i, sign_image in enumerate(sign_images, 1):
        image_elements += f"""
            <div class="flex-shrink-0">
                <img 
                    src="{sign_image.full_path()}" 
                    alt="Social proof sign {i}"
                    class="h-64 md:h-80 w-auto object-contain transition-all duration-300 rounded-lg"
                >
            </div>
        """
    
    return html(f"""
        <!-- Horizontal Scrolling Container -->
        <div class="relative" id="social-proof-container">
            <!-- Fade effect on edges -->
            <div class="absolute left-0 top-0 bottom-0 w-16 bg-gradient-to-r from-black to-transparent z-10 pointer-events-none"></div>
            <div class="absolute right-0 top-0 bottom-0 w-16 bg-gradient-to-l from-black to-transparent z-10 pointer-events-none"></div>
            
            <!-- Left scroll arrow (hidden on mobile) -->
            <button 
                id="scroll-left"
                class="absolute left-4 top-1/2 transform -translate-y-1/2 z-20 bg-black bg-opacity-80 hover:bg-opacity-90 text-white rounded-full p-3 transition-all duration-300 border-2 border-white border-opacity-30 hover:border-opacity-50 shadow-lg hidden md:flex items-center justify-center"
                onclick="scrollSocialProof('left')"
            >
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path>
                </svg>
            </button>
            
            <!-- Right scroll arrow (hidden on mobile) -->
            <button 
                id="scroll-right"
                class="absolute right-4 top-1/2 transform -translate-y-1/2 z-20 bg-black bg-opacity-80 hover:bg-opacity-90 text-white rounded-full p-3 transition-all duration-300 border-2 border-white border-opacity-30 hover:border-opacity-50 shadow-lg hidden md:flex items-center justify-center"
                onclick="scrollSocialProof('right')"
            >
                <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path>
                </svg>
            </button>
            
            <!-- Scrollable container -->
            <div id="social-proof-scroll" class="flex gap-8 overflow-x-auto scrollbar-hide pb-4" style="scroll-behavior: smooth;">
                {image_elements}
            </div>
        </div>
        
        <!-- Scroll indicator -->
        <div class="flex justify-center mt-8">
            <div class="relative w-48 h-1 bg-gray-800 rounded-full">
                <div id="scroll-thumb" class="absolute top-0 h-full bg-white rounded-full transition-all duration-300" style="width: 20%; left: 0%"></div>
            </div>
        </div>
    
        <style>
            /* Hide scrollbar but keep functionality */
            .scrollbar-hide {{
                -ms-overflow-style: none;  /* Internet Explorer 10+ */
                scrollbar-width: none;  /* Firefox */
            }}
            .scrollbar-hide::-webkit-scrollbar {{
                display: none;  /* Safari and Chrome */
            }}
        </style>
        
        <script>
            function scrollSocialProof(direction) {{
                const container = document.getElementById('social-proof-scroll');
                const scrollAmount = 320; // Approximate width of one image + gap
                
                if (direction === 'left') {{
                    container.scrollBy({{ left: -scrollAmount, behavior: 'smooth' }});
                }} else {{
                    container.scrollBy({{ left: scrollAmount, behavior: 'smooth' }});
                }}
                
                // Update arrow visibility after scroll
                setTimeout(() => updateArrowVisibility(), 100);
            }}
            
            function updateArrowVisibility() {{
                const container = document.getElementById('social-proof-scroll');
                const leftArrow = document.getElementById('scroll-left');
                const rightArrow = document.getElementById('scroll-right');

                
                if (!container) return;
                
                const isAtStart = container.scrollLeft <= 10;
                const isAtEnd = container.scrollLeft >= (container.scrollWidth - container.clientWidth - 10);
                
                // Update arrows
                if (leftArrow && rightArrow) {{
                    leftArrow.style.opacity = isAtStart ? '0.3' : '1';
                    rightArrow.style.opacity = isAtEnd ? '0.3' : '1';
                    leftArrow.style.pointerEvents = isAtStart ? 'none' : 'auto';
                    rightArrow.style.pointerEvents = isAtEnd ? 'none' : 'auto';
                }}
                
                // Update scroll thumb
                const scrollThumb = document.getElementById('scroll-thumb');
                if (scrollThumb) {{
                    const containerWidth = container.clientWidth;
                    const contentWidth = container.scrollWidth;
                    const currentScroll = container.scrollLeft;
                    
                    // Calculate thumb width (represents visible portion)
                    const thumbWidthPercent = Math.max((containerWidth / contentWidth) * 100, 15); // Min 15% width
                    
                    // Calculate thumb position
                    const maxScroll = contentWidth - containerWidth;
                    const maxThumbPosition = 100 - thumbWidthPercent;
                    const thumbPositionPercent = maxScroll > 0 ? (currentScroll / maxScroll) * maxThumbPosition : 0;
                    
                    scrollThumb.style.width = thumbWidthPercent + '%';
                    scrollThumb.style.left = thumbPositionPercent + '%';
                }}
            }}
            
            // Initialize arrow visibility on load
            document.addEventListener('DOMContentLoaded', function() {{
                updateArrowVisibility();
                
                // Update arrow visibility on scroll
                const container = document.getElementById('social-proof-scroll');
                if (container) {{
                    container.addEventListener('scroll', updateArrowVisibility);
                }}
            }});
        </script>
    """)
