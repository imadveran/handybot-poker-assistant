import React from 'react';

type Card = { rank: string; suit: string };

type Props = {
  boardCards: Card[];
};

const cardToEmoji = (card: Card) => {
  const suits = { S: '♠', H: '♥', D: '♦', C: '♣' };
  return `${card.rank}${suits[card.suit]}`;
};

const PokerBoard: React.FC<Props> = ({ boardCards }) => (
  <div style={{ display: 'flex', gap: '8px' }}>
    {boardCards.map((card, i) => (
      <div key={i} style={{
        border: '1px solid black',
        borderRadius: '6px',
        padding: '10px',
        fontSize: '20px',
        backgroundColor: 'white',
        width: '40px',
        textAlign: 'center'
      }}>
        {cardToEmoji(card)}
      </div>
    ))}
  </div>
);

export default PokerBoard;
