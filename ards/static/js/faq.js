document.addEventListener('DOMContentLoaded', function () {
    const accordionTargets = document.querySelectorAll('[data-accordion-target]');

    accordionTargets.forEach(target => {
        target.addEventListener('click', function () {
            const content = document.querySelector(this.getAttribute('data-accordion-target'));

            if (content.style.display === 'none' || content.style.display === '') {
                content.style.display = 'block';
                this.setAttribute('aria-expanded', 'true');
            } else {
                content.style.display = 'none';
                this.setAttribute('aria-expanded', 'false');
            }
        });
    });
});
