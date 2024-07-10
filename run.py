import asyncio
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.api.api import API

def main():
    API()
    print("Hello")


if __name__ == "__main__":
    # asyncio.run(main())
    main()
    print()
