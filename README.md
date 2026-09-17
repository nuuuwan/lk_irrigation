# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_19:06:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,600 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 19:06:38 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:06:18 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 19:06:13 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-09-17 19:06:10 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-09-17 19:05:58 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:05:41 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:05:17 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-17 19:05:06 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-17 19:04:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2026-09-17 19:04:24 | Magura (Kalu Ganga) | 4.93 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-09-17 19:04:10 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 19:04:05 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:03:57 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-17 19:03:52 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-17 19:03:47 | Baddegama (Gin Ganga) | 3.57 | 🟡 Alert | -0.019 |  |
| 2026-09-17 19:03:45 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:03:31 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:03:08 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:52 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 19:02:45 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 19:02:44 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:44 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:37 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:18 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-09-17 19:02:14 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 19:01:45 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-17 19:00:45 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.032 |  |
| 2026-09-17 19:00:11 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 19:04:24 | Magura (Kalu Ganga) | 4.93 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-09-17 19:03:47 | Baddegama (Gin Ganga) | 3.57 | 🟡 Alert | -0.019 |  |
| 2026-09-17 19:02:18 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-09-17 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.99 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 19:03:52 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-17 19:03:57 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-17 19:05:17 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-17 18:02:22 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 19:02:14 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 19:02:45 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 19:06:18 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 19:04:10 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 19:02:52 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:05:41 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:05:58 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:03:08 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:44 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:07:32 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:44 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:37 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:03:45 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:04:05 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:03:31 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:06:38 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:05:27 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:00:11 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:05:06 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-17 19:06:10 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-09-17 19:01:45 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-17 18:00:34 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-17 18:07:46 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.019 |  |
| 2026-09-17 19:06:13 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-09-17 19:00:45 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.032 |  |
| 2026-09-17 19:04:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)