let inputBox = document.querySelector("#inputBox");
let submitBtn = document.querySelector("#save-data");
let statusBox = document.querySelector("#status");
let saveStatus = document.querySelector("#save-status");
let deleteDataBox = document.querySelector("#deleteData");
let deleteData = document.querySelector("#delete-data");
let statusText = document.getElementById("statusText");


const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.continuous = false;
recognition.lang = 'en-US';

recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript.toLowerCase();
    statusText.innerText = `Heard : "${transcript}"`;
    changeImgVid(0);
    if (transcript.startsWith("naya task") || transcript.startsWith("new task")) {
        const texText = transcript.replace("new task", "").trim();
        if (texText) {
            inputBox.value = texText;
            setTimeout(() => { submitBtn.click(); }, 3000);
        }
    }
    else if (transcript.startsWith("delete task")) {
        const num = parseInt(transcript.split(" ")[2]);
        if (!isNaN(num)) {
            deleteDataBox.value = num;
            setTimeout(() => { deleteData.click(); }, 2000);
        }
    }
    else if (transcript.startsWith("mark task")) {
        const num = parseInt(transcript.split(" ")[2]);
        if (!isNaN(num)) {
            console.log(num);
            statusBox.value = num;
            setTimeout(() => { saveStatus.click(); }, 2000);
        }
    }
}

function startVoice() {
    statusText.innerText = "Listeing.... ";
    recognition.start();
}

document.getElementById("startBtn").addEventListener("click", () => {
    changeImgVid(1);
    startVoice();
});

function changeImgVid(num) {
    if (num) {
        document.querySelector("#img").style.display = 'none';
        document.querySelector("#vid").style.display = 'block';
        setTimeout(() => { changeImgVid(0); }, 15000);
    }
    else {
        document.querySelector("#vid").style.display = 'none';
        document.querySelector("#img").style.display = 'block';
    }
}
