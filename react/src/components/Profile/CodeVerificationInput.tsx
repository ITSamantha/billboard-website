import React, { createRef, Ref, useEffect, useRef, useState } from 'react';
import { makeStyles } from '@mui/styles';

type CodeVerificationProps = {
  error: boolean,
  numberOfDigits: number,
  onChange: (code: string) => void
}

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

  const classes = useStyles();

  const [verificationCode, setVerificationCode] = useState<string[]>([]);
  const inputRefs = useRef<Ref<HTMLInputElement>[]>([]);

  useEffect(() => {
    onChange(verificationCode.join(''));
  }, [onChange, verificationCode]);

  useEffect(() => {
    setVerificationCode([...new Array(numberOfDigits)].map(() => ''));
    [...new Array(numberOfDigits)].forEach((_, index) => {
      inputRefs.current[index] = createRef<HTMLInputElement>();
    });
  }, [numberOfDigits]);

  const focusOnInput = (index: number) => {
    // @ts-ignore
    inputRefs.current[index].current.focus();
  };

  const handleKeyDown = (index: number, e: React.KeyboardEvent<HTMLDivElement>) => {
    console.log(e.key, index);
    let verificationCodeCopy = JSON.parse(JSON.stringify(verificationCode));
    const FORWARD_KEYS = ['ArrowRight', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    const BACK_KEYS = ['ArrowLeft', 'Delete', 'Backspace'];
    const APPEND_KEYS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    const DELETE_KEYS = ['Delete', 'Backspace'];
    alert(JSON.stringify([(e.target as any).value, e.key, e.keyCode]))
    if (DELETE_KEYS.includes(e.key)) {
      verificationCodeCopy[index] = '';
    }
    if (BACK_KEYS.includes(e.key)) {
      if (index - 1 >= 0) {
        focusOnInput(index - 1);
      }
    } else if (APPEND_KEYS.includes(e.key)) {
      verificationCodeCopy[index] = e.key;
    }
    if (FORWARD_KEYS.includes(e.key)) {
      if (index + 1 < numberOfDigits) {
        focusOnInput(index + 1);
      }
    }
    setVerificationCode(verificationCodeCopy);
  };

  return (

    <div className={classes.form}>
      {verificationCode.map((digit, index) => (
        <div className={"CodeVerification__Digit" + (error ? ' _error': '')}>
          <input value={digit}
                 ref={inputRefs.current[index]}
                 pattern="\d*"
                 onKeyDown={(e) => handleKeyDown(index, e)}
          />
        </div>
      ))}

    </div>
  );

};

export default CodeVerificationInput;
