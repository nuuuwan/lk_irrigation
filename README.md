# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_18:11:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,476 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 18:11:39 | Baddegama (Gin Ganga) | 3.76 | 🟡 Alert | -0.027 |  |
| 2026-09-28 18:10:00 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:08:19 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | -0.026 |  |
| 2026-09-28 18:08:08 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-28 18:08:00 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-28 18:06:35 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:05:34 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.019 |  |
| 2026-09-28 18:05:32 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.029 |  |
| 2026-09-28 18:04:39 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | -0.011 |  |
| 2026-09-28 18:04:04 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:04:01 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:03:30 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:03:26 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:03:12 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:59 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:02:50 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.084 |  |
| 2026-09-28 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.30 | 🟢 Normal | -0.091 |  |
| 2026-09-28 18:02:33 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:32 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |
| 2026-09-28 18:02:25 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-09-28 18:02:12 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:08 | Thaldena (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.059 |  |
| 2026-09-28 18:02:07 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:06 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-09-28 18:02:05 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-28 18:01:54 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:44 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-09-28 18:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:34 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:33 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-28 18:01:28 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:10 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:05 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:00:55 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 18:04:39 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | -0.011 |  |
| 2026-09-28 18:11:39 | Baddegama (Gin Ganga) | 3.76 | 🟡 Alert | -0.027 |  |
| 2026-09-28 18:02:06 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-09-28 18:02:00 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-28 18:08:08 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-28 18:08:00 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-28 18:02:05 | Rathnapura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-28 18:04:01 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:33 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:33 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:07 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 17:09:48 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:06:35 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:32 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:28 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:03:26 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:02:12 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:03:12 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:10:00 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:10 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:01:54 | Manampitiya (Mahaweli Ganga) | -0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:02:59 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:04:04 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:34 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:03:30 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-28 18:01:32 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-09-28 18:02:25 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-09-28 18:01:44 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.012 |  |
| 2026-09-28 18:05:34 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.019 |  |
| 2026-09-28 18:08:19 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | -0.026 |  |
| 2026-09-28 18:05:32 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.029 |  |
| 2026-09-28 18:00:55 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-09-28 18:02:08 | Thaldena (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.059 |  |
| 2026-09-28 18:02:50 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.084 |  |
| 2026-09-28 18:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.30 | 🟢 Normal | -0.091 |  |
| 2026-09-28 18:02:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)