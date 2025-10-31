import React from 'react';
import './PricingModal.css';

function PricingModal({ onClose, onUpgrade }) {
  const plans = [
    {
      name: '?cretsiz',
      price: '?0',
      period: '/ay',
      features: [
        '30 saniyeye kadar m?zik',
        'Temel enstr?manlar',
        'MIDI export',
        'Standart kalite',
        '5 olu?turma/g?n'
      ],
      highlighted: false
    },
    {
      name: 'Premium',
      price: '?99',
      period: '/ay',
      features: [
        '5 dakikaya kadar m?zik',
        'T?m enstr?manlar + Davul',
        'MIDI, WAV, MP3 export',
        'Y?ksek kalite (320kbps)',
        'S?n?rs?z olu?turma',
        '?ncelikli destek',
        'Geli?mi? AI ?zellikleri',
        'Ticari kullan?m haklar?'
      ],
      highlighted: true
    }
  ];

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="close-btn" onClick={onClose}>?</button>
        
        <h2>Planlar? Ke?fet</h2>
        <p className="modal-subtitle">Yarat?c?l???n?z? s?n?rs?zla?t?r?n</p>

        <div className="pricing-grid">
          {plans.map((plan, idx) => (
            <div 
              key={idx}
              className={`pricing-card ${plan.highlighted ? 'highlighted' : ''}`}
            >
              {plan.highlighted && <div className="badge">Pop?ler</div>}
              
              <h3>{plan.name}</h3>
              <div className="price">
                <span className="amount">{plan.price}</span>
                <span className="period">{plan.period}</span>
              </div>

              <ul className="features-list">
                {plan.features.map((feature, fidx) => (
                  <li key={fidx}>
                    <span className="check">?</span>
                    {feature}
                  </li>
                ))}
              </ul>

              <button 
                className={`select-btn ${plan.highlighted ? 'premium' : 'free'}`}
                onClick={() => {
                  if (plan.highlighted) {
                    onUpgrade();
                  }
                }}
              >
                {plan.highlighted ? '?? Premium\'a Ge?' : 'Mevcut Plan'}
              </button>
            </div>
          ))}
        </div>

        <div className="modal-footer">
          <p>? 14 g?n para iade garantisi</p>
          <p>?? G?venli ?deme</p>
          <p>?? ?stedi?in zaman iptal et</p>
        </div>
      </div>
    </div>
  );
}

export default PricingModal;
