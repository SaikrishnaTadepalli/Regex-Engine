# Regex-Engine

This project involves building a Regular Expression (Regex) Engine from scratch, starting with a basic NFA Architecture and gradually adding advanced features such as Lookaheads, Backreferences, and Multithreading support. The main focus is on performance optimization - to create a powerful tool that can handle even the most complex pattern matching tasks with high efficiency.


## Getting Started

[Text Here]

## TimeLine

- Build the basic regex engine using a simple NFA architecture. This enables matching on simple regular expressions.
- Add support for Lookaheads.
- Add support for Lookbehinds.
- Add support for Backreferences.
- Add support for atomic groups.
- Add support for possesive quantifiers.
- Implement multithreading support at the engine level. This divides the input string into smaller chunks and runs the refex engine in parallel on each chunk.
- Implement multithreading support at the pattern level and group level. This divides the regular expression into smaller subexpressions and groups and runs the engine in parallel on each subexpression of group
- Implement benchmarking tools to measure performance of the engine.
- Benchmark Performance and Optimize
