import { useState } from 'react';

const UserVerification = () => {
  const [code, setCode] = useState<string>('');
  const [error, setError] = useState<string>('');

  const handleSubmit = () => {};

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="verificationCode">Verification Code</label>

        {error && <p style={{ color: 'red' }}>{error}</p>}
      </form>
    </div>
  );
};

export default UserVerification;
