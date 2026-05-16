import React, { useState } from 'react';
import './SpecOutput.css';

const SpecOutput = ({ results }) => {
  const [activeTab, setActiveTab] = useState('edge_cases');

  if (!results) return null;

  const { edge_cases, security, architecture } = results;

  const renderEdgeCases = () => {
    if (!edge_cases?.edge_cases) return <p>No edge cases found</p>;
    
    return (
      <div className="results-list">
        {edge_cases.edge_cases.map((item, index) => (
          <div key={index} className="result-item" style={{ animationDelay: `${index * 80}ms` }}>
            <div className="result-header">
              <span className={`criticality criticality--${item.criticality?.toLowerCase()}`}>
                {item.criticality}
              </span>
            </div>
            <h4 className="result-title">{item.scenario}</h4>
            <p className="result-description">{item.question_for_po}</p>
          </div>
        ))}
      </div>
    );
  };

  const renderSecurity = () => {
    if (!security?.security_risks) return <p>No security risks found</p>;
    
    return (
      <div className="results-list">
        {security.security_risks.map((item, index) => (
          <div key={index} className="result-item" style={{ animationDelay: `${index * 80}ms` }}>
            <div className="result-header">
              <span className={`risk-level risk-level--${item.risk_level?.toLowerCase()}`}>
                {item.risk_level}
              </span>
              <span className="standard-badge">{item.standard}</span>
            </div>
            <h4 className="result-title">{item.vulnerability}</h4>
            <p className="result-description">{item.mitigation}</p>
          </div>
        ))}
      </div>
    );
  };

  const renderArchitecture = () => {
    if (!architecture?.architecture) return <p>No architecture found</p>;
    
    const arch = architecture.architecture;
    
    return (
      <div className="architecture-content">
        <div className="complexity-badge-container">
          <span className={`complexity-badge complexity-badge--${arch.complexity?.toLowerCase()}`}>
            {arch.complexity}
          </span>
          <span className="estimated-days">{arch.estimated_days} days</span>
        </div>

        <div className="architecture-section">
          <h4>Components</h4>
          <ul className="component-list">
            {arch.components?.map((comp, index) => (
              <li key={index}>{comp}</li>
            ))}
          </ul>
        </div>

        <div className="architecture-section">
          <h4>API Endpoints</h4>
          <ul className="endpoint-list">
            {arch.endpoints?.map((endpoint, index) => (
              <li key={index}><code>{endpoint}</code></li>
            ))}
          </ul>
        </div>

        <div className="architecture-section">
          <h4>Implementation Order</h4>
          <ol className="implementation-list">
            {arch.implementation_order?.map((step, index) => (
              <li key={index}>{step}</li>
            ))}
          </ol>
        </div>
      </div>
    );
  };

  return (
    <div className="spec-output">
      <div className="spec-header">
        <h2>📋 Complete Specification</h2>
      </div>

      <div className="spec-tabs">
        <button
          className={`tab ${activeTab === 'edge_cases' ? 'tab--active' : ''}`}
          onClick={() => setActiveTab('edge_cases')}
        >
          Edge Cases
        </button>
        <button
          className={`tab ${activeTab === 'security' ? 'tab--active' : ''}`}
          onClick={() => setActiveTab('security')}
        >
          Security
        </button>
        <button
          className={`tab ${activeTab === 'architecture' ? 'tab--active' : ''}`}
          onClick={() => setActiveTab('architecture')}
        >
          Architecture
        </button>
      </div>

      <div className="spec-content">
        {activeTab === 'edge_cases' && renderEdgeCases()}
        {activeTab === 'security' && renderSecurity()}
        {activeTab === 'architecture' && renderArchitecture()}
      </div>
    </div>
  );
};

export default SpecOutput;

// Made with Bob
