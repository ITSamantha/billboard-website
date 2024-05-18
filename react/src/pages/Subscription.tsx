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
    <div className="container">

      <div className="pricing">
        <div className="pricing__title">
          <h1>Pick Your Plan</h1>
          <p>Simple, transparent pricing No contracts. No surprise fees.</p>
        </div>
        <div className="pricing__content">

          <div className="pricing__row">
            <div className="pricing__item__wrapper">
              <div className="pricing__item">
                <div className="pricing__item__title">
                  <h3>Free</h3>
                  <div className="pricing__item__title__price">
                    ₪ 0.00
                  </div>
                </div>
                <p>Verify your phone number and receive 5 free advertisements!</p>
                <div className="pricing__item__features">
                  <h4>Features</h4>
                  <ul>
                    <li>5 advertisements</li>
                    <li>Full Results &amp; No Queue</li>
                  </ul>
                </div>
                <Link to="/profile/edit" className="pricing__item__button">Verify phone</Link>
                <div className="pricing__item__payment-gateways">
                  <img src="https://aidet.tech/images/paypal.svg" alt="Paypal" />
                  <img src="https://aidet.tech/images/bitcoin.svg" alt="Bitcoin" />
                </div>
              </div>
            </div>


            {subscriptions.map((subscription) => (

              <div className="pricing__item__wrapper" key={subscription.id}>
                <div className="pricing__item">
                  <div className="pricing__item__title">
                    <h3>{subscription.name}</h3>
                    <div className="pricing__item__title__price">
                      ₪ {subscription.price.toFixed(2)}
                    </div>
                  </div>
                  <p>{subscription.description}</p>
                  <div className="pricing__item__features">
                    <h4>Features</h4>
                    <ul>
                      <li>{subscription.available_ads} advertisements</li>
                      <li>Full Results &amp; No Queue</li>
                      <li>10% bonus for future orders</li>
                    </ul>
                  </div>
                  <a href="#" onClick={() => {
                    handlePaymentRedirect(subscription.id);
                  }} className="pricing__item__button">Select Plan
                  </a>
                  <div className="pricing__item__payment-gateways">
                    <img src="https://aidet.tech/images/paypal.svg" alt="Paypal" />
                    <img src="https://aidet.tech/images/bitcoin.svg" alt="Bitcoin" />
                  </div>
                </div>
              </div>

            ))}

          </div>
        </div>
      </div>


    </div>
  );
};

export default Subscription;
