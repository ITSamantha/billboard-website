import { Link } from 'react-router-dom';

const PaymentSuccess = () => {
  return (
    <div>
      the payment was successful
      <Link to={'/'}>
        <button>Return to home page</button>
      </Link>
    </div>
  );
};

export default PaymentSuccess;
