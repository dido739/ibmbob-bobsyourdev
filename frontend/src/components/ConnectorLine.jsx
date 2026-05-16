import React from 'react';
import './ConnectorLine.css';

const ConnectorLine = ({ agentStatuses }) => {
  const getLineClass = () => {
    const activeCount = Object.values(agentStatuses).filter(s => s === 'active' || s === 'done').length;
    const allDone = Object.values(agentStatuses).every(s => s === 'done');
    
    if (allDone) return 'connector-line connector-line--complete';
    if (activeCount > 0) return 'connector-line connector-line--active';
    return 'connector-line';
  };

  const getProgressWidth = () => {
    const statuses = Object.values(agentStatuses);
    const doneCount = statuses.filter(s => s === 'done').length;
    return `${(doneCount / 3) * 100}%`;
  };

  return (
    <div className={getLineClass()}>
      <div 
        className="connector-line__progress" 
        style={{ width: getProgressWidth() }}
      />
    </div>
  );
};

export default ConnectorLine;

// Made with Bob