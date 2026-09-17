# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_07:11:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,131 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 07:11:54 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:11:52 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.109 |  |
| 2026-09-17 07:08:15 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.012 |  |
| 2026-09-17 07:07:57 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.040 |  |
| 2026-09-17 07:07:55 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 07:07:37 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.037 |  |
| 2026-09-17 07:06:47 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.481 | 🔺 Rising |
| 2026-09-17 07:06:45 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.037 |  |
| 2026-09-17 07:06:37 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:06:05 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-09-17 07:05:30 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.081 |  |
| 2026-09-17 07:05:19 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.032 |  |
| 2026-09-17 07:05:06 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-17 07:04:56 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:04:42 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.019 |  |
| 2026-09-17 07:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.39 | 🟢 Normal | -0.161 |  |
| 2026-09-17 07:04:16 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.029 |  |
| 2026-09-17 07:03:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:03:40 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:03:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:03:27 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:03:20 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-17 07:03:04 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-09-17 07:02:56 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:02:15 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:02:13 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-09-17 07:02:07 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:02:07 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:02:04 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.020 |  |
| 2026-09-17 07:01:12 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:01:04 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.005 |  |
| 2026-09-17 07:00:50 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:00:43 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-17 07:00:22 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-09-17 07:00:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.095 |  |
| 2026-09-17 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 06:36:50 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 07:06:05 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-09-17 07:06:47 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.481 | 🔺 Rising |
| 2026-09-17 06:02:46 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 07:03:20 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-17 06:12:02 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-17 07:02:56 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:00:50 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:03:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:03:27 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:03:40 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 07:07:55 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 07:01:12 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:06:37 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:04:56 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:02:15 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:05:30 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:02:07 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:03:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:11:54 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:02:07 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 07:01:04 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.005 |  |
| 2026-09-17 07:05:06 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-17 07:03:04 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-09-17 07:00:43 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-17 07:00:22 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-09-17 07:08:15 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.012 |  |
| 2026-09-17 07:04:42 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.019 |  |
| 2026-09-17 07:02:04 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.020 |  |
| 2026-09-17 07:02:13 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-09-17 07:04:16 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.029 |  |
| 2026-09-17 07:05:19 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.032 |  |
| 2026-09-17 07:06:45 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.037 |  |
| 2026-09-17 07:07:37 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.037 |  |
| 2026-09-17 07:07:57 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.040 |  |
| 2026-09-17 07:05:30 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.081 |  |
| 2026-09-17 07:00:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.095 |  |
| 2026-09-17 07:11:52 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.109 |  |
| 2026-09-17 07:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.39 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)