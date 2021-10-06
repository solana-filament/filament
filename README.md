# Ignition_Project


Scaffolding for a dapp built on Solana

Quickstart

git clone https://github.com/solana-labs/dapp-scaffold.git

cd dapp-scaffold

yarn 

yarn start

Environment Setup

Install Rust from https://rustup.rs/

Install Solana v1.6.7 or later from https://docs.solana.com/cli/install-solana-cli-tools#use-solanas-install-tool

Install Node

Install NPM, Yarn

Build Smart Contract (compiled for BPF)

Run the following from the program/ subdirectory:

$ cargo build-bpf

$ cargo test-bpf

Directory structure

program

Solana program template in Rust

program/src/lib.rs

process_instruction function is used to run all calls issued to the smart contract

src/actions

Setup here actions that will interact with Solana programs using sendTransaction function

src/contexts

React context objects that are used propagate state of accounts across the application

src/hooks

Generic react hooks to interact with token program:

useUserBalance - query for balance of any user token by mint, returns:

balance

balanceLamports

balanceInUSD

useUserTotalBalance - aggregates user balance across all token accounts and returns value in USD

balanceInUSD

useAccountByMint

useTokenName

useUserAccounts

src/views

home - main page for your app

faucet - airdrops SOL on Testnet and Devnet
