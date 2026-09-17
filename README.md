# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_16:33:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,492 measurements** from **39** stations.
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
| 2026-09-17 16:33:16 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | -0.007 |  |
| 2026-09-17 16:17:52 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | -0.008 |  |
| 2026-09-17 16:10:32 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 16:09:43 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.009 |  |
| 2026-09-17 16:09:19 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:07:46 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-17 16:06:58 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:06:41 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-09-17 16:06:25 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:06:16 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:05:52 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-09-17 16:05:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 16:05:07 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.068 |  |
| 2026-09-17 16:04:44 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:03:55 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 16:03:49 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2026-09-17 16:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-17 16:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-17 16:03:39 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-17 16:03:19 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:03:18 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-17 16:03:10 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-09-17 16:03:01 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-17 16:02:38 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-17 16:02:37 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:36 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-17 16:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:28 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:24 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 16:02:18 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:16 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:07 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-09-17 16:02:06 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:01:51 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:01:19 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-17 16:00:56 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:00:50 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-09-17 16:00:28 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:00:15 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 16:03:49 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2026-09-17 16:10:32 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | 0.000 |  |
| 2026-09-17 16:07:46 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-17 16:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-17 16:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-17 16:03:01 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-17 16:03:18 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-17 16:02:36 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-17 16:02:24 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 16:02:38 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-17 16:03:55 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 16:05:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 16:00:56 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:00:15 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:04:44 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:06:58 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:06 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:00:28 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:01:51 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:06:16 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:37 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:16 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:06:25 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:09:19 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:18 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:02:28 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:33:16 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | -0.007 |  |
| 2026-09-17 16:17:52 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | -0.008 |  |
| 2026-09-17 16:09:43 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.009 |  |
| 2026-09-17 16:06:41 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-09-17 16:01:19 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-17 16:03:39 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-17 16:02:07 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-09-17 16:05:52 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-09-17 16:03:10 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-09-17 16:00:50 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-09-17 16:05:07 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)