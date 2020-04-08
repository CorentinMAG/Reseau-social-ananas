class WebSocketService {

	static instance = null;
	callbacks = {};

	static getInstance() {
		if (!WebSocketService) {
			WebSocketService.instance = new WebSocketService()

		}
		return WebSocketService.instance;
	}
	constructor() {
		this.socketRef = null;
	}

	connect(chatURL) {
		const path = `ws://127.0.0.1:8000/ws/messenger/${chatURL}/`;
		this.socketRef = new WebSocket(path);
		this.socketRef.onopen = () => {

		};
		this.socketNewMessage(JSON.stringify({
			command: 'fetch_messages'
		}))
		this.socketRef.onmessage = (e) => {
			this.socketNewMessage(e.data);
		};
		this.socketRef.onerror = (e) => {
			console.log(e.massage);

		};
		this.socketRef.onclose = () => {
			this.connect();

		};
	}

	disconnect() {
		this.socketRef.close();
	}
	socketNewMessage(data) {
		const parsedData = JSON.parse(data);
		const command = parsedData.command;
		if (Object.keys(this.callbacks).length == 0) {
			return;
		}
		if (command === 'messages') {
			this.callbacks[command](parsedData.messages)
		}
		if (command === 'new_message') {
			this.callbacks[command](parsedData.message)
		}
	}
	fetchMessages(username) {
		this.sendMessage({
			command: 'fetch_messages',
			username: username
		});
	}
	newChatMessage(message) {
		this.sendMessage({
			command: 'new_message',
			from: message.from,
			message: message.content
		})
	}
	addCalbacks(messagesCallback, newMessageCallback) {
		this.callbacks['messages'] = messagesCallback;
		this.callbacks['new_message'] = newMessageCallback;
	}
	sendMessage(data) {
		try {
			this.socketRef.send(JSON.stringify({...data
			}));
		} catch (err) {
			console.log(err.message);
		}
	}
	waitForSocketConnection(callback) {
		const socket = this.socketRef;
		const recursion = this.waitForSocketConnection;
		setTimeout(
			function() {
				if (socket.readyState === 1) {
					console.log('connecton is secure');
					if (callback != null) {
						callback();
					}
					return;
				} else {
					console.log('waiting for connection...');
					recursion(callback);
				}
			}, 1)
	}
}

const WebSocketInstance = WebSocketService.getInstance();
export default WebSocketInstance;