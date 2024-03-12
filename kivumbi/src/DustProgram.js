import React, { useState } from 'react';

const Main = () => {
  const [gender, setGender] = useState('');
  const [action, setAction] = useState('');
  const [result, setResult] = useState('');

  const handleGenderChange = (e) => {
    setGender(e.target.value);
  };

  const handleActionChange = (e) => {
    setAction(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (gender.toLowerCase() === 'male') {
      setResult(action ? 'Result = Dust' : 'Result = No Dust');
    } else if (gender.toLowerCase() === 'female') {
      setResult(action ? 'Result = No Dust' : 'Result = Dust');
    } else {
      setResult('Invalid gender entered. Please enter either "Male" or "Female".');
    }
  };

  return (
    <div>
      <h1>Dust or No Dust</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Gender:
          <input type="text" value={gender} onChange={handleGenderChange} />
        </label>
        <br />
        <label>
          Action:
          <input type="text" value={action} onChange={handleActionChange} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
      <p>{result}</p>
    </div>
  );
};

export default Main;
