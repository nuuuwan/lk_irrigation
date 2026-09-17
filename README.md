# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_18:08:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,571 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 18:08:43 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:08:30 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-17 18:07:46 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.019 |  |
| 2026-09-17 18:07:40 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:07:32 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:06:55 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-09-17 18:06:08 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-09-17 18:05:27 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:05:09 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-17 18:05:05 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:04:53 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-17 18:04:41 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-09-17 18:04:25 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:04:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:04:08 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:04:01 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:03:36 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-09-17 18:03:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:03:22 | Magura (Kalu Ganga) | 4.87 | 🟡 Alert | 0.090 | 🔺 Rising |
| 2026-09-17 18:03:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-17 18:02:25 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-17 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.99 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 18:02:22 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 18:02:06 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:50 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:50 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.052 |  |
| 2026-09-17 18:01:45 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | 0.000 |  |
| 2026-09-17 18:01:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:43 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:24 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:20 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:16 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:00:34 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-17 18:00:33 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-17 18:00:13 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-17 17:56:10 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 18:03:22 | Magura (Kalu Ganga) | 4.87 | 🟡 Alert | 0.090 | 🔺 Rising |
| 2026-09-17 18:01:45 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | 0.000 |  |
| 2026-09-17 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.99 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 18:02:25 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-17 18:00:13 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-17 18:05:09 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-17 18:00:33 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-17 18:02:22 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-17 18:08:30 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:04:08 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:03:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:50 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:07:32 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:16 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:02:06 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:05:05 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:43 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:04:01 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:04:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:05:27 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:24 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:08:43 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:20 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:07:40 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:03:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-17 18:00:34 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-17 18:04:53 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-17 18:07:46 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.019 |  |
| 2026-09-17 18:06:08 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-09-17 18:04:41 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-09-17 18:03:36 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-09-17 18:06:55 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-09-17 18:01:50 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)