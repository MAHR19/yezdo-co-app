import React from 'react';
import { Stack, Button, Typography, Divider } from '@mui/material';
import CustomTextField from '../input/CustomTextField'

//import { Formik } from 'formik';


const SignInForm  = () =>{
    return(
        <Stack
         spacing = {4}
         sx={{padding : 4}}
         >
            <Typography
             variant = 'h6'
             >
                Fill your data to create an account
            </Typography>
            <CustomTextField 
             label = {'Email'}
             variant = {'standard' }
             />
             <CustomTextField 
             label = {'Password'}
             variant = {'standard'}
             />
             <CustomTextField 
             label = {'Confirm password'}
             variant = {'standard'}
             />
             <Button
              variant = 'contained'
              color = 'success'
              href='/main'
              >
                Create account
             </Button>
             <Divider>
                <Typography variant = 'subtitle1'>
                    or sign in whit
                </Typography>
             </Divider>
        </Stack>
    );

}

export default SignInForm;

