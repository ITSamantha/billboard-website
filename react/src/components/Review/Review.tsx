type Props = {
  review: Review;
};

const Review = ({ review }: Props) => {
  return (
    <div>
      <div>{review.rating}</div>
      <div>{review.created_at}</div>
      <div>{review.text}</div>
    </div>
  );
};

export default Review;
