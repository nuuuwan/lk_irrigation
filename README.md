# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_11:03:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,620 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 11:03:08 | Katharagama (Menik Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:03:06 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 11:02:49 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-13 11:02:21 | Panadugama (Nilwala Ganga) | 6.28 | 🟠 Minor Flood | -0.024 |  |
| 2026-11-13 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.05 | 🟡 Alert | -0.020 |  |
| 2026-11-13 11:02:16 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:02:06 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 11:02:05 | Thanamalwila (Kirindi Oya) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-11-13 11:01:33 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.065 |  |
| 2026-11-13 11:01:25 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:01:12 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | -0.052 |  |
| 2026-11-13 11:00:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 10:12:16 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 10:07:00 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 11:02:21 | Panadugama (Nilwala Ganga) | 6.28 | 🟠 Minor Flood | -0.024 |  |
| 2026-11-13 10:02:30 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | 0.665 | 🔺 Rising |
| 2026-11-13 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.05 | 🟡 Alert | -0.020 |  |
| 2026-11-13 10:07:19 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-13 10:07:16 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-13 11:00:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-13 11:02:06 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 11:03:06 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 11:02:16 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:05:13 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:03:00 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:01:07 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-13 11:03:08 | Katharagama (Menik Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-13 10:04:38 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-11-13 11:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-13 11:01:25 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-13 10:02:20 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-13 10:02:04 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-13 10:05:23 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.012 |  |
| 2026-11-13 10:06:57 | Kuda Oya (Kirindi Oya) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-11-13 10:03:29 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-11-13 10:01:36 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-13 09:01:49 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-13 11:02:49 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-13 10:02:30 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.022 |  |
| 2026-11-13 10:09:03 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.028 |  |
| 2026-11-13 10:11:37 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.035 |  |
| 2026-11-13 10:04:29 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.041 |  |
| 2026-11-13 10:03:51 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.044 |  |
| 2026-11-13 11:01:12 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | -0.052 |  |
| 2026-11-13 10:05:25 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.058 |  |
| 2026-11-13 10:04:08 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.059 |  |
| 2026-11-13 11:02:05 | Thanamalwila (Kirindi Oya) | 2.09 | 🟢 Normal | -0.060 |  |
| 2026-11-13 11:01:33 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.065 |  |
| 2026-11-13 10:05:39 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.069 |  |
| 2026-11-13 10:09:48 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.098 |  |
| 2026-11-13 10:02:49 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)