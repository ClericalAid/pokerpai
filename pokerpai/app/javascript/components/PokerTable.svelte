<script>
  import PlayerBox from './PlayerBox.svelte';
  import Pot from './Pot.svelte';
  import CommunityCards from './CommunityCards.svelte';
  import TerminalPrompt from './TerminalPrompt.svelte';
</script>

<div class="w-fit h-full flex flex-col bg-gray-800 rounded-lg border-2 border-gray-700 shadow-xl items-center">
  <!-- Top row - 4 players -->
  <div class="w-fit flex justify-center items-center gap-2 pt-2">
    <div class="relative">
      <PlayerBox
        name="player_1"
        stack="$1,850"
        bet="$100"
        betPosition="bottom-right"
        folded={false}
      />
    </div>
    <div class="relative">
      <PlayerBox
        name="player_2"
        stack="$3,200"
        bet="$250"
        betPosition="bottom"
        folded={false}
      />
    </div>
    <div class="relative">
      <PlayerBox
        name="player_3"
        stack="$980"
        bet="$250"
        betPosition="bottom"
        folded={false}
      />
    </div>
    <div class="relative">
      <PlayerBox
        name="player_4"
        stack="$2,780"
        bet="$150"
        betPosition="bottom-left"
        folded={false}
      />
    </div>
  </div>

  <!-- Middle section with side players and table -->
  <div class="flex w-fit justify-center items-center px-6 py-8">
    <!-- Left side - 2 players -->
    <div class="flex flex-col gap-4 pr-24">
      <div class="relative">
        <PlayerBox
          name="player_5"
          stack="$1,250"
          bet="$200"
          betPosition="right"
          folded={false}
        />
      </div>
      <div class="relative">
        <PlayerBox
          name="player_6"
          stack="$2,100"
          bet="$150"
          betPosition="right"
          folded={false}
        />
      </div>
    </div>

    <!-- Table center with pot and community cards -->
    <div class="w-80 text-center">
      <Pot amount="$1,250" />
      <CommunityCards />
    </div>

    <!-- Right side - 2 players -->
    <div class="flex flex-col gap-4 pl-24">
      <div class="relative">
        <PlayerBox
          name="player_7"
          stack="$4,200"
          bet="$100"
          betPosition="left"
          folded={false}
        />
      </div>
      <div class="relative">
        <PlayerBox
          name="player_8"
          stack="$3,670"
          action="FOLD"
          betPosition="left"
          folded={true}
        />
      </div>
    </div>
  </div>

  <!-- Bottom section with hero and terminal -->
  <div class="w-full flex justify-between items-center pb-2 px-6">
    <div class="flex-1">
      <!-- Spacer -->
    </div>

    <!-- Hero player -->
    <div class="relative z-10">
      <PlayerBox
        name="user@terminal"
        stack="$2,450"
        bet="$100"
        betPosition="top"
        isHero={true}
        cards={[{rank: 'Q', suit: 'h'}, {rank: 'Q', suit: 's'}]}
      />
    </div>

    <div class="flex-1 flex justify-end">
      <!-- Terminal Prompt -->
      <TerminalPrompt
        minBet={250}
        maxBet={2450}
      />
    </div>
  </div>
</div>
