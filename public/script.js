document.getElementById('instabot-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData();
    const fileField = document.querySelector('input[type="file"]');

    formData.append('photo', fileField.files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const message = document.getElementById('message');
            message.classList.remove('hidden');
            setTimeout(() => {
                message.classList.add('hidden');
            }, 2000);
        } else {
            alert('Failed to post the image.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while posting the image.');
    }
});