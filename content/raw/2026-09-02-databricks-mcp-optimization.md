# How we eliminated $1 million a year of wasted AI agent ...

**Source URL:** https://www.databricks.com/blog/how-we-eliminated-1-million-year-wasted-ai-agent-spend-one-hour

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyIiBoZWlnaHQ9IjIyIiB2aWV3Qm94PSIwIDAgMTMyIDIyIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im0xOC4zMTggOS4yNzUtOC42MzEgNC44NTlMLjQ0NSA4Ljk0MiAwIDkuMTgydjMuNzdsOS42ODcgNS40MzEgOC42My00Ljg0djEuOTk1bC04LjYzIDQuODYtOS4yNDItNS4xOTItLjQ0NS4yNHYuNjQ2bDkuNjg3IDUuNDMyIDkuNjY4LTUuNDMydi0zLjc2OWwtLjQ0NS0uMjQtOS4yMjMgNS4xNzMtOC42NS00Ljg0VjEwLjQybDguNjUgNC44NCA5LjY2OC01LjQzVjYuMTE0bC0uNDgyLS4yNzctOS4xODYgNS4xNTVMMS40ODIgNi40MWw4LjIwNS00LjYgNi43NDEgMy43ODcuNTkzLS4zMzJ2LS40NjJMOS42ODcuNjg0IDAgNi4xMTV2LjU5Mmw5LjY4NyA1LjQzMiA4LjYzLTQuODZ6IiBmaWxsPSIjRUUzRDJDIi8+PHBhdGggZD0iTTM3LjQ0OSAxOC40NDNWMS44NTJoLTIuNTU2djYuMjA3YzAgLjA5My0uMDU2LjE2Ny0uMTQ4LjIwNGEuMjMuMjMgMCAwIDEtLjI0LS4wNTZjLS44NzEtMS4wMTYtMi4yMjMtMS41ODktMy43MDUtMS41ODktMy4xNjcgMC01LjY1IDIuNjYtNS42NSA2LjA2IDAgMS42NjMuNTc1IDMuMTk3IDEuNjMgNC4zMjRhNS40NCA1LjQ0IDAgMCAwIDQuMDIgMS43MzZjMS40NjMgMCAyLjgxNS0uNjEgMy43MDQtMS42NjIuMDU2LS4wNzQuMTY3LS4wOTMuMjQtLjA3NC4wOTMuMDM3LjE1LjExLjE1LjIwM3YxLjIzOHptLTYuMDkzLTIuMDE0Yy0yLjAzOCAwLTMuNjMtMS42NDQtMy42My0zLjc1IDAtMi4xMDcgMS41OTItMy43NTEgMy42My0zLjc1MXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NW0xOS43NjIgMi4wMTZWNi44OTZoLTIuNTM3VjguMDZjMCAuMDkzLS4wNTYuMTY2LS4xNDkuMjAzYS4yLjIgMCAwIDEtLjI0LS4wNzNjLS44NTItMS4wMTctMi4xODYtMS41OS0zLjcwNS0xLjU5LTMuMTY3IDAtNS42NDkgMi42NjEtNS42NDkgNi4wNiAwIDMuNCAyLjQ4MiA2LjA2IDUuNjUgNi4wNiAxLjQ2MyAwIDIuODE1LS42MSAzLjcwNC0xLjY4LjA1NS0uMDc1LjE2Ni0uMDkzLjI0LS4wNzUuMDkzLjAzNy4xNDkuMTExLjE0OS4yMDR2MS4yNTZoMi41Mzd6bS02LjA1Ni0yLjAxNGMtMi4wMzggMC0zLjYzLTEuNjQ1LTMuNjMtMy43NSAwLTIuMTA3IDEuNTkyLTMuNzUxIDMuNjMtMy43NTFzMy42MyAxLjY0NCAzLjYzIDMuNzUtMS41OTMgMy43NS0zLjYzIDMuNzVtMjcuNzgxIDIuMDE1VjYuODk2aC0yLjUzOFY4LjA2YzAgLjA5My0uMDU1LjE2Ni0uMTQ4LjIwM3MtLjE4NSAwLS4yNC0uMDczYy0uODUzLTEuMDE3LTIuMTg2LTEuNTktMy43MDUtMS41OS0zLjE4NiAwLTUuNjQ5IDIuNjYxLTUuNjQ5IDYuMDggMCAzLjQxNyAyLjQ4MiA2LjA2IDUuNjQ5IDYuMDYgMS40NjMgMCAyLjgxNS0uNjEgMy43MDQtMS42ODIuMDU2LS4wNzQuMTY3LS4wOTMuMjQxLS4wNzQuMDkzLjAzNy4xNDguMTEuMTQ4LjIwM3YxLjI1NnptLTYuMDU3LTIuMDE0Yy0yLjAzNyAwLTMuNjMtMS42NDUtMy42My0zLjc1IDAtMi4xMDcgMS41OTMtMy43NTEgMy42My0zLjc1MXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NW0xMC43MDYuNjQ3Yy4wMTkgMCAuMDU2LS4wMTkuMDc0LS4wMTkuMDU2IDAgLjEzLjAzNy4xNjcuMDc0Ljg3IDEuMDE2IDIuMjIyIDEuNTg5IDMuNzA0IDEuNTg5IDMuMTY3IDAgNS42NS0yLjY2IDUuNjUtNi4wNiAwLTEuNjYzLS41NzUtMy4xOTYtMS42My00LjMyM2E1LjQ0IDUuNDQgMCAwIDAtNC4wMi0xLjczN2MtMS40NjMgMC0yLjgxNS42MS0zLjcwNCAxLjY2My0uMDU2LjA3NC0uMTQ4LjA5Mi0uMjQuMDc0LS4wOTMtLjAzNy0uMTQ5LS4xMTEtLjE0OS0uMjA0VjEuODUyaC0yLjU1NnYxNi41OWgyLjU1NlYxNy4yOGMwLS4wOTMuMDU2LS4xNjYuMTQ4LS4yMDNtLS4yNi00LjM5OGMwLTIuMTA2IDEuNTk0LTMuNzUgMy42MzEtMy43NXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NS0zLjYzLTEuNjYyLTMuNjMtMy43NW0xNy4yNDQtMy40MTZjLjI0IDAgLjQ2My4wMTkuNjEuMDU2VjYuNjk1YTIuNCAyLjQgMCAwIDAtLjQyNS0uMDM3Yy0xLjMzNCAwLTIuNTU2LjY4NC0zLjIwNCAxLjc3NC0uMDU2LjA5Mi0uMTQ5LjEzLS4yNDEuMDkyYS4yMi4yMiAwIDAgMS0uMTY3LS4yMDNWNi44OThoLTIuNTM3djExLjU2NmgyLjU1NnYtNS4xYzAtMi41MyAxLjI5Ni00LjEgMy40MDgtNC4xbTQuODE1LTIuMzY3aC0yLjU5M3YxMS41NjZoMi41OTN6TTk3Ljk1OCAxLjg3YTEuNTcxIDEuNTcxIDAgMSAwIDAgMy4xNDEgMS41NzEgMS41NzEgMCAxIDAgMC0zLjE0bTguOTI4IDQuNzI5Yy0zLjU1NiAwLTYuMTMxIDIuNTUtNi4xMzEgNi4wOCAwIDEuNzE3LjYxMiAzLjI1IDEuNzA0IDQuMzYgMS4xMTIgMS4xMDggMi42NjcgMS43MTggNC40MDggMS43MTggMS40NDUgMCAyLjU1Ni0uMjc3IDQuNjY4LTEuODNsLTEuNDYzLTEuNTMzYy0xLjAzOC42ODQtMi4wMDEgMS4wMTYtMi45NDUgMS4wMTYtMi4xNDkgMC0zLjc2LTEuNjA3LTMuNzYtMy43MzJzMS42MTEtMy43MzIgMy43Ni0zLjczMmMxLjAxOCAwIDEuOTYzLjMzMyAyLjkwOCAxLjAxNmwxLjYyOS0xLjUzM2MtMS45MDctMS42MjYtMy42My0xLjgzLTQuNzc4LTEuODNtOS4xNDkgNi43NjJhLjIuMiAwIDAgMSAuMTQ5LS4wNTVoLjAxOGMuMDU2IDAgLjExMS4wMzcuMTY3LjA3M2w0LjA5MyA1LjA2M2gzLjE0OWwtNS4yOTctNi4zOTNjLS4wNzUtLjA5Mi0uMDc1LS4yMjIuMDE4LS4yOTVsNC44NzEtNC44NmgtMy4xM2wtNC4yMDQgNC4yMTNjLS4wNTYuMDU1LS4xNDguMDc0LS4yNDEuMDU1YS4yMy4yMyAwIDAgMS0uMTMtLjIwM1YxLjg3aC0yLjU3NHYxNi41OTFoMi41NTZ2LTQuNTA4YzAtLjA1NS4wMTgtLjEzLjA3NC0uMTY2eiIgZmlsbD0iIzAwMCIvPjxwYXRoIGQ9Ik0xMjcuNzc2IDE4LjczOWMyLjA5MyAwIDQuMjIzLTEuMjc1IDQuMjIzLTMuNjk1IDAtMS41ODktMS0yLjY4LTMuMDM3LTMuMzQ0bC0xLjM5LS40NjJjLS45NDQtLjMxNC0xLjM4OS0uNzU4LTEuMzg5LTEuMzY3IDAtLjcwMi42My0xLjE4MyAxLjUxOS0xLjE4My44NTIgMCAxLjYxMS41NTUgMi4wOTMgMS41MTVsMi4wNTYtMS4xMDhjLS43NTktMS41NTItMi4zMzQtMi41MTMtNC4xNDktMi41MTMtMi4yOTcgMC0zLjk2MyAxLjQ3OC0zLjk2MyAzLjQ5MiAwIDEuNjA3Ljk2MyAyLjY3OSAyLjk0NCAzLjMwN2wxLjQyNy40NjJjMSAuMzE0IDEuNDI2LjcyIDEuNDI2IDEuMzY3IDAgLjk4LS45MDggMS4zMy0xLjY4NiAxLjMzLTEuMDM3IDAtMS45NjMtLjY2NS0yLjQwNy0xLjc1NWwtMi4wOTMgMS4xMDljLjY4NSAxLjc1NSAyLjM3IDIuODQ1IDQuNDI2IDIuODQ1bS02OS41NDYtLjExMWMuODE1IDAgMS41MzgtLjA3NCAxLjk0NS0uMTN2LTIuMjE2YTE0IDE0IDAgMCAxLTEuMjc4LjA3M2MtMS4wMzcgMC0xLjgzMy0uMTg0LTEuODMzLTIuNDJWOS4xODdjMC0uMTMuMDkyLS4yMjIuMjIyLS4yMjJoMi41VjYuODc3aC0yLjVhLjIxNC4yMTQgMCAwIDEtLjIyMi0uMjIxVjMuMzNoLTIuNTU2djMuMzQ0YzAgLjEzLS4wOTMuMjIyLS4yMjMuMjIyaC0xLjc3OHYyLjA4OGgxLjc3OGMuMTMgMCAuMjIzLjA5Mi4yMjMuMjIxdjUuMzc3YzAgNC4wNDYgMi43MDQgNC4wNDYgMy43MjIgNC4wNDYiIGZpbGw9IiMwMDAiLz48L3N2Zz4=)
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMyIiBoZWlnaHQ9IjIyIiB2aWV3Qm94PSIwIDAgMTMyIDIyIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im0xOC4zMTggOS4yNzUtOC42MzEgNC44NTlMLjQ0NSA4Ljk0MiAwIDkuMTgydjMuNzdsOS42ODcgNS40MzEgOC42My00Ljg0djEuOTk1bC04LjYzIDQuODYtOS4yNDItNS4xOTItLjQ0NS4yNHYuNjQ2bDkuNjg3IDUuNDMyIDkuNjY4LTUuNDMydi0zLjc2OWwtLjQ0NS0uMjQtOS4yMjMgNS4xNzMtOC42NS00Ljg0VjEwLjQybDguNjUgNC44NCA5LjY2OC01LjQzVjYuMTE0bC0uNDgyLS4yNzctOS4xODYgNS4xNTVMMS40ODIgNi40MWw4LjIwNS00LjYgNi43NDEgMy43ODcuNTkzLS4zMzJ2LS40NjJMOS42ODcuNjg0IDAgNi4xMTV2LjU5Mmw5LjY4NyA1LjQzMiA4LjYzLTQuODZ6IiBmaWxsPSIjRUUzRDJDIi8+PHBhdGggZD0iTTM3LjQ0OSAxOC40NDNWMS44NTJoLTIuNTU2djYuMjA3YzAgLjA5My0uMDU2LjE2Ny0uMTQ4LjIwNGEuMjMuMjMgMCAwIDEtLjI0LS4wNTZjLS44NzEtMS4wMTYtMi4yMjMtMS41ODktMy43MDUtMS41ODktMy4xNjcgMC01LjY1IDIuNjYtNS42NSA2LjA2IDAgMS42NjMuNTc1IDMuMTk3IDEuNjMgNC4zMjRhNS40NCA1LjQ0IDAgMCAwIDQuMDIgMS43MzZjMS40NjMgMCAyLjgxNS0uNjEgMy43MDQtMS42NjIuMDU2LS4wNzQuMTY3LS4wOTMuMjQtLjA3NC4wOTMuMDM3LjE1LjExLjE1LjIwM3YxLjIzOHptLTYuMDkzLTIuMDE0Yy0yLjAzOCAwLTMuNjMtMS42NDQtMy42My0zLjc1IDAtMi4xMDcgMS41OTItMy43NTEgMy42My0zLjc1MXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NW0xOS43NjIgMi4wMTZWNi44OTZoLTIuNTM3VjguMDZjMCAuMDkzLS4wNTYuMTY2LS4xNDkuMjAzYS4yLjIgMCAwIDEtLjI0LS4wNzNjLS44NTItMS4wMTctMi4xODYtMS41OS0zLjcwNS0xLjU5LTMuMTY3IDAtNS42NDkgMi42NjEtNS42NDkgNi4wNiAwIDMuNCAyLjQ4MiA2LjA2IDUuNjUgNi4wNiAxLjQ2MyAwIDIuODE1LS42MSAzLjcwNC0xLjY4LjA1NS0uMDc1LjE2Ni0uMDkzLjI0LS4wNzUuMDkzLjAzNy4xNDkuMTExLjE0OS4yMDR2MS4yNTZoMi41Mzd6bS02LjA1Ni0yLjAxNGMtMi4wMzggMC0zLjYzLTEuNjQ1LTMuNjMtMy43NSAwLTIuMTA3IDEuNTkyLTMuNzUxIDMuNjMtMy43NTFzMy42MyAxLjY0NCAzLjYzIDMuNzUtMS41OTMgMy43NS0zLjYzIDMuNzVtMjcuNzgxIDIuMDE1VjYuODk2aC0yLjUzOFY4LjA2YzAgLjA5My0uMDU1LjE2Ni0uMTQ4LjIwM3MtLjE4NSAwLS4yNC0uMDczYy0uODUzLTEuMDE3LTIuMTg2LTEuNTktMy43MDUtMS41OS0zLjE4NiAwLTUuNjQ5IDIuNjYxLTUuNjQ5IDYuMDggMCAzLjQxNyAyLjQ4MiA2LjA2IDUuNjQ5IDYuMDYgMS40NjMgMCAyLjgxNS0uNjEgMy43MDQtMS42ODIuMDU2LS4wNzQuMTY3LS4wOTMuMjQxLS4wNzQuMDkzLjAzNy4xNDguMTEuMTQ4LjIwM3YxLjI1NnptLTYuMDU3LTIuMDE0Yy0yLjAzNyAwLTMuNjMtMS42NDUtMy42My0zLjc1IDAtMi4xMDcgMS41OTMtMy43NTEgMy42My0zLjc1MXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NW0xMC43MDYuNjQ3Yy4wMTkgMCAuMDU2LS4wMTkuMDc0LS4wMTkuMDU2IDAgLjEzLjAzNy4xNjcuMDc0Ljg3IDEuMDE2IDIuMjIyIDEuNTg5IDMuNzA0IDEuNTg5IDMuMTY3IDAgNS42NS0yLjY2IDUuNjUtNi4wNiAwLTEuNjYzLS41NzUtMy4xOTYtMS42My00LjMyM2E1LjQ0IDUuNDQgMCAwIDAtNC4wMi0xLjczN2MtMS40NjMgMC0yLjgxNS42MS0zLjcwNCAxLjY2My0uMDU2LjA3NC0uMTQ4LjA5Mi0uMjQuMDc0LS4wOTMtLjAzNy0uMTQ5LS4xMTEtLjE0OS0uMjA0VjEuODUyaC0yLjU1NnYxNi41OWgyLjU1NlYxNy4yOGMwLS4wOTMuMDU2LS4xNjYuMTQ4LS4yMDNtLS4yNi00LjM5OGMwLTIuMTA2IDEuNTk0LTMuNzUgMy42MzEtMy43NXMzLjYzIDEuNjQ0IDMuNjMgMy43NS0xLjU5MyAzLjc1LTMuNjMgMy43NS0zLjYzLTEuNjYyLTMuNjMtMy43NW0xNy4yNDQtMy40MTZjLjI0IDAgLjQ2My4wMTkuNjEuMDU2VjYuNjk1YTIuNCAyLjQgMCAwIDAtLjQyNS0uMDM3Yy0xLjMzNCAwLTIuNTU2LjY4NC0zLjIwNCAxLjc3NC0uMDU2LjA5Mi0uMTQ5LjEzLS4yNDEuMDkyYS4yMi4yMiAwIDAgMS0uMTY3LS4yMDNWNi44OThoLTIuNTM3djExLjU2NmgyLjU1NnYtNS4xYzAtMi41MyAxLjI5Ni00LjEgMy40MDgtNC4xbTQuODE1LTIuMzY3aC0yLjU5M3YxMS41NjZoMi41OTN6TTk3Ljk1OCAxLjg3YTEuNTcxIDEuNTcxIDAgMSAwIDAgMy4xNDEgMS41NzEgMS41NzEgMCAxIDAgMC0zLjE0bTguOTI4IDQuNzI5Yy0zLjU1NiAwLTYuMTMxIDIuNTUtNi4xMzEgNi4wOCAwIDEuNzE3LjYxMiAzLjI1IDEuNzA0IDQuMzYgMS4xMTIgMS4xMDggMi42NjcgMS43MTggNC40MDggMS43MTggMS40NDUgMCAyLjU1Ni0uMjc3IDQuNjY4LTEuODNsLTEuNDYzLTEuNTMzYy0xLjAzOC42ODQtMi4wMDEgMS4wMTYtMi45NDUgMS4wMTYtMi4xNDkgMC0zLjc2LTEuNjA3LTMuNzYtMy43MzJzMS42MTEtMy43MzIgMy43Ni0zLjczMmMxLjAxOCAwIDEuOTYzLjMzMyAyLjkwOCAxLjAxNmwxLjYyOS0xLjUzM2MtMS45MDctMS42MjYtMy42My0xLjgzLTQuNzc4LTEuODNtOS4xNDkgNi43NjJhLjIuMiAwIDAgMSAuMTQ5LS4wNTVoLjAxOGMuMDU2IDAgLjExMS4wMzcuMTY3LjA3M2w0LjA5MyA1LjA2M2gzLjE0OWwtNS4yOTctNi4zOTNjLS4wNzUtLjA5Mi0uMDc1LS4yMjIuMDE4LS4yOTVsNC44NzEtNC44NmgtMy4xM2wtNC4yMDQgNC4yMTNjLS4wNTYuMDU1LS4xNDguMDc0LS4yNDEuMDU1YS4yMy4yMyAwIDAgMS0uMTMtLjIwM1YxLjg3aC0yLjU3NHYxNi41OTFoMi41NTZ2LTQuNTA4YzAtLjA1NS4wMTgtLjEzLjA3NC0uMTY2eiIgZmlsbD0iIzAwMCIvPjxwYXRoIGQ9Ik0xMjcuNzc2IDE4LjczOWMyLjA5MyAwIDQuMjIzLTEuMjc1IDQuMjIzLTMuNjk1IDAtMS41ODktMS0yLjY4LTMuMDM3LTMuMzQ0bC0xLjM5LS40NjJjLS45NDQtLjMxNC0xLjM4OS0uNzU4LTEuMzg5LTEuMzY3IDAtLjcwMi42My0xLjE4MyAxLjUxOS0xLjE4My44NTIgMCAxLjYxMS41NTUgMi4wOTMgMS41MTVsMi4wNTYtMS4xMDhjLS43NTktMS41NTItMi4zMzQtMi41MTMtNC4xNDktMi41MTMtMi4yOTcgMC0zLjk2MyAxLjQ3OC0zLjk2MyAzLjQ5MiAwIDEuNjA3Ljk2MyAyLjY3OSAyLjk0NCAzLjMwN2wxLjQyNy40NjJjMSAuMzE0IDEuNDI2LjcyIDEuNDI2IDEuMzY3IDAgLjk4LS45MDggMS4zMy0xLjY4NiAxLjMzLTEuMDM3IDAtMS45NjMtLjY2NS0yLjQwNy0xLjc1NWwtMi4wOTMgMS4xMDljLjY4NSAxLjc1NSAyLjM3IDIuODQ1IDQuNDI2IDIuODQ1bS02OS41NDYtLjExMWMuODE1IDAgMS41MzgtLjA3NCAxLjk0NS0uMTN2LTIuMjE2YTE0IDE0IDAgMCAxLTEuMjc4LjA3M2MtMS4wMzcgMC0xLjgzMy0uMTg0LTEuODMzLTIuNDJWOS4xODdjMC0uMTMuMDkyLS4yMjIuMjIyLS4yMjJoMi41VjYuODc3aC0yLjVhLjIxNC4yMTQgMCAwIDEtLjIyMi0uMjIxVjMuMzNoLTIuNTU2djMuMzQ0YzAgLjEzLS4wOTMuMjIyLS4yMjMuMjIyaC0xLjc3OHYyLjA4OGgxLjc3OGMuMTMgMCAuMjIzLjA5Mi4yMjMuMjIxdjUuMzc3YzAgNC4wNDYgMi43MDQgNC4wNDYgMy43MjIgNC4wNDYiIGZpbGw9IiMwMDAiLz48L3N2Zz4=)

