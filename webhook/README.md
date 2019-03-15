# Python Webhook Demo

This is a simple demo to show how webhooks work with [RingCentral](https://developers.ringcentral.com).

## 1) Run Server

Run the `server.py` program to listen on `localhost:8080`.

```
$ python3 server.py
```

Run ngrok to have a public URL tunnel to `localhost:8080`

```
$ ngrok http 8080
```

## 2) Create The Subscription

Create a `.env` file with your credentials.

Edit the webhook url to be your ngrok URL, e.g. `https://12345.ngrok.io/webhook`

Run the script:

```
$ python3 create.py
```

## 3) Test the Webhook

Make a phone call to the number you authorized.

You should see the server log the event to the console.