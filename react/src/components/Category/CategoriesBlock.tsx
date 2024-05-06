
type Props = {
    categories: Category[];
}

const CategoriesBlock = ({ categories }: Props) => {
    return(<div>{categories.map((category) => (<div>
        <div>{category.title}</div>
        <div>{category.id}</div>
    </div>))}
        
    </div>)
};
export default CategoriesBlock;
