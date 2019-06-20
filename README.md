# Dev Week Face Key Demo

## TODO

1. Create python server that opens a websocket and listens and responds to messages as described below. This looks like the way to go: https://websockets.readthedocs.io/en/stable/intro.html
1. Authenticate Yubikey OTP using the demo server (see below)
1. Update app/facekey.js with correct server ip and port

## Web app

The web app seems to run fine without a web server (i.e. just open the file in Chrome). If you have node installed you can run a simple web server by doing this:

1. `npm install` or `yarn` (if you have it)
2. `npm run start` or `yarn start`

The web app is currently set to connect to a server that just echoes back what is sent. This makes it easy to test by sending fake messages in the chrome console that are echoed back as if they came from the server. So, to emulate a successful completed last step, you could open the chrome console and do this:

`> ws.send(JSON.stringify({action: 'authenticate', payload: true}))`

## Websocket communications

Here is the flow for the websocket communications:

- Start server listening for websocket connections
- Load client web page in browser, websocket connection is opened
- Click "Detect Face" button and it sends to server:

`{ "action": "checkFace" }`

- Server takes photo checks for a face and returns either:

`{ "action": "checkFace", "payload": true }` if there is a face or

`{ "action": "checkFace", "payload": false }` if there is no face

- If true, checkmark goes green, if false an alert pops
- Insert Yubikey and touch contact, client sends:

`{ "action": "authenticate", "payload": "[YUBIKEY OTP VALUE HERE]" }`

- Server validates key and sends either:

`{ "action": "authenticate", "payload": true }` if key passes

`{ "action": "authenticate", "payload": false}` if key fails

- If key passes "You're in" message, or alert warning.

## Yubikey demo server

You should be able to test for a valid key by hitting Yubico's validation server. To do that do a HTTP post to `https://demo.yubico.com/api/v1/simple/otp/validate` with a json payload like this:

`{ "key": "[YUBIKEY OTP CODE HERE]"}`

You should get back something like this if successful:

```
{
  "data": {
    "nonce": "waLwXR3mNuSxddCqU8cXx3WAZ",
    "otp": "cccccckucunjubduciiurunbcdjtkdgvnlbcjifghfld",
    "sl": "25",
    "status": "OK",
    "t": "2019-06-20T01:34:36Z0062"
  },
  "status": "success"
}
```

or, like this if it fails:

```
{
  "data": {
    "reason": "NO_VALID_ANSWERS"
  },
  "message": "NO_VALID_ANSWERS",
  "status": "error"
}
```

## Notes

- Before touching the Yubikey to send the OTP code, make sure you click somewhere in the browser window to make sure it has focus. Otherwise the OTP code will get sent to whatever has the focus. The event listener is connected to "window" so anything in the window can have the focus.
- You can simulate a bad Yubikey by simply typing a few characters and pressing <ENTER>.
