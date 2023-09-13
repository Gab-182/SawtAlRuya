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
    const audioElement = document.querySelector('audio');
    audioElement.src = '/'; // Set the root route as the audio source
});

function playAudio() {
    const audioElement = document.querySelector('audio');
    audioElement.play();
}
