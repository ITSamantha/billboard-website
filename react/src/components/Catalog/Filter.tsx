import { useEffect, useState } from 'react';
import { getFilters } from '../../service/dataService';
import { Button, Checkbox, GetProp } from 'antd';

type Filter = {
  id: number;
  name: string;
  type: string;
  values: Value[];
};

type Value = {
  id: number;
  value: string;
};

const Filter = () => {
  const [filters, setFilters] = useState<Filter[]>([]);

  useEffect(() => {
    setFilters(getFilters('test'));
  }, []);

  const onChange: GetProp<typeof Checkbox.Group, 'onChange'> = (checkedValues) => {
    console.log('checked = ', checkedValues);
  };

  const handleFiltersSet = () => {
    // sendFilters();
  };

  return (
    <div>
      {filters.map((item) => (
        <div>
          <div>{item.name}</div>
          <Checkbox.Group onChange={onChange} options={item.values.map((item) => item.value)} />
        </div>
      ))}
      <Button>Set</Button>
    </div>
  );
};

export default Filter;
