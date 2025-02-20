import React, { useState, useEffect } from 'react';
import { Box, Paper, TextField, Button, Typography } from '@mui/material';
import { CDDCChart } from './CDDCChart';

interface Message {
  text: string;
  sender: 'bot' | 'user';
  timestamp: Date;
}

export const AssessmentChat: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [assessmentData, setAssessmentData] = useState(null);

  useEffect(() => {
    // Start conversation when component mounts
    startAssessment();
  }, []);

  const startAssessment = async () => {
    const response = await fetch('/api/assessment/start', {
      method: 'POST',
      body: JSON.stringify({ age_months: 24 }), // Example age
    });
    const data = await response.json();
    
    setMessages([{
      text: data.message,
      sender: 'bot',
      timestamp: new Date()
    }]);
  };

  const handleSend = async () => {
    if (!input.trim()) return;

    // Add user message
    const userMessage = {
      text: input,
      sender: 'user',
      timestamp: new Date()
    };
    setMessages(prev => [...prev, userMessage]);
    setInput('');

    // Get bot response
    const response = await fetch('/api/assessment/process', {
      method: 'POST',
      body: JSON.stringify({ 
        message: input,
        context: messages[messages.length - 1]
      })
    });
    const data = await response.json();

    // Add bot response
    setMessages(prev => [...prev, {
      text: data.message,
      sender: 'bot',
      timestamp: new Date()
    }]);

    // Update assessment data if available
    if (data.assessmentData) {
      setAssessmentData(data.assessmentData);
    }
  };

  return (
    <Box sx={{ display: 'flex', height: '100vh', p: 2 }}>
      <Box sx={{ flex: 1, mr: 2 }}>
        <Paper sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
          {/* Chat messages */}
          <Box sx={{ flex: 1, overflow: 'auto', p: 2 }}>
            {messages.map((message, index) => (
              <Box
                key={index}
                sx={{
                  display: 'flex',
                  justifyContent: message.sender === 'user' ? 'flex-end' : 'flex-start',
                  mb: 2
                }}
              >
                <Paper
                  sx={{
                    p: 1,
                    backgroundColor: message.sender === 'user' ? 'primary.light' : 'grey.100'
                  }}
                >
                  <Typography>{message.text}</Typography>
                </Paper>
              </Box>
            ))}
          </Box>

          {/* Input area */}
          <Box sx={{ p: 2, borderTop: 1, borderColor: 'grey.300' }}>
            <TextField
              fullWidth
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSend()}
              placeholder="Type your response..."
            />
          </Box>
        </Paper>
      </Box>

      {/* CDDC Chart */}
      <Box sx={{ width: '400px' }}>
        <Paper sx={{ p: 2, height: '100%' }}>
          <Typography variant="h6" gutterBottom>
            Development Progress
          </Typography>
          {assessmentData && <CDDCChart data={assessmentData} />}
        </Paper>
      </Box>
    </Box>
  );
}; 