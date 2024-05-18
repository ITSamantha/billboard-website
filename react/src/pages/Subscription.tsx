import { useEffect, useState } from 'react';
import { createPayment, getSubscriptions } from '../service/dataService';
import { Link, useNavigate } from 'react-router-dom';

type Subscription = {
  id: number;
  name: string;
  description: string;
  price: number;
  available_ads: number;
};

const Subscription = () => {
  const [subscriptions, setSubscriptions] = useState<Subscription[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchData() {
      const subs = await getSubscriptions();
      setSubscriptions(subs);
    }
    fetchData();
  }, []);

  const handlePaymentRedirect = async (id: number) => {
    const link = await createPayment(id);
    window.location.href = link.url;
  };

  return (
    <div>
      {subscriptions.map((subscription) => (
        <div key={subscription.id}>
          <div>{subscription.price}</div>
          <div>{subscription.name}</div>
          <div>{subscription.description}</div>
          <button
            onClick={() => {
              handlePaymentRedirect(subscription.id);
            }}
          >
            choose plan
          </button>
        </div>
      ))}
    </div>
  );
};

export default Subscription;
