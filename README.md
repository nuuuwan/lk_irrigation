# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_19:06:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,701 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 19:06:13 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-16 19:06:03 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.018 |  |
| 2026-09-16 19:05:48 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:05:31 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-09-16 19:05:10 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 19:05:10 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-09-16 19:04:51 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 19:04:00 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:03:54 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:03:43 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-16 19:03:21 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.060 |  |
| 2026-09-16 19:02:49 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-16 19:02:45 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:44 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-16 19:02:39 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:37 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:23 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-16 19:02:18 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:09 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.052 |  |
| 2026-09-16 19:02:06 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-16 19:01:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.089 |  |
| 2026-09-16 19:01:58 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:01:42 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-16 19:01:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:01:02 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-09-16 19:00:42 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 19:00:27 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.086 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 18:04:34 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-09-16 19:01:02 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-09-16 19:05:10 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-09-16 19:00:27 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-16 19:02:23 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-16 19:01:42 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-16 19:06:13 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-16 19:05:10 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-16 19:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 19:04:51 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:39 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:18 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:01:58 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:04:00 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:00:42 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:00:17 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:09:47 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:05:48 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:45 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:07:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:03:54 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:01:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:02:37 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-16 19:03:43 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-16 19:02:44 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-16 19:02:49 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-16 19:02:06 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-16 19:05:31 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-09-16 18:05:29 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.014 |  |
| 2026-09-16 18:04:50 | Baddegama (Gin Ganga) | 3.05 | 🟢 Normal | -0.015 |  |
| 2026-09-16 19:06:03 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.018 |  |
| 2026-09-16 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.037 |  |
| 2026-09-16 19:02:09 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.052 |  |
| 2026-09-16 19:03:21 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.060 |  |
| 2026-09-16 19:01:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)