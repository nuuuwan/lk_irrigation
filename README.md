# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_15:13:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,555 measurements** from **39** stations.
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
| 2026-11-24 15:13:44 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:10:06 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.026 |  |
| 2026-11-24 15:07:13 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -1.241 |  |
| 2026-11-24 15:07:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.056 |  |
| 2026-11-24 15:07:00 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 15:06:44 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -1.241 |  |
| 2026-11-24 15:06:36 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.039 |  |
| 2026-11-24 15:06:28 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.019 |  |
| 2026-11-24 15:06:27 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-24 15:06:14 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.037 |  |
| 2026-11-24 15:05:25 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 15:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.077 |  |
| 2026-11-24 15:05:15 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-24 15:05:14 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-24 15:04:28 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-24 15:04:19 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 15:04:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:04:09 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:03:59 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-24 15:03:48 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:03:43 | Weraganthota (Mahaweli Ganga) | -2.43 | 🟢 Normal | -0.048 |  |
| 2026-11-24 15:03:40 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.071 |  |
| 2026-11-24 15:03:32 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-11-24 15:03:25 | Moraketiya (Walawe Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-11-24 15:03:21 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.118 |  |
| 2026-11-24 15:03:16 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-11-24 15:03:08 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | -0.059 |  |
| 2026-11-24 15:03:02 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:02:57 | Giriulla (Maha Oya) | 2.53 | 🟢 Normal | -0.070 |  |
| 2026-11-24 15:02:27 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:02:24 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:02:23 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 15:02:19 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-24 15:02:11 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-24 15:01:12 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:21 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:17 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:05 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 15:02:19 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-24 15:03:32 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-11-24 15:06:27 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-24 15:05:14 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-24 15:02:11 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-24 15:04:28 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-24 15:07:00 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 14:03:12 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-24 15:05:25 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 15:04:19 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 15:02:23 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 15:02:24 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:21 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:01:12 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:17 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:03:02 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:03:48 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:13:44 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:05 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:04:09 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:04:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:02:27 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:05:15 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-24 15:06:28 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.019 |  |
| 2026-11-24 15:03:25 | Moraketiya (Walawe Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 15:10:06 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.026 |  |
| 2026-11-24 15:03:16 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-11-24 15:03:59 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-24 15:06:14 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.037 |  |
| 2026-11-24 15:06:36 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.039 |  |
| 2026-11-24 15:03:43 | Weraganthota (Mahaweli Ganga) | -2.43 | 🟢 Normal | -0.048 |  |
| 2026-11-24 15:07:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.056 |  |
| 2026-11-24 15:03:08 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | -0.059 |  |
| 2026-11-24 15:02:57 | Giriulla (Maha Oya) | 2.53 | 🟢 Normal | -0.070 |  |
| 2026-11-24 15:03:40 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.071 |  |
| 2026-11-24 15:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.077 |  |
| 2026-11-24 15:03:21 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.118 |  |
| 2026-11-24 15:07:13 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -1.241 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)