# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_16:23:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,073 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 16:23:31 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:21:08 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.008 |  |
| 2026-09-01 16:18:04 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.017 |  |
| 2026-09-01 16:15:08 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-01 16:15:03 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:14:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:13:40 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:07:30 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2026-09-01 16:07:13 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:07:06 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:07:06 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:06:39 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:06:38 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 16:06:18 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:05:54 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-09-01 16:05:34 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-01 16:05:22 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:05:22 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.048 |  |
| 2026-09-01 16:05:14 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-01 16:04:58 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:04:30 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:04:09 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-01 16:04:09 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:03:24 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:03:07 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:03:05 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-01 16:03:05 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.059 |  |
| 2026-09-01 16:02:59 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:02:32 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 16:02:21 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-01 16:02:19 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-01 16:02:17 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-01 16:02:14 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-01 16:02:12 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-01 16:02:07 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:02:01 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:02:00 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.082 |  |
| 2026-09-01 16:01:49 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:01:13 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 16:01:04 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-01 16:00:58 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:00:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 16:02:21 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-01 16:03:05 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-01 16:04:09 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-01 16:15:08 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-01 16:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 16:02:32 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 16:06:38 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 16:07:13 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:01:13 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:02:01 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:02:07 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:14:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:00:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:13:40 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:07:06 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:02:59 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:03:05 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:04:09 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:01:49 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:23:31 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:06:39 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:03:07 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:03:24 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:06:18 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:04:58 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:00:58 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:15:03 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:43 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:05:22 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 16:21:08 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.008 |  |
| 2026-09-01 16:07:30 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2026-09-01 16:05:14 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-01 16:05:34 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-01 16:01:04 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-01 16:18:04 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.017 |  |
| 2026-09-01 16:05:54 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-09-01 16:05:22 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.048 |  |
| 2026-09-01 16:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.059 |  |
| 2026-09-01 16:02:00 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)