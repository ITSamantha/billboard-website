import { Grid, Paper, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

type Props = {
  advertisements: AdInfo[];
  advertisementsInRow: number;
  maxAdvertisements: number;
};

const AdvertisementBlock = ({ advertisements, advertisementsInRow, maxAdvertisements }: Props) => {
  if (!advertisements || advertisements.length === 0) {
    return <div> No advertisements found!</div>;
  }

  return (
    <div>
      <section>
        <div className="Advertisements">
          {advertisements.slice(0, maxAdvertisements).map((ad) => (
            <div className="Advertisement">
              <Link to={`/advertisement/${ad.id}`}>
                <div className="Advertisement__Image">
                  <img src="https://http.cat/300" alt="Advertisement" height={'300px'} />
                </div>
                <div className="Advertisement__Content">
                  <h4>{ad.title}
                    <span> {ad.price.toFixed(2)}</span>
                  </h4>
                  <p>{ad.user_description}</p>
                  <span className="Advertisement__Address">{ad.address.toString()}</span>
                </div>
              </Link>
            </div>
          ))}
        </div>
        <Grid container spacing={2}>
          {advertisements.slice(0, maxAdvertisements).map((ad) => (
            <Grid item xs={12 / advertisementsInRow} key={ad.id}>
              <Link to={`/advertisement/${ad.id}`}>
                <Paper>
                  <img src="https://http.cat/300" alt="Advertisement" height={'300px'} />
                  <Typography variant="h6" component="h6">
                    {ad.title}
                  </Typography>
                  <Typography variant="body1">{ad.user_description}</Typography>
                  <Typography variant="body2">Advertisement Address</Typography>
                </Paper>
              </Link>
            </Grid>
          ))}
        </Grid>
      </section>
    </div>
  );
};

export default AdvertisementBlock;
