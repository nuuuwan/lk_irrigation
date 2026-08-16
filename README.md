# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_00:18:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,466 measurements** from **39** stations.
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
| 2026-08-17 00:18:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-17 00:17:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-17 00:17:15 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-08-17 00:13:49 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:13:16 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:09:40 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:08:51 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-08-17 00:07:25 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.024 |  |
| 2026-08-17 00:06:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:06:10 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:05:53 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.062 |  |
| 2026-08-17 00:05:43 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-17 00:05:21 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:05:10 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:05:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-17 00:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-08-17 00:04:22 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 00:04:08 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-08-17 00:04:07 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:52 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:44 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:44 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.025 |  |
| 2026-08-17 00:03:18 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:14 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:09 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:23 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:23 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:22 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:13 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 00:01:38 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-08-17 00:01:38 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-08-17 00:01:36 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-17 00:01:27 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:01:20 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:01:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-17 00:01:12 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:01:00 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 00:17:15 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.418 | 🔺 Rising |
| 2026-08-17 00:01:36 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-17 00:17:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-17 00:05:01 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-17 00:18:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-17 00:02:13 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 00:04:22 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 00:05:21 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:23 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:01:12 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:06:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:01:00 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:01:20 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:57 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:22 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:13:49 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:09:40 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:06:10 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:09 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:02:23 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:44 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:14 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:13:16 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:10:59 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:04:07 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:03:18 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:01:27 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:05:10 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-17 00:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-08-17 00:05:43 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-17 00:01:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-08-17 00:01:38 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-08-17 00:08:51 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-08-17 00:01:38 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-08-17 00:07:25 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.024 |  |
| 2026-08-17 00:03:44 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.025 |  |
| 2026-08-17 00:05:53 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)