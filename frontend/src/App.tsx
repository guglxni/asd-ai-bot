import React from 'react';
import { ThemeProvider, CssBaseline, Container } from '@mui/material';
import { theme } from './theme';
import { AssessmentChat } from './components/AssessmentChat';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="xl" sx={{ height: '100vh', py: 2 }}>
        <AssessmentChat />
      </Container>
    </ThemeProvider>
  );
}

export default App;
