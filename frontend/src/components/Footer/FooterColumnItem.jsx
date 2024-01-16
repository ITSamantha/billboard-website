export default function FooterColumnItem(props) {
  return (
    <>
      <a
        href={props.item.href}
        target="_blank"
        className="footer-column-item egqqf8t6"
      >
        {props.item.title}
      </a>
    </>
  );
}
