import React from 'react';
import './AgentCard.css';

const AgentCard = ({ agent, status, results }) => {
  const getStatusIcon = () => {
    switch (status) {
      case 'idle':
        return '○';
      case 'active':
        return <span className="pulse-dot">◉</span>;
      case 'done':
        return '✓';
      case 'error':
        return '✕';
      default:
        return '○';
    }
  };

  const getStatusClass = () => {
    return `agent-card agent-card--${status} agent-card--${agent.slug}`;
  };

  return (
    <div className={getStatusClass()}>
      <div className="agent-header">
        <span className="agent-icon">{agent.icon}</span>
        <h3 className="agent-title">{agent.name}</h3>
      </div>
      
      <div className="agent-status">
        <span className="status-icon">{getStatusIcon()}</span>
        <span className="status-text">{status.toUpperCase()}</span>
      </div>

      {status === 'active' && (
        <div className="agent-thinking">
          <span>Analyzing</span>
          <span className="dot dot-1">.</span>
          <span className="dot dot-2">.</span>
          <span className="dot dot-3">.</span>
        </div>
      )}

      {status === 'done' && results && (
        <div className="agent-results">
          <div className="results-count">
            {Array.isArray(results) ? results.length : Object.keys(results).length} items found
          </div>
        </div>
      )}

      {status === 'error' && (
        <div className="agent-error">
          Analysis failed
        </div>
      )}
    </div>
  );
};

export default AgentCard;

// Made with Bob
