import React, { useState } from 'react';
import './TicketInput.css';

const TicketInput = ({ onAnalyze, isAnalyzing }) => {
  const [ticket, setTicket] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (ticket.trim()) {
      onAnalyze(ticket);
    }
  };

  return (
    <div className="ticket-input-container">
      <h1 className="hero-title">
        Transform your ticket into a complete specification
      </h1>
      <p className="hero-subtitle">
        Powered by IBM watsonx.ai — 3 AI agents working in parallel
      </p>
      
      <form onSubmit={handleSubmit} className="ticket-form">
        <textarea
          className="ticket-textarea"
          placeholder="Paste your development ticket here..."
          value={ticket}
          onChange={(e) => setTicket(e.target.value)}
          disabled={isAnalyzing}
          rows={8}
        />
        
        <button
          type="submit"
          className="analyze-button"
          disabled={isAnalyzing || !ticket.trim()}
        >
          {isAnalyzing ? (
            <>
              <span className="spinner"></span>
              Analyzing...
            </>
          ) : (
            <>
              <span className="play-icon">▶</span>
              Analyze with BobSpec
            </>
          )}
        </button>
      </form>
    </div>
  );
};

export default TicketInput;

// Made with Bob
