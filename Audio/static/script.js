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
    
    // Set the src attribute of the audio element to the processed audio URL
    audioSource.src = processed_audio_url;

    // Play the audio automatically
    audioSource.play();
});
