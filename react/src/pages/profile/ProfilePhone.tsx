import React, { useEffect, useRef, useState } from 'react';
import { makeStyles } from '@mui/styles';
import { Button, Container, FormHelperText, ThemeProvider, Typography } from '@mui/material';
import CodeVerificationInput from '../../components/Profile/CodeVerificationInput';
import { THEME } from './Profile';
import { sendCode, tryCode } from '../../service/dataService';
import { Link } from 'react-router-dom';
import { ToastContainer, ToastPosition, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

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

const NUMBER_OF_DIGITS_IN_CODE = 4;

const PhoneConfirmation = () => {
  const classes = useStyles();
  const [verificationCode, setVerificationCode] = useState('');

  const [error, setError] = useState<string>('');
  const errorFlag = useRef<number>(0);

  const [codeTimeout, setCodeTimeout] = useState<number>(60);

  useEffect(() => {
    let interval = setInterval(() => {
      setCodeTimeout((old) => {
        return Math.max(0, old - 1);
      });
    }, 1000);
    return () => {
      clearInterval(interval);
    };
  }, []);

  const handleSend = (event: any) => {
    event?.preventDefault();
    if (errorFlag.current > 2) return;
    if (event === null) {
      if (errorFlag.current !== 0) return;
    }
    tryCode(verificationCode)
      .then((response) => {
        toast.success(
          'Phone was successfully verified and now you have 5 free advertisement to publish!.',
          {
            position: 'top-center',
            autoClose: 5000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined
          }
        );
      })
      .catch((error) => {
        console.log('real error', error);
        setError(error.response.data.detail);
        errorFlag.current += 1;
        setTimeout(() => {
          errorFlag.current -= 1;
          if (errorFlag.current === 0) {
            setError('');
          }
        }, 3000);
      });
  };

  useEffect(() => {
    if (
      verificationCode.split('').filter((l) => {
        return /^\d$/.test(l);
      }).length === NUMBER_OF_DIGITS_IN_CODE
    ) {
      handleSend(null);
    }
  }, [verificationCode]);

  return (
    <ThemeProvider theme={THEME}>
      <Container maxWidth="xs" className={classes.root}>
        <Typography variant="h4" component="h1" gutterBottom>
          Phone Confirmation (1111 correct)
        </Typography>

        <Typography variant="body1" gutterBottom>
          Please enter the verification code sent to your phone.
        </Typography>

        <form className={classes.form} onSubmit={handleSend}>
          <div style={{ marginBottom: 15 }}>
            <CodeVerificationInput
              numberOfDigits={NUMBER_OF_DIGITS_IN_CODE}
              onChange={setVerificationCode}
              error={!!error}
            />
          </div>
          {error && (
            <div style={{ marginBottom: 15 }}>
              <FormHelperText error>{error}</FormHelperText>
            </div>
          )}

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
        <Link
          to="."
          style={{ display: 'block', marginTop: 15 }}
          onClick={(e) => {
            e.preventDefault();
            if (codeTimeout <= 0) {
              sendCode().then((response) => {
                setCodeTimeout(60);
                console.log('code sent', response);
              });
            }
          }}
        >
          {codeTimeout <= 0 ? (
            <>Send code again</>
          ) : (
            <>You can send code again in {codeTimeout} seconds</>
          )}
        </Link>
      </Container>
      <ToastContainer />
    </ThemeProvider>
  );
};

export default PhoneConfirmation;
