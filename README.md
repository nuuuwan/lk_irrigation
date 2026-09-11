# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_00:07:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **258,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 00:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-12 00:06:56 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-12 00:06:41 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-12 00:06:22 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-09-12 00:06:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-12 00:05:58 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:05:46 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:05:41 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.009 |  |
| 2026-09-12 00:04:28 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:04:27 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:04:21 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 00:03:33 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-12 00:03:29 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-12 00:02:53 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-12 00:02:47 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:02:21 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-12 00:02:16 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:02:14 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:01:47 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.040 |  |
| 2026-09-12 00:01:47 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:01:36 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:01:13 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:01:10 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-09-12 00:00:48 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-11 23:59:48 | Padiyathalawa (Maduru Oya) | 0.00 | 🟢 Normal | -0.074 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 00:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.600 | 🔺 Rising |
| 2026-09-12 00:06:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-11 23:15:25 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-09-12 00:06:41 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-12 00:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-12 00:03:33 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-11 23:01:16 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-12 00:04:21 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-11 18:03:43 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-11 23:18:22 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-12 00:02:16 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:08:01 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-09-11 23:02:20 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:02:47 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:02:14 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:01:47 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:01:36 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:00:48 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-11 23:07:14 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-11 23:02:38 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:02:21 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-11 23:05:20 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:01:10 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-11 23:03:02 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:05:58 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:05:46 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:04:27 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:02:32 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-11 23:04:36 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:01:13 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-12 00:06:22 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-09-12 00:05:41 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.009 |  |
| 2026-09-12 00:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-12 00:03:29 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-12 00:02:53 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-12 00:06:56 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-11 23:04:36 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-09-12 00:01:47 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.040 |  |
| 2026-09-11 23:59:48 | Padiyathalawa (Maduru Oya) | 0.00 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)