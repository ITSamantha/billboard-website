import { Button } from 'antd';
import TextArea from 'antd/es/input/TextArea';
import { useState } from 'react';

const Chat = () => {
  const [message, setMessage] = useState<string>('');

  return (
    <div>
      <TextArea
        autoSize={{ minRows: 2, maxRows: 6 }}
        value={message}
        onChange={(e) => {
          setMessage(e.target.value);
        }}
      />
      <Button>Send</Button>
    </div>
  );
};

export default Chat;
