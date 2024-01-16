import FooterColumnHeader from "./FooterColumnHeader";
import FooterColumnItem from "./FooterColumnItem";

export default function FooterColumn(props) {
  return (
    <>
      <div className="footer-column egqqf8t2">
        <FooterColumnHeader title={props.column.title} />
        <div className="footer-column-items egqqf8t1">
            {props.column.items.map(item =><FooterColumnItem item={item} key={item.title}/>)}
        </div>
      </div>
    </>
  );
}
