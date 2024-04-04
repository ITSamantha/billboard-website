class WebSocketInstance extends WebSocket {
  constructor(url: string) {
    super(url);
  }

  sendJson(data: any) {
    this.send(JSON.stringify(data));
  }
}

export default WebSocketInstance;
