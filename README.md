# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_09:07:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **258,706 measurements** from **39** stations.
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
| 2026-09-12 09:07:43 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-09-12 09:07:18 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:06:05 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:05:34 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:05:20 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:05:17 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:04:54 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:04:43 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:04:36 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.140 |  |
| 2026-09-12 09:04:33 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.020 |  |
| 2026-09-12 09:04:33 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-09-12 09:04:09 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-12 09:04:00 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:03:54 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:03:28 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-12 09:03:20 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-12 09:03:15 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:03:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.052 |  |
| 2026-09-12 09:03:10 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-09-12 09:03:01 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 09:02:59 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:54 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.079 |  |
| 2026-09-12 09:02:50 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:27 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:24 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:23 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-12 09:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:01:43 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-12 09:01:39 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.031 |  |
| 2026-09-12 09:01:27 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-09-12 09:01:14 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-12 09:00:52 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.040 |  |
| 2026-09-12 09:00:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:00:19 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 09:01:43 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-12 09:03:28 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-12 09:03:20 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-12 09:02:23 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-12 08:06:29 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-12 09:03:01 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 08:06:11 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-12 09:03:15 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:05:20 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:59 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:54 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 08:01:52 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 08:01:16 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:04:43 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:04:00 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:07:18 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:06:05 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:03:54 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:00:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:05:34 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:27 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:05:17 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:24 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:04:54 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:00:19 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:02:50 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-12 09:07:43 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-09-12 09:04:33 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-09-12 09:01:14 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-12 09:04:09 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-12 09:01:27 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-09-12 09:04:33 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.020 |  |
| 2026-09-12 09:03:10 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-09-12 09:01:39 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.031 |  |
| 2026-09-12 09:00:52 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.040 |  |
| 2026-09-12 09:03:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.052 |  |
| 2026-09-12 09:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.079 |  |
| 2026-09-12 09:04:36 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)