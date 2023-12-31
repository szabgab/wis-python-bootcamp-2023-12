{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fc9cb413",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Add start range: 3\n",
      "Add end range: 5\n",
      "Add num of attemps: 2\n",
      "Add math operator: +, -, /, * +\n",
      "Lets start the game!\n",
      "How much is 3 + 3? 2\n",
      "Incorrect\n",
      "How much is 3 + 3? 2\n",
      "Incorrect\n",
      "done\n"
     ]
    }
   ],
   "source": [
    "#### \n",
    "#### \n",
    "\n",
    "\n",
    "import random\n",
    "\n",
    "start_range = int(input(\"Add start range: \"))\n",
    "end_range   = int(input(\"Add end range: \"))\n",
    "number_of_attempts   = int(input(\"Add num of attemps: \"))\n",
    "operator = input(\"Add math operator: +, -, /, * \")\n",
    "\n",
    "print(\"Lets start the game!\")\n",
    "\n",
    "a = random.randrange(start_range, end_range)\n",
    "b = random.randrange(start_range, end_range)\n",
    "\n",
    "for _ in range(0, number_of_attempts):\n",
    "    result = input(f\"How much is {a} {operator} {b}? \")\n",
    "    if operator == '+':\n",
    "        if a + b == int(result):\n",
    "            print(f\"Indeed {result} is the correct number\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Incorrect\")\n",
    "        \n",
    "    elif operator == '-':\n",
    "        if a - b == int(result):\n",
    "            print(f\"Indeed {result} is the correct number\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Incorrect\")\n",
    "                    \n",
    "    elif operator == '*':\n",
    "        if a * b == int(result):\n",
    "            print(f\"Indeed {result} is the correct number\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Incorrect\")\n",
    "\n",
    "        \n",
    "    elif operator == '/':\n",
    "        if a / b == int(result):\n",
    "            print(f\"Indeed {result} is the correct number\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Incorrect\")\n",
    "\n",
    "\n",
    "print(\"done\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
