const server = 'wss://echo.websocket.org/'

const ws = new WebSocket(server)
var keys = ''

ws.onopen = function(e) {
  console.log('connected')
}
ws.onclose = function(e) {
  console.log(e)
}
ws.onmessage = function(e) {
  if (e.data === 'face detected') {
    document.getElementById('checkOne').classList.add('fas-ready')
  }
  if (e.data === 'authenticated') {
    document.getElementById('loggedIn').classList.add('show')
    document.getElementById('notLoggedIn').classList.add('hide')
  }
}

function sendMessage(message) {
  console.log('trying to send... ' + message)
  ws.send(message)
}

window.onkeypress = function(e) {
  if (e.key === 'Enter') {
    console.log('got otp: ' + keys)
    document.getElementById('checkTwo').classList.add('fas-ready')
    keys = ''
  } else {
    keys = keys + e.key
  }
}
