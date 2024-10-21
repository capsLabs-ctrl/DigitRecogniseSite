const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const colorPicker = document.getElementById("color-picker");
const gridSizeInput = document.getElementById("grid-size");
const clearButton = document.getElementById("clear");
const scaleSize =  parseInt(getComputedStyle(document.documentElement).getPropertyValue('--max-width').trim(),10);

let brushColor = "#000000";
let drawing = false;
let gridSize = 28;  // Количество квадратов по одной стороне
let cellSize = canvas.width / gridSize;        // Размер одного квадрата

canvas.addEventListener("mousedown", () => drawing = true);
canvas.addEventListener("mouseup", () => {
    drawing = false;
    sendData(getCanvasData(), document.querySelector("#model_choose").value);
});
document.querySelector("#model_choose").addEventListener("change", function(){
    sendData(getCanvasData(), this.value);
})
canvas.addEventListener("mousemove", drawSquare);
clearButton.addEventListener("click", clearCanvas);

function drawSquare(event) {
    if (!drawing) return;

    // Получаем координаты мыши относительно холста
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Вычисляем позицию квадрата
    const squareX = Math.floor(x / cellSize) * cellSize;
    const squareY = Math.floor(y / cellSize) * cellSize;

    // Рисуем квадрат
    ctx.fillStyle = brushColor;
    ctx.fillRect(squareX, squareY, cellSize, cellSize);
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    changeScale(Array(10).fill(0));
}
function getCanvasData() {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Получаем данные о всех пикселях на канве
    const imageData = context.getImageData(0, 0, width, height).data;

    let pixelMatrix = [];

    // Пройти по каждой строке и столбцу матрицы 28x28
    for (let y = 0; y < 28; y++) {
        const row = [];
        for (let x = 0; x < 28; x++) {
            // Индекс пикселя в imageData
            const pixelIndex = (20 * y * width + x * 20) * 4;
            const alpha = imageData[pixelIndex + 3]; // Альфа-канал

            // Если пиксель непрозрачный, преобразуем его в градацию серого
            if (alpha === 255) {
                row.push(1);
            } else {
                row.push(0); // Или используйте другое значение, например, 255 для белого
            }
        }
        // Добавляем строку в матрицу
        pixelMatrix.push(row);
    }

    // Возвращаем конечный результат
    return pixelMatrix;
}
function downloadArray(array, filename) {
    // Преобразуем массив в JSON
    const json = JSON.stringify(array, null, 2);

    // Создаем новый Blob с данными
    const blob = new Blob([json], { type: 'application/json' });

    // Создаем URL для Blob
    const url = URL.createObjectURL(blob);

    // Создаем элемент <a> для скачивания
    const a = document.createElement('a');
    a.href = url;
    a.download = filename; // Имя файла

    // Добавляем элемент в документ
    document.body.appendChild(a);
    a.click(); // Кликаем по элементу, чтобы инициировать скачивание

    // Удаляем элемент из документа
    document.body.removeChild(a);

    // Освобождаем созданный URL
    URL.revokeObjectURL(url);
}
function sendData(array, model) {
    const dataToSend = {
        array: array,
        model: model
    };
    fetch('https://flask-app-qw64.onrender.com/process_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' 
        },  
        body: JSON.stringify(dataToSend)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Ответ от сервера:', data);
        changeScale(data["predictions"]);
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}

function changeScale(predictions){
    for(let i = 0; i<10; i++){
        const scale = document.querySelector(".scale:nth-child(" + (i + 1) + ")");
        scale.style.width = predictions[i] * scaleSize + "px";
        let persent = (predictions[i] * 100).toFixed(1) + "%";
        
        // Создаём новый стиль
        const styleSheet = document.styleSheets[0]; // Берём первое доступное style-правило
        styleSheet.insertRule(`.scale:nth-child(${i + 1})::after { content: "${persent}"; }`, styleSheet.cssRules.length);
    }
}