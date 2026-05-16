import React, { useState } from 'react';
import TicketInput from './components/TicketInput';
import AgentCard from './components/AgentCard';
import SpecOutput from './components/SpecOutput';
import './styles/variables.css';
import './App.css';

const AGENTS = [
  {
    slug: 'edge',
    name: 'Edge Case Detective',
    icon: '🔍'
  },
  {
    slug: 'security',
    name: 'Security Analyst',
    icon: '🛡️'
  },
  {
    slug: 'architect',
    name: 'Architect Blueprint',
    icon: '🏗️'
  }
];

function App() {
  const [agentStatuses, setAgentStatuses] = useState({
    edge: 'idle',
    security: 'idle',
    architect: 'idle'
  });
  const [results, setResults] = useState(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const handleAnalyze = async (ticket) => {
    setIsAnalyzing(true);
    setResults(null);
    
    // Activate agents with stagger
    setTimeout(() => setAgentStatuses({ edge: 'active', security: 'idle', architect: 'idle' }), 200);
    setTimeout(() => setAgentStatuses({ edge: 'active', security: 'active', architect: 'idle' }), 400);
    setTimeout(() => setAgentStatuses({ edge: 'active', security: 'active', architect: 'active' }), 600);

    try {
      const response = await fetch('http://localhost:5000/api/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ticket }),
      });

      if (!response.ok) {
        throw new Error('Analysis failed');
      }

      const data = await response.json();
      setResults(data);
      setAgentStatuses({ edge: 'done', security: 'done', architect: 'done' });
    } catch (error) {
      console.error('Error analyzing ticket:', error);
      setAgentStatuses({ edge: 'error', security: 'error', architect: 'error' });
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1 className="logo">BobSpec</h1>
          <div className="header-badge">
            <span className="status-indicator"></span>
            <span>Powered by IBM Bob</span>
          </div>
        </div>
      </header>

      <main className="app-main">
        <TicketInput onAnalyze={handleAnalyze} isAnalyzing={isAnalyzing} />

        <div className="agents-section">
          <div className="agents-grid">
            {AGENTS.map((agent) => (
              <AgentCard
                key={agent.slug}
                agent={agent}
                status={agentStatuses[agent.slug]}
                results={results?.[agent.slug === 'edge' ? 'edge_cases' : agent.slug === 'security' ? 'security' : 'architecture']}
              />
            ))}
          </div>
        </div>

        {results && <SpecOutput results={results} />}
      </main>

      <footer className="app-footer">
        <p>BobSpec — Team Bobsyourdev | IBM Bob Hackathon 2026</p>
      </footer>
    </div>
  );
}

export default App;

// Made with Bob
