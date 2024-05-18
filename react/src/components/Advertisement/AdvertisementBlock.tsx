import { Link } from 'react-router-dom';
import { CiLocationOn } from 'react-icons/ci';
import Loader from '../Loader';

type Props = {
  advertisements: AdInfo[];
  advertisementsInRow: number;
  maxAdvertisements: number;
};

function trimText(text: string, maxLength: number = 50): string {
  if (text.length <= maxLength) {
    return text;
  }
  return text.slice(0, maxLength) + '...';
}

const AdvertisementBlock = ({ advertisements, advertisementsInRow, maxAdvertisements }: Props) => {
  if (!advertisements) {
    return (
      <div>
        <Loader />
      </div>
    );
  }

  return (
    <div>
      <section>
        <div className="Advertisements">
          <div className="Advertisements__Wrapper">
            {advertisements.slice(0, maxAdvertisements).map((ad) => (
              <div className="Advertisement">
                <div className="Advertisement__Wrapper">
                  <Link to={`/advertisement/${ad.id}`}>
                    <div className="Advertisement__Image">
                      <img src="https://http.cat/300" alt="Advertisement" height={'300px'} />
                    </div>
                    <div className="Advertisement__Content">
                      <h4>
                        {trimText(ad.title, 35)}
                        <span>{ad.price.toFixed(2)} ₪</span>
                      </h4>
                      <p>{trimText(ad.user_description)}</p>
                      <span className="Advertisement__Address">
                        {ad.address && (
                          <>
                            <CiLocationOn /> {ad.address.country.title}, {ad.address.city.title},{' '}
                            {ad.address.street}
                          </>
                        )}
                      </span>
                    </div>
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export default AdvertisementBlock;
