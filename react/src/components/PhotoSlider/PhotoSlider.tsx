import React, { useState } from 'react';
import './PhotoSlider.css'; // Import your CSS file for styling
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';

interface PhotoSliderProps {
  photos: string[];
}

const PhotoSlider: React.FC<PhotoSliderProps> = ({ photos }) => {
  const [currentPhotoIndex, setCurrentPhotoIndex] = useState(0);

  const handleThumbnailClick = (index: number) => {
    setCurrentPhotoIndex(index);
  };

  const handlePrevClick = () => {
    setCurrentPhotoIndex((prevIndex) => (prevIndex === 0 ? photos.length - 1 : prevIndex - 1));
  };

  const handleNextClick = () => {
    setCurrentPhotoIndex((prevIndex) => (prevIndex === photos.length - 1 ? 0 : prevIndex + 1));
  };

  return (
    <div className="photo-slider-container">
      <div className="main-photo-container">
        <img
          className="main-photo"
          src={photos[currentPhotoIndex]}
          alt={`Photo ${currentPhotoIndex + 1}`}
        />
        <button className="prev-btn" onClick={handlePrevClick}>
          <ArrowBackIcon />
        </button>
        <button className="next-btn" onClick={handleNextClick}>
          <ArrowForwardIcon />
        </button>
      </div>
      <div className="thumbnail-container">
        {photos.map((photo, index) => (
          <img
            key={index}
            className={`thumbnail ${index === currentPhotoIndex ? 'active' : ''}`}
            src={photo}
            alt={`Thumbnail ${index + 1}`}
            onClick={() => handleThumbnailClick(index)}
          />
        ))}
      </div>
    </div>
  );
};

export default PhotoSlider;
