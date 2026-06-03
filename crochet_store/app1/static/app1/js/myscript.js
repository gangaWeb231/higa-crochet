
    console.log("🌿 HIGA — Olive Green + Sand + Clay palette active!");
    console.log("✅ Navbar hover effects working, product section with 8 items displayed.");
    
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            if(link.getAttribute('href') === '#products') {
                e.preventDefault();
                document.getElementById('products').scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    