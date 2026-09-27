# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_21:22:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,701 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 21:22:40 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:16:14 | Baddegama (Gin Ganga) | 4.46 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 21:12:01 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.036 |  |
| 2026-09-27 21:08:13 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-27 21:07:51 | Panadugama (Nilwala Ganga) | 5.02 | 🟡 Alert | -0.037 |  |
| 2026-09-27 21:07:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-09-27 21:06:58 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:06:35 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-09-27 21:06:05 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:05:27 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.032 |  |
| 2026-09-27 21:05:20 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-09-27 21:04:57 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-27 21:04:43 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.036 |  |
| 2026-09-27 21:04:36 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-27 21:04:21 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:04:07 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-09-27 21:03:28 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:03:25 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-09-27 21:03:17 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-09-27 21:03:15 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:57 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:36 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:35 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-09-27 21:02:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:32 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:32 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | -0.089 |  |
| 2026-09-27 21:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.030 |  |
| 2026-09-27 21:02:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 21:02:10 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | -0.076 |  |
| 2026-09-27 21:02:00 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:01:58 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.082 |  |
| 2026-09-27 21:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:01:30 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:01:08 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-09-27 21:00:12 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 21:04:57 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-27 21:16:14 | Baddegama (Gin Ganga) | 4.46 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 21:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | -0.030 |  |
| 2026-09-27 21:07:51 | Panadugama (Nilwala Ganga) | 5.02 | 🟡 Alert | -0.037 |  |
| 2026-09-27 21:01:08 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-09-27 21:04:36 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-27 21:08:13 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-27 21:02:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:01:30 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:06:05 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:57 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:32 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:03:28 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:03:15 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:04:21 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:00 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:06:58 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:22:40 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:02:36 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:06:35 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-09-27 21:05:20 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-09-27 21:00:12 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-09-27 21:02:35 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-09-27 21:07:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-09-27 21:04:07 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-09-27 21:03:17 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-09-27 21:03:25 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-09-27 21:05:27 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.032 |  |
| 2026-09-27 21:04:43 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.036 |  |
| 2026-09-27 21:12:01 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.036 |  |
| 2026-09-27 21:02:10 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | -0.076 |  |
| 2026-09-27 21:01:58 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.082 |  |
| 2026-09-27 21:02:32 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | -0.089 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)