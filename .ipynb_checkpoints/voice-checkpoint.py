{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9a52c678-80fd-41a6-b3ad-06855148535d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess\n",
    "\n",
    "def jtalk(t):\n",
    "    open_jtalk=['open_jtalk']\n",
    "    mech=['-x','/usr/local/Cellar/open-jtalk/1.11/dic/']\n",
    "    htsvoice=['-m','/usr/local/Cellar/open-jtalk/1.11/voice/m100/nitech_jp_atr503_m001.htsvoice']\n",
    "    speed=['-r','1.0']\n",
    "    outwav=['-ow','open_jtalk.wav']\n",
    "    cmd=open_jtalk+mech+htsvoice+speed+outwav\n",
    "    subprocess.run(cmd,input=t.encode())\n",
    "    afplay = ['afplay','open_jtalk.wav']\n",
    "    subprocess.run(afplay)\n",
    "    \n",
    "jtalk(\"こんばんは\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a0344b7-3348-4ba0-a42c-61f6266f0370",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ac9b261-5593-43b4-8ec7-1c3a4e57a9c9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
