import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { selectMyUser } from '../../redux/slices/MyUserSlice';

const Menu = () => {
  const user = useSelector(selectMyUser);

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
                <Link to={`/profile/${user.id}`} className="Header__Auth__Button">
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
