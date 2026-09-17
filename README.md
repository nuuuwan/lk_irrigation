# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_20:06:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,631 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 20:06:39 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-09-17 20:06:37 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-17 20:06:32 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:05:45 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-17 20:05:02 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 20:05:02 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:04:47 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:03:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:03:50 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:03:04 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-09-17 20:02:48 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:02:41 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:02:36 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:02:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.095 |  |
| 2026-09-17 20:02:29 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:02:20 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:02:12 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-09-17 20:01:55 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-09-17 20:01:46 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-09-17 20:01:28 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:01:18 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:01:14 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-17 20:00:53 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-17 20:00:51 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:00:12 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-09-17 19:30:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.102 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 20:03:04 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-09-17 19:03:47 | Baddegama (Gin Ganga) | 3.57 | 🟡 Alert | -0.019 |  |
| 2026-09-17 19:30:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-17 20:01:14 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-17 19:03:57 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-17 20:00:53 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-17 20:05:45 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-17 19:05:17 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-17 20:06:37 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-17 19:04:10 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 20:05:02 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 19:13:38 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:02:36 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:03:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:03:08 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:02:20 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:02:37 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:02:29 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:00:51 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:06:32 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:06:38 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-17 19:07:00 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:01:18 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:01:28 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 20:00:12 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-09-17 20:06:39 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-09-17 20:02:48 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:03:50 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:05:02 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:04:47 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-17 20:02:41 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-17 19:12:15 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.019 |  |
| 2026-09-17 20:02:12 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-09-17 20:01:55 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-09-17 20:01:46 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-09-17 20:02:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)