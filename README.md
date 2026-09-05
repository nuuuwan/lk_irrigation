# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_07:35:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,308 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 07:35:55 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:24:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:24:03 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.008 |  |
| 2026-09-05 07:10:06 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:09:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:06:24 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:05:48 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-05 07:05:37 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.030 |  |
| 2026-09-05 07:05:33 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.028 |  |
| 2026-09-05 07:04:17 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.105 |  |
| 2026-09-05 07:04:03 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:57 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:49 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:48 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:23 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 07:03:15 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:14 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:06 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-05 07:03:01 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-05 07:02:50 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 07:02:27 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:02:24 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:02:14 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-09-05 07:01:53 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-05 07:01:44 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-05 07:01:37 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:01:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:01:24 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-09-05 07:01:18 | Thanamalwila (Kirindi Oya) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-05 07:01:12 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-05 07:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:00:50 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:00:50 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.001 |  |
| 2026-09-05 07:00:15 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.172 |  |
| 2026-09-05 07:00:15 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.017 |  |
| 2026-09-05 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 07:03:01 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-05 07:03:06 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-05 07:01:12 | Peradeniya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-05 07:01:44 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-05 07:01:18 | Thanamalwila (Kirindi Oya) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-05 07:01:53 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-05 07:03:23 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 07:02:50 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 07:03:49 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:01:37 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:01:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:02:24 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:00:50 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:04:03 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:10:06 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:48 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:35:55 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:06:24 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:14 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:09:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:57 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:04:17 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:02:27 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:24:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:03:15 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-05 07:00:50 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.001 |  |
| 2026-09-05 06:05:30 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.006 |  |
| 2026-09-05 07:24:03 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.008 |  |
| 2026-09-05 07:05:48 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-05 07:00:15 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.017 |  |
| 2026-09-05 07:01:24 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-09-05 07:02:14 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-09-05 07:05:33 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.028 |  |
| 2026-09-05 07:05:37 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | -0.030 |  |
| 2026-09-05 07:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.105 |  |
| 2026-09-05 07:00:15 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)