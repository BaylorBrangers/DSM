const diseases = [
  {
    name: 'Common Cold',
    symptoms: ['Runny nose', 'Sneezing', 'Sore throat'],
    diagnosis: 'Usually based on symptoms and physical examination.',
    treatment: 'Rest, fluids, and over-the-counter medications.'
  },
  {
    name: 'Diabetes',
    symptoms: ['Increased thirst', 'Frequent urination', 'Fatigue'],
    diagnosis: 'Blood sugar testing by a healthcare provider.',
    treatment: 'Lifestyle changes, monitoring, and medication as prescribed.'
  },
  {
    name: 'Influenza',
    symptoms: ['Fever', 'Chills', 'Body aches'],
    diagnosis: 'Rapid influenza diagnostic tests or clinical evaluation.',
    treatment: 'Antiviral medication and supportive care.'
  }
];

function App() {
  const [query, setQuery] = React.useState('');
  const [result, setResult] = React.useState(null);

  const handleSearch = () => {
    const found = diseases.find(d => d.name.toLowerCase() === query.trim().toLowerCase());
    setResult(found ? found : { error: 'Disease not found' });
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Disease Lookup</h1>
      <input
        type="text"
        placeholder="Enter disease name"
        value={query}
        onChange={e => setQuery(e.target.value)}
        style={{ padding: '8px', width: '250px' }}
      />
      <button onClick={handleSearch} style={{ marginLeft: '10px', padding: '8px' }}>
        Search
      </button>
      {result && (
        <div style={{ marginTop: '20px' }}>
          <h2>{result.error ? result.error : result.name}</h2>
          {!result.error && (
            <ul>
              <li><strong>Symptoms:</strong> {result.symptoms.join(', ')}</li>
              <li><strong>Diagnosis:</strong> {result.diagnosis}</li>
              <li><strong>Treatment:</strong> {result.treatment}</li>
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
