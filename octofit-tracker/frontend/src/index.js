
// Set REACT_APP_CODESPACE_NAME from environment if available
if (!process.env.REACT_APP_CODESPACE_NAME && window.location.hostname.includes('github.dev')) {
  const match = window.location.hostname.match(/^([^-]+)-8000\.app\.github\.dev$/);
  if (match) {
    process.env.REACT_APP_CODESPACE_NAME = match[1];
    console.log('Detected codespace:', process.env.REACT_APP_CODESPACE_NAME);
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
