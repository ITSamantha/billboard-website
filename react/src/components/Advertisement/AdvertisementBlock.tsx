import { Grid, Paper, Typography } from '@mui/material';
import { Button } from 'antd';
import { Link } from 'react-router-dom';

type Props = {
  advertisements: AdInfo[];
  advertisementsInRow: number;
  maxAdvertisements: number;
};

const AdvertisementBlock = ({ advertisements, advertisementsInRow, maxAdvertisements }: Props) => {
  if (!advertisements) {
    return <div> No advertisements!</div>;
  }

  return (
    <div>
      <section>
        <Grid container spacing={2}>
          {advertisements.slice(0, maxAdvertisements).map((ad) => (
            <Grid item xs={12 / advertisementsInRow}>
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
