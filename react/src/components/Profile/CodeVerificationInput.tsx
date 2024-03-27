import React, { createRef, Ref, useEffect, useRef, useState } from 'react';

type CodeVerificationProps = {
  numberOfDigits: number,
  handleSend: (code: string) => void
}

const CodeVerificationInput = ({ numberOfDigits, handleSend }: CodeVerificationProps) => {

  const [verificationCode, setVerificationCode] = useState<string[]>([]);
  const inputRefs = useRef<Ref<HTMLInputElement>[]>([]);

  useEffect(() => {
    setVerificationCode([...new Array(numberOfDigits)].map(() => ''));
    [...new Array(numberOfDigits)].forEach((_, index) => {
      inputRefs.current[index] = createRef<HTMLInputElement>()
    })
  }, [numberOfDigits])

  const focusOnInput = (index: number) => {
    // @ts-ignore
    inputRefs.current[index].current.focus()
  }

  const handleKeyDown = (index: number, e: React.KeyboardEvent<HTMLInputElement>) => {
    console.log(e.key, index)
    let verificationCodeCopy = JSON.parse(JSON.stringify(verificationCode));
    const FORWARD_KEYS = ['ArrowRight', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    const BACK_KEYS = ['ArrowLeft', 'Delete', 'Backspace']
    const APPEND_KEYS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    const DELETE_KEYS = ['Delete', 'Backspace']
    if (DELETE_KEYS.includes(e.key)) {
      verificationCodeCopy[index] = ''
    }
    if (BACK_KEYS.includes(e.key)) {
      if (index - 1 >= 0) {
        focusOnInput(index - 1)
      }
    }
    else if (APPEND_KEYS.includes(e.key)) {
      verificationCodeCopy[index] = e.key
    }
    if (FORWARD_KEYS.includes(e.key)) {
      if (index + 1 < numberOfDigits) {
        focusOnInput(index + 1)
      }
    }
    setVerificationCode(verificationCodeCopy)
  }

  return (
    <div className="CodeVerification">
      {
        verificationCode.map((el, index) => (
          <div className="CodeVerification__Digit" key={index}>
            <input value={el}
                   ref={inputRefs.current[index]}
                   pattern="\d*"
                   onKeyDown={(e) => handleKeyDown(index, e)}
            />
          </div>
        ))
      }
    </div>
  );

};

export default CodeVerificationInput;
