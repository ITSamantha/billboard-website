import {Button, Input, TextField} from '@mui/material';
import React, {useState} from "react";
import { IoSearch } from "react-icons/io5";

const Search = () => {

    const [searchValue, setSearchValue] = useState<string>('')

    const handleSearch = () => {
        return;
    };

    return (
        <div className="Search">
            <TextField
                variant="outlined"
                margin="none"
                fullWidth
                id="search"
                label="Search for everything"
                defaultValue={searchValue}
                name="search"
                onChange={(event) => setSearchValue(event.target.value)}
                autoComplete="search"
            />
            <div className="Search__Button">
                <button onClick={handleSearch} type="submit">
                    <IoSearch />
                </button>
            </div>
        </div>
    );
};

export default Search;
