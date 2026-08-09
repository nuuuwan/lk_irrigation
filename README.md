# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_22:17:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 22:17:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:16:47 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-09 22:12:13 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:11:00 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.026 |  |
| 2026-08-09 22:09:30 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-08-09 22:07:43 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-09 22:07:16 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-08-09 22:07:04 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-08-09 22:06:45 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-09 22:06:03 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-09 22:05:55 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:05:26 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:05:06 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:04:55 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:04:16 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-09 22:04:01 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:03:44 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:03:39 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 22:03:11 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:03:10 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 22:03:03 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:56 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-08-09 22:02:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:24 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.180 |  |
| 2026-08-09 22:02:16 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.050 |  |
| 2026-08-09 22:02:08 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:07 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-09 22:02:06 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:00 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 22:01:41 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.010 |  |
| 2026-08-09 22:01:31 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:01:29 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:00:48 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:00:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 22:06:45 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-09 22:02:07 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-09 22:06:03 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-09 21:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-09 22:07:43 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-09 22:02:00 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 22:03:39 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 22:03:10 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 22:16:47 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-09 22:03:03 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:08 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:00:40 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:16 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:05:06 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:03:44 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:02:06 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:05:55 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:17:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:01:29 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:04:55 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:04:01 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:00:48 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:03:11 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:12:13 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:01:31 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:05:26 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 22:07:16 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-08-09 22:09:30 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-08-09 22:02:56 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-08-09 22:01:41 | Peradeniya (Mahaweli Ganga) | 3.80 | 🟢 Normal | -0.010 |  |
| 2026-08-09 22:04:16 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-09 22:07:04 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-08-09 22:11:00 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.026 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-09 22:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.050 |  |
| 2026-08-09 22:02:24 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)