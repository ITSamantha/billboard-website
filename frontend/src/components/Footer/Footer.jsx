import {footer_data} from '../../data/footer'
import FooterColumn from './FooterColumn';

export default function Footer() {
  return (
    <>
      <div className="main-footer-container e1eprvtp1">
        <div data-auto="footer-container" className="css-4ke7ep egqqf8t5">
          <div className="footer-columns egqqf8t0">
            {footer_data.map(column=><FooterColumn column={column} key={column.title} />)}
            <div className="footer-column egqqf8t2">
              <div className="footer-column-header e3vrfmg6">
                <span className="footer-span">
                  <span className="footer-span">Квартиры в аренду</span>
                </span>
              </div>
              <div className="footer-column-items egqqf8t1">
                <a
                  href="/for-rent/ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартиры в аренду по всей стране
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/תל-אביב-יפו-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартиры в аренду в Тель-Авиве
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/ירושלים-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартиры в аренду в Иерусалиме
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/הרצליה-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартиры в аренду в Герцлии
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/רמת-גן-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартиры в аренду в Рамат-Гане
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/גבעתיים-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартира в аренду в Гиватаиме
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/חיפה-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартира в аренду в Хайфе
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/אשדוד-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартиры в аренду в Ашдоде
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/פתח-תקווה-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Аренда квартир в Петах-Тикве
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/חולון-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартиры в аренду в Холоне
                    </span>
                  </span>
                </a>
                <a
                  href="/for-rent/רחובות-ישראל?tracking_search_source=homepage_footer"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Квартиры в аренду в Реховот
                    </span>
                  </span>
                </a>
              </div>
            </div>
            <div className="footer-column egqqf8t2">
              <div className="footer-column-header e3vrfmg6">
                <span className="footer-span">
                  <span className="footer-span">кварталы</span>
                </span>
              </div>
              <div className="footer-column-items egqqf8t1">
                <a
                  href="/local/pricesHeatmap?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Карта недвижимости Израиля
                    </span>
                  </span>
                </a>
                <a
                  href="/area-info/תל-אביב-יפו-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Районы Тель-Авива</span>
                  </span>
                </a>
                <a
                  href="/area-info/ירושלים-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Районы Иерусалима</span>
                  </span>
                </a>
                <a
                  href="/area-info/הרצליה-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Герцлия: Районы</span>
                  </span>
                </a>
                <a
                  href="/area-info/רמת-גן-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Рамат-Ган: Районы</span>
                  </span>
                </a>
                <a
                  href="/area-info/גבעתיים-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Гиватаим: Районы</span>
                  </span>
                </a>
                <a
                  href="/area-info/חיפה-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Хайфа: Районы</span>
                  </span>
                </a>
                <a
                  href="/area-info/אשדוד-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Ашдод: Районы</span>
                  </span>
                </a>
                <a
                  href="/area-info/פתח-תקווה-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Районы Петах-Тиквы</span>
                  </span>
                </a>
                <a
                  href="/area-info/חולון-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Холон: Районы</span>
                  </span>
                </a>
                <a
                  href="/area-info/רחובות-ישראל?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">кварталы на улицах</span>
                  </span>
                </a>
              </div>
            </div>
            <div className="footer-column egqqf8t2">
              <div className="footer-column-header e3vrfmg6">
                <span className="footer-span">
                  <span className="footer-span">тарелки</span>
                </span>
              </div>
              <div className="footer-column-items egqqf8t1">
                <a
                  href="https://www.madlan.co.il/blog?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Блог Мадлана</span>
                  </span>
                </a>
                <a
                  href="/education/bestSchools?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Образование и карта мицвы
                    </span>
                  </span>
                </a>
                <a
                  href="/developers?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Индекс предпринимателей</span>
                  </span>
                </a>
                <a
                  href="/search-agent?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">База данных брокеров</span>
                  </span>
                </a>
                <a
                  href="/madad?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Брокерский индекс 2022/23
                    </span>
                  </span>
                </a>
                <a
                  href="/madad/2022?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Индекс брокера 2021/22</span>
                  </span>
                </a>
                <a
                  href="/mechirLamishtaken/introduction?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Цена за арендатора</span>
                  </span>
                </a>
                <a
                  href="/mechirLamishtaken/eligible?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Калькулятор приемлемости
                    </span>
                  </span>
                </a>
                <a
                  href="/article/main?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Статьи о недвижимости</span>
                  </span>
                </a>
                <a
                  href="/appartmentTax/calculator?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Калькулятор налога на покупку
                    </span>
                  </span>
                </a>
                <a
                  href="/lp/homeOwner?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Мой дом</span>
                  </span>
                </a>
              </div>
            </div>
            <div className="footer-column egqqf8t2">
              <div className="footer-column-header e3vrfmg6">
                <span className="footer-span">
                  <span className="footer-span">информация</span>
                </span>
              </div>
              <div className="footer-column-items egqqf8t1">
                <a
                  href="/lp/promotion?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Реклама для предпринимателей
                    </span>
                  </span>
                </a>
                <a
                  href="/lp/agents?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Реклама для брокеров</span>
                  </span>
                </a>
                <a
                  href="/professional?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Профессиональная система для предпринимателей
                    </span>
                  </span>
                </a>
                <a
                  href="/agent/main?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">
                      Профессиональная система для брокеров
                    </span>
                  </span>
                </a>
                <a
                  href="https://www.madlan.co.il/etc/jobs?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">нужный</span>
                  </span>
                </a>
                <a
                  href="/etc/faq?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Вопросы и ответы</span>
                  </span>
                </a>
                <a
                  href="/etc/aboutUs?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">о</span>
                  </span>
                </a>
                <a
                  href="/etc/terms?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Условия эксплуатации</span>
                  </span>
                </a>
                <a
                  href="/accessibility?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Заявление о доступности</span>
                  </span>
                </a>
                <a
                  href="/lp/connectUs?source=footer_link"
                  target="_blank"
                  className="footer-column-item egqqf8t6"
                >
                  <span className="footer-span">
                    <span className="footer-span">Связаться с нами</span>
                  </span>
                </a>
                <a href="#" className="footer-column-item egqqf8t6">
                  <span className="footer-span">
                    <span className="footer-span">восстановление пароля</span>
                  </span>
                </a>
              </div>
            </div>
          </div>
          <div className="css-pwzg5p egqqf8t4">
            <div className="css-19peoj6 e11nvyc7">
              <a href="https://www.facebook.com/madlan.co.il/" target="_blank">
                <div className="css-196bxl7 e11nvyc8">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    viewBox="0 0 10 18"
                  >
                    <path
                      fill="#3B5998"
                      fillRule="evenodd"
                      d="M5.662 3.918c0-1.757 3.067-.856 3.067-.856l.4-2.728S7.553-.07 5.662.01C1.768.177 1.903 3.248 1.903 3.248V5.93H0v2.775h1.903V18h3.759V8.705h2.856l.22-2.775H5.661V3.918"
                    ></path>
                  </svg>
                </div>
              </a>
              <a
                href="https://www.linkedin.com/company/localize-city/"
                target="_blank"
              >
                <div className="css-196bxl7 e11nvyc8">
                  <svg
                    height="16"
                    viewBox="0 0 512 512"
                    width="16"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M409.391,511.359V317.203c0,0-5.75-51.938-56-51.938c-50.219,0-59.406,49.375-59.406,49.375v196.719h-103.5l1.688-320.719 h100.125l-0.813,40.313c0,0,20.876-52.688,99.531-52.688c78.625,0,114.25,45.188,120.875,129.688c0,84.531,0,203.406,0,203.406 H409.391z M63.547,145.078c-35.563,0-64.438-25.438-64.438-56.875s28.875-56.938,64.438-56.938s64.438,25.5,64.438,56.938 S99.109,145.078,63.547,145.078z M127.422,511.734H0.172V191.453l127.25-0.813V511.734z"></path>
                  </svg>
                </div>
              </a>
              <a href="https://localizeos.com/" target="_blank">
                <div className="css-196bxl7 e11nvyc8">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    e
                    height="16"
                    viewBox="0 0 31 32"
                  >
                    <defs>
                      <linearGradient
                        id="id-14a"
                        x1="83.218%"
                        x2="4.337%"
                        y1="14.092%"
                        y2="97.832%"
                      >
                        <stop
                          offset="0%"
                          stopColor="#029499"
                          stopOpacity=".07"
                        ></stop>
                        <stop
                          offset="100%"
                          stopColor="#029499"
                          stopOpacity=".1"
                        ></stop>
                      </linearGradient>
                    </defs>
                    <g fill="none" fillRule="evenodd">
                      <path
                        fill="#018489"
                        fillOpacity=".09"
                        d="M15.585 28.345c-3.712 0-7.03-1.724-9.23-4.432a12.387 12.387 0 0 1-2.765-7.836c0-6.776 5.37-12.268 11.995-12.268 6.625 0 11.995 5.492 11.995 12.268 0 6.776-5.37 12.268-11.995 12.268zm-.12-4.167c4.395.047 7.996-3.559 8.044-8.054.047-4.496-3.476-8.179-7.871-8.226-4.396-.047-7.997 3.559-8.044 8.054-.048 4.496 3.475 8.179 7.87 8.226z"
                      ></path>
                      <path
                        fill="url(#id-14a)"
                        d="M15.54 31.896c8.548 0 15.415-7.114 15.415-15.858S24.026.206 15.477.206 0 7.341 0 16.084V29.17a2.726 2.726 0 0 0 2.726 2.726H15.54zm.084-10.971c-2.635-.029-4.748-2.249-4.719-4.959.029-2.71 2.188-4.883 4.822-4.855 2.635.029 4.748 2.248 4.719 4.958-.029 2.71-2.188 4.884-4.822 4.856z"
                      ></path>
                      <path
                        fill="#029499"
                        d="M1.862 16.246c1.03 0 1.868.831 1.877 1.862l.07 8.884a1.09 1.09 0 0 0 1.095 1.082l7.91-.043a1.898 1.898 0 0 1 1.907 1.888v.01a1.916 1.916 0 0 1-1.908 1.916l-10.623.043A2.18 2.18 0 0 1 0 29.715V18.108c0-1.028.834-1.862 1.862-1.862zm13.77-8.893c4.667.05 8.409 3.935 8.358 8.677-.051 4.743-3.875 8.547-8.543 8.497-4.668-.05-8.41-3.935-8.358-8.677.05-4.743 3.874-8.547 8.542-8.497zm-.042 3.816c-2.56-.027-4.657 2.086-4.685 4.72-.028 2.636 2.024 4.794 4.584 4.821 2.56.028 4.657-2.085 4.684-4.72.028-2.635-2.024-4.793-4.583-4.82z"
                      ></path>
                    </g>
                  </svg>
                </div>
              </a>
            </div>
          </div>
        </div>
        <div className="css-10dtbrx egqqf8t3">
          <div className="css-4ke7ep egqqf8t5">
            <div className="css-gr93xn e11nvyc10">
              <a
                target="_blank"
                rel="nofollow"
                href="https://www.madlan.co.il/etc/jobs?source=footer_link"
              >
                <div data-auto="careers-link" className="css-7so23d e3vrfmg6">
                  <span className="footer-span">
                    <span className="footer-span">нужный</span>
                  </span>
                </div>
              </a>
              <a
                target="_blank"
                rel="nofollow"
                href="/etc/terms?source=footer_bar_link"
              >
                <div data-auto="terms-link" className="css-7so23d e3vrfmg6">
                  <span className="footer-span">
                    <span className="footer-span">Условия эксплуатации</span>
                  </span>
                </div>
              </a>
              <a href="/site-map">
                <div data-auto="site-map-link" className="css-7so23d e3vrfmg6">
                  <span className="footer-span">
                    <span className="footer-span">карта сайта</span>
                  </span>
                </div>
              </a>
              <a target="_blank" rel="nofollow" href="https://localizeos.com">
                <div className="css-7so23d e3vrfmg6">
                  <span className="footer-span">
                    <span className="footer-span">ЛокализеОС</span>
                  </span>
                </div>
              </a>
            </div>
            <div data-auto="copyright" className="css-1rxldqv e11nvyc11">
              <span className="footer-span">
                <span className="footer-span">Мадлен 2024</span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
