# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_12:21:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 12:21:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:13:18 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:09:54 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.018 |  |
| 2026-09-03 12:07:21 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:07:14 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:07:06 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 12:06:56 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-09-03 12:05:36 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-03 12:05:33 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:05:18 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.053 |  |
| 2026-09-03 12:04:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-03 12:04:37 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.335 |  |
| 2026-09-03 12:04:36 | Padiyathalawa (Maduru Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-09-03 12:04:30 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-09-03 12:04:28 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-03 12:04:26 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:03:53 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:03:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.081 |  |
| 2026-09-03 12:03:22 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:03:18 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-03 12:03:02 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:03:01 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-03 12:02:58 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:02:50 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 12:02:47 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:02:19 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-03 12:02:16 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 12:02:08 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-09-03 12:01:57 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-03 12:01:56 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.079 |  |
| 2026-09-03 12:01:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:28 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:11 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.174 |  |
| 2026-09-03 12:01:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:08 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:00 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-03 12:00:57 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 12:02:08 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-09-03 12:04:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-03 12:05:36 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-03 12:04:28 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-03 12:07:06 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 12:02:16 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 12:02:50 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 12:01:56 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:03:02 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:03:53 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:08 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:02:47 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:03:22 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:04:26 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:00:57 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:13:18 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:01:28 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:02:58 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:07:21 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:21:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:07:14 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 12:06:56 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-09-03 12:04:36 | Padiyathalawa (Maduru Oya) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-09-03 12:01:57 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-03 12:03:01 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-03 12:03:18 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-03 12:02:19 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-03 12:04:30 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-09-03 12:09:54 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.018 |  |
| 2026-09-03 12:01:00 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-03 12:05:18 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.053 |  |
| 2026-09-03 12:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.079 |  |
| 2026-09-03 12:03:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.081 |  |
| 2026-09-03 12:01:11 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.174 |  |
| 2026-09-03 12:04:37 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.335 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)