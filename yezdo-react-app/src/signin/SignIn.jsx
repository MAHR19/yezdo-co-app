import React from 'react';
import {Grid, Stack} from '@mui/material'
import SignInForm from './SignInForm';

/**
 *  Login Main Component
 * 
 */

const SignIn = () => {
    return(
        <Grid container spacing={2}>
            <Grid 
             item 
             xs = {12} 
             sm = {7} 
             md = {4}
             >
             <Stack
              alignContent={'center'}
              sx = {{padding : 8}}
              >
                <SignInForm />
             </Stack>
            </Grid>

            <Grid
             sx={{
                backgroundColor : 'success.main'
             }} 
             item
             xs = {12}
             sm = {5}
             md = {8}
             >
            </Grid>
        </Grid>
    );
}

export default SignIn;