# How we eliminated $1 million a year of wasted AI agent spend in one hour

Unity Gateway tracing plus Genie One turned our agents' tool failures into a ranked, fixable bug list, helping us identify and eliminate an estimated $1.2 million a year in wasted AI spend and lost productivity.

by [Alkis Polyzotis](/blog/author/alkis-polyzotis)

• Broken MCP tool calls silently cost real money. Across our agent fleet, seven small MCP-server bugs burned ~$499K/year in tokens and 12,000 eng-hours/year ($1.2M lost) because agents quietly retry instead of surfacing failures.  
• Observe, then fix. Unity Gateway traces every MCP tool call, while Genie One lets teams surface the biggest sources of wasted AI spent using natural language. Our coding agents shipped the fixes in one hour from start to finish.  
• Design tools for how LLMs actually use them. Models make guesses on ambiguous inputs, so tools should handle variations gracefully rather than crash on unexpected inputs.

Databricks engineers rely heavily on AI agents to streamline and accelerate their work. In turn, these agents require access not only to different Foundation Models but also to MCP servers with tools that enable access to relevant artifacts (e.g., system logs, usage tables, support tickets, wikis). In a [previous blog](https://www.databricks.com/blog/managing-ai-coding-costs-scale), we shared that managing AI costs at scale requires optimizing not only model selection but also how agents use tools. In this post, we describe how we looked for cost savings in our agents' use of tools, the challenges we hit along the way, and how OTel tracing in Unity Gateway cut the path from analysis to $1.2M/year in savings to a single hour.

Enabling our developers to build their agents was a huge unlock on productivity, but as usage ramped up, we also faced increasing costs. We started investigating several optimizations, and one suspicion that we had was the hidden cost of failing tool calls. Specifically, when tools misbehave, the calling agent rarely fails loudly. Instead, it retries, guesses, and eventually works around the problem, quietly burning tokens and developer time the whole way. This type of waste is dangerous: from the outside, the task still completes, and an aggregate cost dashboard may show a 10% bump in token spend that can be easily misinterpreted as usage growth. 

We investigated this suspicion in our agent fleet using Unity Gateway's [tracing](https://docs.databricks.com/aws/en/ai-gateway/unified-trace-table) and [Genie One](https://www.databricks.com/product/genie/one). We found seven small bugs in our tool servers that were costing an estimated **$499K/year in wasted tokens** and about 12,000 engineering hours per year in agent wait time. Overall, this is an estimated **$1.2M/year** in lost productivity. 

Finding all seven bugs, quantifying them, and fixing them took about an hour. This post describes the process we followed and what it taught us about building tools for agents.

## How to monitor AI agent and MCP activity

When we first deployed AI agents widely at Databricks for coding and internal workflows, it was impossible to manage or even fully understand costs because we lacked visibility into the agents’ tool calls and overall activity. To solve this, we leveraged Unity Gateway, which automatically emits an OpenTelemetry trace for all MCP tool invocations, including the tool name, arguments, error (if any), token counts, latency, and a session ID that ties calls together. Those traces land in a single table that records exactly what our agents did over any time window. No new instrumentation was required, and the gateway already sits on the path of every call, so the data was readily available.

![](https://www.databricks.com/sites/default/files/inline-images/image1_123.png?v=1788292106)

This makes AI agent cost management more actionable, where instead of seeing only aggregate token spend, we can attribute wasted spend to specific tools, errors, and agent sessions.

Now that the data is available, the next step is exploration:

Normally, the expensive part of this kind of analysis is the SQL and the schema spelunking. But with Genie One, we just pointed it at the trace table, **asked these exact questions in plain English**, and got answers back in minutes. Most of our hour went to reading those answers rather than writing queries.

## What the traces revealed: How MCP tool failures drive up AI agent costs

Genie One turned a vague suspicion ("agents seem to thrash on Jira calls") into a ranked, quantified bug list in minutes. Here is an example from a single 24-hour window, showing bugs in our Jira and Google Drive/Docs tool servers:

|                                              |            |                   |                  |             |
| -------------------------------------------- | ---------- | ----------------- | ---------------- | ----------- |
| Bug                                          | Errors/day | Annual token cost | Annual wait time | Repeat rate |
| Jira: KeyError: 'fields' (get)               | 137        | $250K             | 2,500 h          | ~30%        |
| Jira: 'list' object has no attribute 'split' | 535        | $87K              | 4,850 h          | 30.5%       |
| Jira: KeyError: 'fields' (search)            | 32         | $58K              | 580 h            | ~30%        |
| GDrive: Invalid field selection              | 417        | $46K              | 2,740 h          | 54.5%       |
| Jira: unexpected analysis_prompt kwarg       | 121        | $42K              | 840 h            | 50.0%       |
| GDocs: find_text required                    | 137        | $15K              | 440 h            | 14.3%       |
| Jira: quote_from_bytes() expected bytes      | 30         | $1.2K             | 73 h             | 66.7%       |
| **Total**                                    | **1,409**  | **$499K**         | **12,023 h**     | n/a         |

Bug

Errors/day

Annual token cost

Annual wait time

Repeat rate

Jira: KeyError: 'fields' (get)

137

$250K

2,500 h

~30%

Jira: 'list' object has no attribute 'split'

535

$87K

4,850 h

30.5%

Jira: KeyError: 'fields' (search)

32

$58K

580 h

~30%

GDrive: Invalid field selection

417

$46K

2,740 h

54.5%

Jira: unexpected analysis_prompt kwarg

121

$42K

840 h

50.0%

GDocs: find_text required

137

$15K

440 h

14.3%

Jira: quote_from_bytes() expected bytes

30

$1.2K

73 h

66.7%

**Total**

**1,409**

**$499K**

**12,023 h**

n/a

Take the highest-volume bug, 535 failures a day, as an example. The Jira issues.search tool takes a fields parameter, and the server did this:

It expected a comma-separated string like "key,summary,status". But an array is the semantically natural JSON type for "a list of fields," and that is what the model inferred from its background knowledge of JSON conventions and from adjacent tool calls in the same session. So it passed the structured value that a reasonable caller would:

A list has no .split(), so the server raised 'list' object has no attribute 'split', a raw Python traceback that tells the agent nothing about what it did wrong. So the agent guessed again. Sometimes it retried the same list and failed the same way; sometimes it re-read the schema or fell back to trial and error. On average, it took **12 turns** to recover, and 30% of sessions hit the error more than once. One .split() call was costing an estimated $87K/year in tokens and 4,850 hours of agent wait time.

The Google Drive Invalid field selection error was even more striking in volume: **49.6% of all**drive_file_get **calls failed**, because the model kept passing valid-looking Drive API field names (id, name, mimeType) that the tool's endpoint did not accept.

## The real lesson: How to design MCP tools for AI agents and LLMs

The obvious takeaway is "write better error messages," and the data backs it up. Recovery cost tracks error-message quality almost perfectly:

|                       |                                                 |             |                      |
| --------------------- | ----------------------------------------------- | ----------- | -------------------- |
| Error message quality | Example                                         | Repeat rate | Avg turns to recover |
| Self-documenting      | "find_text and replace_text required"           | 14%         | 4.6                  |
| Somewhat informative  | "Missing required parameters: org, repo"        | ~30%        | 4                    |
| Cryptic traceback     | "'list' object has no attribute 'split'"        | 30.5%       | 12.1                 |
| Misleading            | "unexpected keyword argument 'analysis_prompt'" | 50%         | 13.1                 |

Error message quality

Example

Repeat rate

Avg turns to recover

Self-documenting

"find_text and replace_text required"

14%

4.6

Somewhat informative

"Missing required parameters: org, repo"

~30%

4

Cryptic traceback

"'list' object has no attribute 'split'"

30.5%

12.1

Misleading

"unexpected keyword argument 'analysis_prompt'"

50%

13.1

But "good error messages help" is old news. The more interesting question is *why* the model called these tools "wrong" in the first place. In most of these cases, it didn't.

MCP tool signatures are often deliberately under-specified. We keep them loose on purpose: partly for generality, and partly to save context tokens, since every parameter description costs tokens the model pays for on every call. The consequence is that when a signature is vague about fields, the model fills the gap with a reasonable guess, and a JSON array is a reasonable guess for a list of fields. The bug was not that the model called the tool incorrectly. It was that the server accepted only one of several reasonable interpretations and crashed on the rest.

So the design principle is the reverse of the reflexive one: **tools for agents should adapt to the way LLMs naturally call them,** e.g., coerce the list into a string, default the omitted parameter, absorb the unexpected argument, and so on. An under-specified signature is a promise of flexibility, and the tool should honor that promise on the receiving end rather than crash on the first input that doesn't match the one shape its author had in mind.

## The easy part: How we reduced wasted AI agent spend in one hour

The fixes themselves were simple and are not the interesting part of this story. Once Genie One had handed us a ranked list of which errors to fix and what the model was actually sending, applying the fixes across the tool servers was a quick pass with a coding agent. The whole loop (find, quantify, fix) took about an hour.

The scarce, expensive step was never writing the fix. It was knowing what to fix. Tracing plus Genie One turned that step from a research project into a question you can ask out loud.

## Closing the loop: How to continuously monitor and reduce AI agent costs

As more real work shifts onto agents, silent tool failures become a first-class cost center, the kind that hides inside "usage growth" and never pages anyone. The loop for catching them is cheap and repeatable: Unity Gateway makes agent behavior observable, and Genie One makes that behavior queryable without SQL.

Together, this gives teams a repeatable way to monitor AI agents, diagnose MCP tool failures, and reduce wasted AI spend. If you run agents against your own tools, do the same. Trace the calls and ask Genie One what keeps going wrong.

## Get started with Unity Gateway trace analysis with Genie One

Unity Gateway is Generally Available, and you can now monitor all AI activity using the unified trace table, which is now in Beta. See [our docs](https://docs.databricks.com/aws/en/ai-gateway/unified-trace-table) on how to get started. 

### Get the latest posts in your inbox

Subscribe to our blog and get the latest posts delivered to your inbox.

## Sign up

![databricks logo]()
![databricks logo](https://www.databricks.com/sites/default/files/2023-08/databricks-default.png?v=1712162038)
![databricks logo]()
![databricks logo](https://www.databricks.com/sites/default/files/2023-08/databricks-default.png?v=1712162038)

Databricks Inc.  
160 Spear Street, 15th Floor  
San Francisco, CA 94105  
1-866-330-0121

![]()
![](https://www.databricks.com/sites/default/files/2021/02/telco-icon-2.png?v=1715274112)

[See Careers](https://www.databricks.com/company/careers)  
[at Databricks](https://www.databricks.com/company/careers)

© Databricks 2026. All rights reserved. Apache, Apache Spark, Spark, the Spark Logo, Apache Iceberg, Iceberg, and the Apache Iceberg logo are trademarks of the [Apache Software Foundation](https://www.apache.org/).

![](https://www.databricks.com/sites/default/files/2022-12/gpcicon_small.png)
