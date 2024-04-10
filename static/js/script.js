let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');
ctx.strokeStyle = 'white'
ctx.lineWidth = 30

let isDrawing = false;
let curImage = '';

canvas.addEventListener('mousedown', function(e) {
  isDrawing = true;
  ctx.beginPath();
  ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
});

canvas.addEventListener('mousemove', function(e) {
  if(isDrawing) {
    ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    ctx.stroke();
  }
});

let result = document.getElementById('result')
let img = document.querySelector('img')

canvas.addEventListener('mouseup', function() {
  isDrawing = false;

  curImage = canvas.toDataURL( 'image/png')  

  fetch('/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ image: curImage }),
  })
  .then(response => response.json())
  .then(data => {
    result.innerText = `${result.innerText} ${data.result}`
    img.src = '../static/img/input-converted.png' + '/?foo=' + new Date().getTime() // add datetime to prevent cache issue
})

});

let clearBtn = document.getElementById('clear');

clearBtn.addEventListener('click', () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  result.innerText = 'Number predicted:'
  img.src = '../static/img/th.jpg'
});
