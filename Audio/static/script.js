
// // static/script.js
// document.addEventListener('DOMContentLoaded', () => {
//     const audioElement = document.querySelector('audio');
//     audioElement.src = '/'; // Set the root route as the audio source
// });

// function playAudio() {
//     const audioElement = document.querySelector('audio');
//     audioElement.play();
// }

document.addEventListener('DOMContentLoaded', () => {
    const audioElement = document.querySelector('audio');
    audioElement.src = '/'; // Set the root route as the audio source
    audioElement.onplay = () => console.log("Audio started playing.");
    audioElement.onerror = (e) => console.log("Error playing audio:", e);
});

function playAudio() {
    const audioElement = document.querySelector('audio');
    const promise = audioElement.play();
    
    if (promise !== undefined) {
        promise.then(_ => {
            console.log("Playback started successfully");
        }).catch(error => {
            console.error("Playback failed:", error);
        });
    }
}


