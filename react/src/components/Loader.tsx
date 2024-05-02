import { CircularProgress } from '@mui/material';

interface LoaderProps {
  fullscreen?: boolean;
}

const Loader = ({ fullscreen }: LoaderProps) => {
  if (fullscreen) {
    return <CircularProgress />;
  }
  return (
    <div
      className="Loader"
      style={{
        minWidth: 100,
        minHeight: 100,
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center'
      }}
    >
      <CircularProgress />
    </div>
  );
};

export default Loader;
