# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_22:18:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,316 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 22:18:26 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:07:43 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.010 |  |
| 2026-09-21 22:07:05 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.037 |  |
| 2026-09-21 22:07:01 | Baddegama (Gin Ganga) | 4.12 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-21 22:06:53 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-09-21 22:06:13 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-21 22:06:09 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.104 |  |
| 2026-09-21 22:05:51 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-21 22:05:40 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | -0.019 |  |
| 2026-09-21 22:05:29 | Thawalama (Gin Ganga) | 3.03 | 🟢 Normal | -0.050 |  |
| 2026-09-21 22:05:27 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 22:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.12 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-21 22:04:41 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 22:04:18 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:03:59 | Rathnapura (Kalu Ganga) | 5.39 | 🟡 Alert | -0.086 |  |
| 2026-09-21 22:03:41 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:03:12 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:02:53 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.089 |  |
| 2026-09-21 22:02:49 | Glencourse (Kelani Ganga) | 12.94 | 🟢 Normal | -0.070 |  |
| 2026-09-21 22:02:48 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:02:43 | Ellagawa (Kalu Ganga) | 9.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 22:02:36 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-21 22:02:24 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:02:23 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.020 |  |
| 2026-09-21 22:02:10 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-21 22:02:08 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-09-21 22:01:54 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:42 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:39 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:28 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:20 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:12 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:00:43 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:59:59 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 22:07:01 | Baddegama (Gin Ganga) | 4.12 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-21 22:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.12 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-21 22:02:08 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-09-21 22:05:40 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | -0.019 |  |
| 2026-09-21 21:04:38 | Magura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.030 |  |
| 2026-09-21 22:03:59 | Rathnapura (Kalu Ganga) | 5.39 | 🟡 Alert | -0.086 |  |
| 2026-09-21 22:02:36 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-21 22:02:10 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-21 21:59:59 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-21 22:02:43 | Ellagawa (Kalu Ganga) | 9.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 22:05:27 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 22:04:41 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 22:06:13 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-21 22:02:24 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:54 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:03:12 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:12 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:00:43 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:18:26 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:28 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:02:48 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:03:41 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:42 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:04:18 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:39 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:01:20 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 22:05:51 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-21 22:07:43 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.010 |  |
| 2026-09-21 22:06:53 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-21 22:02:23 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.020 |  |
| 2026-09-21 22:07:05 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.037 |  |
| 2026-09-21 22:05:29 | Thawalama (Gin Ganga) | 3.03 | 🟢 Normal | -0.050 |  |
| 2026-09-21 22:02:49 | Glencourse (Kelani Ganga) | 12.94 | 🟢 Normal | -0.070 |  |
| 2026-09-21 22:02:53 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.089 |  |
| 2026-09-21 22:06:09 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)