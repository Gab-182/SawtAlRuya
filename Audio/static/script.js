// // static/script.js
// document.addEventListener('DOMContentLoaded', () => {
//     // Automatically trigger file upload when the page loads
//     autoUploadAndPlay();
    
//     function autoUploadAndPlay() {
//         fetch('/get_processed_audio')
//             .then(response => response.json())
//             .then(data => {
//                 if (data.success) {
//                     let audio = new Audio(data.audio_url);
//                     audio.play();
//                 }
//             })
//             .catch((error) => {
//                 console.error('Error:', error);
//             });
//     }
// });

// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const audioSource = document.getElementById('audioSource');
    
    fetch('/')
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                audioSource.src = data.audio_url;
                audioSource.play(); // Play only if the audio file exists
            } else {
                console.error(data.error);
                // Handle the case where the audio file doesn't exist
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});
