# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_03:03:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,172 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thawalama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 03:03:10 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.003 |  |
| 2026-09-15 03:03:02 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 03:02:58 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-09-15 03:02:56 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 03:02:49 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:44 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.851 | 🔺 Rising |
| 2026-09-15 03:02:42 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:42 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-15 03:02:24 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-09-15 03:02:15 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-09-15 03:02:15 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:48 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-09-15 03:01:47 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:44 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-09-15 03:00:56 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:00:41 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:45:49 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.851 | 🔺 Rising |
| 2026-09-15 02:40:09 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-09-15 02:38:37 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-09-15 02:35:20 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-15 02:20:21 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-15 02:19:23 | Thawalama (Gin Ganga) | 4.27 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-09-15 02:19:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 02:19:23 | Thawalama (Gin Ganga) | 4.27 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-09-15 03:02:42 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-15 03:02:44 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.851 | 🔺 Rising |
| 2026-09-15 03:02:15 | Panadugama (Nilwala Ganga) | 4.18 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-09-15 03:02:24 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-09-15 03:02:58 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-09-15 02:05:17 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-09-15 02:35:20 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-15 02:10:45 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-15 02:01:00 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 02:14:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-15 02:14:24 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-15 02:03:10 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 02:20:21 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-15 03:02:56 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 03:03:02 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 03:00:56 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:20 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:02:01 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:42 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:47 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:45 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:19:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:01:44 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:22 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:49 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:02:15 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 01:06:12 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 03:03:10 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.003 |  |
| 2026-09-15 02:08:45 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-15 02:38:37 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-09-15 03:01:48 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-09-15 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-09-15 01:04:54 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.022 |  |
| 2026-09-15 02:01:49 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.161 |  |
| 2026-09-15 01:01:51 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.330 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)