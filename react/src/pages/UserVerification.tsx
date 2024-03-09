import { Button, Input } from 'antd';
import { useState } from 'react';

const UserVerification = () => {
  const [code, setCode] = useState<string>('');
  const [error, setError] = useState<string>('');

  const handleSubmit = () => {};

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="verificationCode">Verification Code</label>
        <Input
          type="text"
          id="verificationCode"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          maxLength={6}
          minLength={6}
          pattern="\d*"
          required
        />
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <Button onClick={handleSubmit}>Verify</Button>
      </form>
    </div>
  );
};

export default UserVerification;
