import React, { useEffect, useRef, useState } from 'react';
import { makeStyles } from '@mui/styles';
import { Button, Container, FormHelperText, ThemeProvider, Typography } from '@mui/material';
import CodeVerificationInput from '../../components/Profile/CodeVerificationInput';
import { THEME } from './Profile';

const useStyles = makeStyles({
  root: {
    marginTop: '1.5rem'
  },
  form: {
    width: '100%',
    marginTop: '1rem'
  },
  submit: {
    margin: '1rem 0',
    marginTop: 15
  }
});

const NUMBER_OF_DIGITS_IN_CODE = 6;

const PhoneConfirmation = () => {
  const classes = useStyles();
  const [verificationCode, setVerificationCode] = useState('');

  const [error, setError] = useState<boolean>(false)
  const errorFlag = useRef<number>(0)

  const handleSend = (event: any) => {
    event?.preventDefault();
    if (event === null) {
      if (errorFlag.current !== 0) return
    }
    if (verificationCode !== '123456') {
      setError(true)
      errorFlag.current += 1
      setTimeout(() => {
        errorFlag.current -= 1
        if (errorFlag.current === 0) {
          setError(false)
        }
      }, 3000)
    } else {
      console.log("accepted")
    }
  };

  useEffect(() => {
    if (verificationCode.split('').filter((l) => {
      return /^\d$/.test(l)
    }).length === NUMBER_OF_DIGITS_IN_CODE) {
      handleSend(null);
    }
  }, [verificationCode]);

  return (
    <ThemeProvider theme={THEME}>

      <Container maxWidth="xs" className={classes.root}>
        <Typography variant="h4" component="h1" gutterBottom>Phone Confirmation (123456 correct)</Typography>

        <Typography variant="body1" gutterBottom>
          Please enter the verification code sent to your phone.
        </Typography>

        <form className={classes.form} onSubmit={handleSend}>

          <div style={{ marginBottom: 15 }}>
            <CodeVerificationInput numberOfDigits={NUMBER_OF_DIGITS_IN_CODE} onChange={setVerificationCode} error={error} />
          </div>
          {error && <div style={{ marginBottom: 15}}>
            <FormHelperText error>Incorrect code, please try again</FormHelperText>
          </div>}

          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Submit
          </Button>
        </form>
      </Container>
    </ThemeProvider>
  );
};

export default PhoneConfirmation;
