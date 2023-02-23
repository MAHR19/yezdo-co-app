import React from 'react';
import { TextField } from '@mui/material';

const CustomTextField = ({label, placeholder, error, haserror, variant}) =>{
    return(
        <TextField 
         fullWidth 
         color = 'success'
         size = 'small'
         label = {label}
         variant = {variant}
          />
    );
}

export default CustomTextField;