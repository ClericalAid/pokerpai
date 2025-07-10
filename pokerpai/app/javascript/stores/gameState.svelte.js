// Game state management using Svelte 5 runes
// This acts like a store but uses the new runes API

// Create reactive game state
let gameState = $state({
  game_id: null,
  player_count: 0,
  blinds: [0, 0],
  starting_stacks: [],
  current_stacks: [],
  current_bets: [],
  total_pot_amount: 0,
  actor_index: 0,
  hole_cards: [],
  board: [],
  hand_actions: []
});

// Helper function to parse card notation (e.g., "4h" -> {rank: "4", suit: "h"})
export function parseCard(cardStr) {
  if (!cardStr || cardStr.length < 2) return {rank: '?', suit: ''};

  const suit = cardStr.slice(-1);
  const rank = cardStr.slice(0, -1);

  return {
    rank: rank,
    suit: suit
  };
}

// Helper function to format currency
export function formatCurrency(amount) {
  return `$${amount.toFixed(2)}`;
}

// Get the current game state (reactive)
export function getGameState() {
  return gameState;
}

// Update game state from received data
export function updateGameState(gameData) {
  if (gameData && gameData.game_data && gameData.game_data.game_status) {
    const status = gameData.game_data.game_status;

    gameState.game_id = gameData.game_data.game_id;
    gameState.player_count = status.player_count;
    gameState.blinds = status.blinds;
    gameState.starting_stacks = status.starting_stacks;
    gameState.current_stacks = status.current_stacks;
    gameState.current_bets = status.current_bets;
    gameState.total_pot_amount = status.total_pot_amount;
    gameState.actor_index = status.actor_index;
    gameState.hole_cards = status.hole_cards;
    gameState.board = status.board;
    gameState.hand_actions = status.hand_actions;

    console.log('Game state updated:', gameState);
  }
}

// Helper function to get player data for a specific position
export function getPlayerData(playerIndex) {
  if (playerIndex >= gameState.player_count) {
    return null;
  }

  const stack = gameState.current_stacks[playerIndex];
  const bet = gameState.current_bets[playerIndex];
  const holeCards = gameState.hole_cards[playerIndex] || [];
  const isActor = gameState.actor_index === playerIndex;

  return {
    name: `Player ${playerIndex + 1}`,
    stack: formatCurrency(stack),
    bet: bet > 0 ? formatCurrency(bet) : null,
    cards: holeCards.map(parseCard),
    isActor: isActor,
    folded: false // TODO: Determine from hand_actions
  };
}

// Individual update methods for granular state changes
export function updatePlayerBet(playerIndex, amount) {
  if (playerIndex < gameState.current_bets.length) {
    gameState.current_bets[playerIndex] = amount;
  }
}

export function updatePlayerStack(playerIndex, newStack) {
  if (playerIndex < gameState.current_stacks.length) {
    gameState.current_stacks[playerIndex] = newStack;
  }
}

export function updatePot(newAmount) {
  gameState.total_pot_amount = newAmount;
}

export function setCurrentActor(playerIndex) {
  gameState.actor_index = playerIndex;
}

export function addCommunityCard(card) {
  gameState.board.push(card);
}
