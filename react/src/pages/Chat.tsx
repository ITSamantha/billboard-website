import { Button, TextField } from '@mui/material';
import { useState } from 'react';

const Chat = () => {
  const [message, setMessage] = useState<string>('');

  return (
    <div>
      <TextField
        rows={2}
        maxRows={6}
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
