import { Button, Dropdown, Space } from 'antd';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import { selectMyUser } from '../../redux/slices/MyUserSlice';
import { useEffect } from 'react';

const Menu = () => {
  const user = useSelector(selectMyUser);

  useEffect(() => {}, [user]);
  return (
    <header className="global-navigation-site-header">
      <div className="global-navigation-site-header-container">
        <section className="global-navigation-row primary">
          <div className=" global-navigation-row-container">
            <div className="header-row uitk-layout-flex uitk-layout-flex-align-items-center uitk-layout-flex-flex-wrap-nowrap uitk-spacing uitk-spacing-margin-unset uitk-spacing-padding-inlinestart-six uitk-spacing-padding-small-inlineend-three uitk-spacing-padding-medium-inlineend-three uitk-spacing-padding-large-inlineend-two uitk-spacing-padding-extra_large-inlineend-two uitk-layout-flex-item uitk-layout-flex-item-flex-grow-1">
              <div>
                <Link to="/" className="uitk-header-brand-logo">
                  <img
                    src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png"
                    alt="logo"
                  />
                </Link>
                <div
                  className="uitk-layout-flex uitk-layout-flex-align-items-center uitk-layout-flex-justify-content-flex-start uitk-layout-flex-flex-wrap-nowrap uitk-spacing uitk-spacing-padding-inlinestart-one uitk-layout-flex-item uitk-layout-flex-item-flex-basis-half_width uitk-layout-flex-item-flex-grow-1"
                  id="primary-navigation"
                >
                  <Dropdown
                    menu={{
                      items: [
                        {
                          key: '4',
                          danger: true,
                          label: 'a danger item'
                        }
                      ]
                    }}
                  >
                    <Space>קטגוריות מוצרים</Space>
                  </Dropdown>
                </div>
              </div>
              {user && (
                <div>
                  <Link to={`/profile/${user.id}`}>
                    <Button type="primary">Profile</Button>
                  </Link>
                  <Link to="/upload-form">
                    <Button type="primary">Upload</Button>
                  </Link>
                  <Button type="primary">Logout</Button>
                </div>
              )}

              {!user && (
                <Link to="/login">
                  <Button type="primary">Login</Button>
                </Link>
              )}
            </div>
          </div>
        </section>
      </div>
    </header>
  );
};

export default Menu;
