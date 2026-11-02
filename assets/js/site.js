(() => {
    function track(name) {
        if (name && window.goatcounter?.count) {
            window.goatcounter.count({ path: `event/${name}`, title: name, event: true });
        }
    }

    document.querySelectorAll('[data-goat-event]').forEach(link => {
        link.addEventListener('click', () => track(link.dataset.goatEvent));
    });

    // Let listmonk display its actual result. Cross-origin no-cors requests
    // cannot distinguish a successful subscription from a rejected one.
    document.querySelectorAll('[data-subscribe-form]').forEach(form => {
        form.addEventListener('submit', () => track('subscribe-attempt'));
    });

    document.querySelectorAll('[data-share-url]').forEach(button => {
        let resetTimer;
        const label = button.textContent;

        async function copy(url) {
            try {
                await navigator.clipboard.writeText(url);
                button.textContent = 'COPIED';
                clearTimeout(resetTimer);
                resetTimer = setTimeout(() => { button.textContent = label; }, 1600);
            } catch {
                window.prompt('Copy this link:', url);
            }
        }

        button.addEventListener('click', async () => {
            const url = button.dataset.shareUrl;
            const title = button.dataset.shareTitle || document.title;

            if (navigator.share) {
                try {
                    await navigator.share({ title, url });
                } catch (error) {
                    if (error.name !== 'AbortError') await copy(url);
                }
            } else {
                await copy(url);
            }
        });
    });
})();
