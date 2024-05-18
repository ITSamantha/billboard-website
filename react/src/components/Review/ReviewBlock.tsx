import Review from './Review';

type Props = {
  reviews: Review[];
};

const ReviewBlock = ({ reviews }: Props) => {
  return (
    <div>
      {reviews.map((review) => (
        <Review review={review} />
      ))}
    </div>
  );
};

export default ReviewBlock;
