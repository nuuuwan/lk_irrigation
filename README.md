# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_07:37:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,500 measurements** from **39** stations.
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
| 2026-09-03 07:37:19 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:27:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.014 |  |
| 2026-09-03 07:27:02 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:22:55 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:21:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:08:36 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-09-03 07:08:30 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:08:26 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:08:23 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2026-09-03 07:08:02 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-03 07:07:19 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.031 |  |
| 2026-09-03 07:07:05 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-03 07:06:11 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:06:04 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:05:50 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.028 |  |
| 2026-09-03 07:05:45 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.051 |  |
| 2026-09-03 07:05:41 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-03 07:05:35 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:05:06 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:04:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.108 |  |
| 2026-09-03 07:04:40 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:04:28 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:04:07 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:04:00 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:03:30 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-09-03 07:03:24 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:03:11 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:03:08 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:02:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | -0.011 |  |
| 2026-09-03 07:02:16 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:02:15 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:01:44 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.002 |  |
| 2026-09-03 07:01:28 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:01:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:00:53 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:00:39 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:00:15 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 07:08:02 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-03 07:08:30 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:03:24 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:04:40 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:04:07 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:02:16 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 07:05:41 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-03 07:21:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:01:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:37:19 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:05:06 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:08:26 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:27:02 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:03:11 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:03:08 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:04:32 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:00:53 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:04:00 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:00:39 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:01:28 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:06:11 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:04:28 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:06:04 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:22:55 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 07:05:35 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:23:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | -0.001 |  |
| 2026-09-03 07:01:44 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.002 |  |
| 2026-09-03 07:08:36 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-09-03 07:07:05 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-03 07:03:30 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-09-03 07:02:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | -0.011 |  |
| 2026-09-03 07:27:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.014 |  |
| 2026-09-03 07:08:23 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.027 |  |
| 2026-09-03 07:05:50 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.028 |  |
| 2026-09-03 07:07:19 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | -0.031 |  |
| 2026-09-03 07:05:45 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.051 |  |
| 2026-09-03 07:00:15 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.060 |  |
| 2026-09-03 07:04:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)