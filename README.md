# Dev Week Face Key Demo

## TODO

1. Create python server that opens a websocket and listens and responds to messages as described below.
2. Update app/facekey.js with correct server ip and port

## Web app

The web app seems to run fine without a web server (i.e. just open the file in Chrome). If you have node installed you can run a simple web server by doing this:

1. `npm install` or `yarn` (if you have it)
2. `npm run start` or `yarn start`

## Websocket communications

Here is the flow for the websocket communications:

- Start server listening for websocket connections
- Load client web page in browser, websocket connection is opened
- Click "Detect Face" button and it sends to server:

`{ "action": "checkFace" }`

- Server takes photo checks for a face and returns either:

`{ "action": "checkFace", "payload": true }` if there is a face or

`{ "action": "checkFace", "payload": false }` is there is no face

- If true, checkmark goes green, if false an alert pops
- Insert Yubikey and touch contact, client sends:

`{ "action": "authenticate", "payload": "[YUBIKEY OTP VALUE HERE]" }`

- Server validates key and sends either:

`{ "action": "authenticate", "payload": true }` if key passes

`{ "action": "authenticate", "payload": false}` if key fails

- If key passes "You're in" message, or alert warning.

## Notes

- Before touching the Yubikey to send the OTP code, make sure you click somewhere in the browser window to make sure it has focus. Otherwise the OTP code will get sent to whatever has the focus.
- You can simulate a bad Yubikey by simply typing a few characters and pressing <ENTER>.
