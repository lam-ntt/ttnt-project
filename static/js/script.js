var canvas = document.getElementById('canvas');

var ctx = canvas.getContext('2d');
ctx.strokeStyle = 'white'
ctx.lineWidth = 30

var isDrawing = false;

var curImage = '';

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

canvas.addEventListener('mouseup', function() {
  isDrawing = false;

  ctx.fillStyle = 'black';
  curImage = canvas.toDataURL( 'image/png')  

  fetch('/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ image: curImage }),
  })
  .then(response => {
    if (response.ok) {
      console.log('Ảnh đã được lưu trữ trên máy chủ');
    } else {
      console.error('Có lỗi xảy ra khi lưu ảnh');
    }
  })
  .catch(error => {
    console.error('Có lỗi xảy ra khi gửi yêu cầu lưu ảnh:', error);
  });

});