// Configure these stuff
const server = 'ws://localhost'
const port = 8080

// Open websocket connection
const ws = new WebSocket(`${server}:${port}`)

// Global var for storing keystrokes from yubikey
var keys = ''

// Listen for websocket open event
ws.onopen = function(e) {
  console.log('connected to server')
}

// Listen for websocket close event
ws.onclose = function(e) {
  console.log('server disconnected')
}

// Listen for messages received
ws.onmessage = receiveMessage

// Listen for OTP keys sent
window.onkeypress = receiveOtp

// Listen for a click on the "Detect Face" button
document.getElementById('checkFace').addEventListener('click', function() {
  sendMessage({
    action: 'checkFace',
  })
})

// Handler for incoming websocket messages
function receiveMessage(e) {
  const message = JSON.parse(e.data)
  console.log('Message received:')
  console.log(e)
  if (message.action === 'checkFace') {
    if (message.payload === true) {
      document.getElementById('checkOne').classList.add('fas-ready')
    } else [alert('No face detected.')]
  }
  if (message.action === 'authenticate') {
    if (message.payload === true) {
      document.getElementById('loggedIn').classList.add('show')
      document.getElementById('notLoggedIn').classList.add('hide')
    } else {
      alert('Yubikey authentication failed.')
    }
  }
}

// Send websocket message
function sendMessage(m) {
  const message = JSON.stringify(m)
  console.log('Sending...' + message)
  ws.send(message)
}

// Handler for receiving keyboard input
function receiveOtp(e) {
  if (e.key === 'Enter') {
    console.log('got otp: ' + keys)
    sendMessage({
      action: 'authenticate',
      payload: keys,
    })
    keys = ''
  } else {
    keys = keys + e.key
  }
}
