import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { fetchMyUser, selectMyUser } from '../../redux/slices/MyUserSlice';
import { AppDispatch } from '../../redux/store';
import { useEffect } from 'react';

const Menu = () => {
  const user = useSelector(selectMyUser);
  const dispatch = useDispatch<AppDispatch>();

  useEffect(() => {
    if (user) {
      dispatch(fetchMyUser());
    }
  }, [dispatch]);

  return (
    <header className="Header">
      <div className="container">
        <div className="Header__Wrapper">
          <div className="Header__Logo">
            <Link to="/">
              <img src="/images/Logo.png" alt="Logo" />
            </Link>
          </div>
          <div className="Header__Navbar">
            <>
              <Link to="/" className="Header__Navbar__Item">
                Advertisements
              </Link>
              {!user && (
                <Link to="/login" className="Header__Navbar__Item">
                  Upload
                </Link>
              )}
              {user && (
                <>
                  <Link to="/upload-form" className="Header__Navbar__Item">
                    Upload
                  </Link>
                  <Link to="/chats" className="Header__Navbar__Item">
                    Chats
                  </Link>
                </>
              )}
            </>
          </div>
          <div className="Header__Auth">
            {user ? (
              <div>
                <Link to={`/profile/${user.id}`} className="Header__Auth__Button">
                  Profile
                </Link>
                <Link to={`/subscription`} className="Header__Auth__Button">
                  Balance: {user.available_ads} ads
                </Link>
              </div>
            ) : (
              <Link to="/login" className="Header__Auth__Button">
                Login
              </Link>
            )}
          </div>
        </div>
      </div>
    </header>
  );
};

export default Menu;
