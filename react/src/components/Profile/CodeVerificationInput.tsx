import React, { createRef, Ref, useEffect, useRef, useState } from 'react';
import { makeStyles } from '@mui/styles';

type CodeVerificationProps = {
  error: boolean;
  numberOfDigits: number;
  onChange: (code: string) => void;
};

const useStyles = makeStyles({
  root: {
    marginTop: '1.5rem'
  },
  form: {
    width: '100%',
    marginTop: '1rem',
    display: 'flex',
    justifyContent: 'center',
    gap: '0.5rem'
  },
  digitInput: {
    width: '3rem',
    textAlign: 'center',
    fontSize: 18
  }
});

const CodeVerificationInput = ({ numberOfDigits, onChange, error }: CodeVerificationProps) => {
  const isMobileDevice = window.innerWidth <= 992;

  const classes = useStyles();

  const [verificationCode, setVerificationCode] = useState<string[]>([]);

  const inputRefs = useRef<Ref<HTMLInputElement>[]>([]);

  useEffect(() => {
    onChange(verificationCode.join(''));
  }, [onChange, verificationCode]);

  const focusOnInput = (index: number) => {
    if (index >= 0 && index < numberOfDigits) {
      // @ts-ignore
      let currentInputRef = inputRefs.current[index].current;
      if (currentInputRef) {
        currentInputRef.focus();
        if (verificationCode.length === numberOfDigits) {
          let verificationCodeCopy = JSON.parse(JSON.stringify(verificationCode));
          verificationCodeCopy[index] = parseInt(verificationCodeCopy[index]);
          setVerificationCode(verificationCodeCopy);
        }
      }
    }
  };

  useEffect(() => {
    setVerificationCode([...new Array(numberOfDigits)].map(() => ''));
    [...new Array(numberOfDigits)].forEach((_, index) => {
      inputRefs.current[index] = createRef<HTMLInputElement>();
    });
    setTimeout(() => {
      focusOnInput(0);
    }, 300);
  }, [numberOfDigits]);

  const handleKeyDown = (index: number, e: React.KeyboardEvent<HTMLDivElement>) => {
    if (isMobileDevice) return;
    let key = e.key;
    let verificationCodeCopy = JSON.parse(JSON.stringify(verificationCode));
    const FORWARD_KEYS = ['ArrowRight', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    const BACK_KEYS = ['ArrowLeft', 'Delete', 'Backspace'];
    const APPEND_KEYS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    const DELETE_KEYS = ['Delete', 'Backspace'];
    if (DELETE_KEYS.includes(key)) {
      verificationCodeCopy[index] = '';
    }
    if (BACK_KEYS.includes(key)) {
      focusOnInput(index - 1);
    } else if (APPEND_KEYS.includes(key)) {
      verificationCodeCopy[index] = key;
    }
    if (FORWARD_KEYS.includes(key)) {
      focusOnInput(index + 1);
    }
    if (!APPEND_KEYS.includes(key) && !DELETE_KEYS.includes(key)) {
      verificationCodeCopy[index] = parseInt(verificationCodeCopy[index]);
    }
    setVerificationCode(verificationCodeCopy);
  };

  const handleChange = (index: number, e: React.ChangeEvent<HTMLInputElement>) => {
    if (!isMobileDevice) return;
    let verificationCodeCopy = JSON.parse(JSON.stringify(verificationCode));
    let inputtedValue = e.target.value;
    if (inputtedValue.length === 0) {
      verificationCodeCopy[index] = '';
      focusOnInput(index - 1);
    } else if (inputtedValue.length === 1) {
      verificationCodeCopy[index] = inputtedValue;
      focusOnInput(index + 1);
    } else {
      if (verificationCodeCopy[index] === inputtedValue[0])
        verificationCodeCopy[index] = inputtedValue[1];
      if (verificationCodeCopy[index] === inputtedValue[1])
        verificationCodeCopy[index] = inputtedValue[0];
      focusOnInput(index + 1);
    }
    setVerificationCode(verificationCodeCopy);
  };

  return (
    <div className={classes.form}>
      {verificationCode.map((digit, index) => (
        <div className={'CodeVerification__Digit' + (error ? ' _error' : '')}>
          <input
            value={digit}
            ref={inputRefs.current[index]}
            pattern="\d*"
            type="number"
            onChange={(e) => handleChange(index, e)}
            onKeyDown={(e) => handleKeyDown(index, e)}
          />
        </div>
      ))}
    </div>
  );
};

export default CodeVerificationInput;
