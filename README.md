# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_15:03:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,788 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 15:03:33 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:26 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.012 |  |
| 2026-11-13 15:03:15 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:08 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | -0.022 |  |
| 2026-11-13 15:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -0.030 |  |
| 2026-11-13 15:03:02 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-11-13 15:02:58 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-13 15:02:39 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.078 |  |
| 2026-11-13 15:02:34 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.058 |  |
| 2026-11-13 15:02:33 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-11-13 15:02:27 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:02:20 | Peradeniya (Mahaweli Ganga) | 3.83 | 🟢 Normal | -0.096 |  |
| 2026-11-13 15:02:10 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-11-13 15:02:07 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.040 |  |
| 2026-11-13 15:01:53 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:01:35 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:01:32 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.050 |  |
| 2026-11-13 15:01:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:01:15 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.025 |  |
| 2026-11-13 15:01:11 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:28 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:07 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 15:02:58 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-13 14:05:39 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-13 15:03:08 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | -0.022 |  |
| 2026-11-13 15:02:10 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-11-13 15:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -0.030 |  |
| 2026-11-13 14:00:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-13 15:01:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:01:11 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:00:12 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-13 15:01:53 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-13 14:02:15 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:15 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:02:27 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:03:33 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:01:35 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:28 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-13 15:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:03:02 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-13 14:01:04 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-11-13 15:03:26 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.012 |  |
| 2026-11-13 14:05:51 | Kuda Oya (Kirindi Oya) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-11-13 14:05:07 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-13 15:03:02 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-11-13 14:08:18 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-11-13 14:24:56 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.022 |  |
| 2026-11-13 14:04:31 | Pitabeddara (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.024 |  |
| 2026-11-13 15:01:15 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.025 |  |
| 2026-11-13 14:19:16 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | -0.032 |  |
| 2026-11-13 15:02:07 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.040 |  |
| 2026-11-13 15:02:33 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-11-13 15:00:07 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.042 |  |
| 2026-11-13 14:03:55 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.050 |  |
| 2026-11-13 14:06:46 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.050 |  |
| 2026-11-13 15:01:32 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.050 |  |
| 2026-11-13 14:07:12 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.055 |  |
| 2026-11-13 15:02:34 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.058 |  |
| 2026-11-13 15:02:39 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.078 |  |
| 2026-11-13 14:04:33 | Rathnapura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.083 |  |
| 2026-11-13 15:02:20 | Peradeniya (Mahaweli Ganga) | 3.83 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)