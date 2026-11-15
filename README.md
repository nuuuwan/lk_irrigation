# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_22:02:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 22:02:29 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-15 22:02:28 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-15 22:02:15 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 22:02:14 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:02:01 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:59 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:34 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:16 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.010 |  |
| 2026-11-15 22:01:15 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:00:49 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:00:12 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.010 |  |
| 2026-11-15 21:24:51 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.029 |  |
| 2026-11-15 21:14:51 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.506 |  |
| 2026-11-15 21:11:23 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.019 |  |
| 2026-11-15 21:11:15 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 21:01:56 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-15 21:02:32 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-15 21:02:02 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 22:02:15 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 21:03:00 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:34 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:02:01 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:59 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:01:34 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:06:17 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:05:47 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:02:14 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:06:59 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:00:49 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:03:51 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:11 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:10:20 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:09:23 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-15 22:01:15 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:08:53 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-11-15 21:05:23 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-15 21:08:45 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-11-15 22:01:16 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.010 |  |
| 2026-11-15 21:04:04 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.010 |  |
| 2026-11-15 22:00:12 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-15 21:11:15 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-11-15 21:11:23 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.019 |  |
| 2026-11-15 21:04:48 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-11-15 22:02:28 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-15 22:02:29 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-11-15 21:02:01 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.022 |  |
| 2026-11-15 21:24:51 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.029 |  |
| 2026-11-15 21:05:59 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.046 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |
| 2026-11-15 21:14:51 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.506 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)