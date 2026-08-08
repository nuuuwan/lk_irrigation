# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_10:05:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 10:05:36 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:05:23 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 10:05:22 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:04:14 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -0.040 |  |
| 2026-08-08 10:03:52 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-08-08 10:03:32 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:03:29 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-08 10:03:25 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:03:00 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:57 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:50 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:32 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:26 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:20 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:10 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:10 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 10:02:04 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-08-08 10:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-08 10:01:45 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.005 |  |
| 2026-08-08 10:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:30 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 10:01:22 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:22 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:21 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:07 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-08-08 10:00:30 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:00:08 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:59:51 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 09:15:10 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-08 09:05:34 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-08 09:06:45 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-08 10:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-08 10:05:23 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 09:04:46 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 10:02:10 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 10:01:30 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 10:05:36 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:10 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:21 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:22 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:03:25 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:03:03 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:22 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:03:32 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:26 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:20 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:57 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:00:08 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:03:00 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:32 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:07:23 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:00:30 | Thanthirimale (Malwathu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:09:08 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-08 09:59:51 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:50 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:05:22 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-08-08 10:01:45 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.005 |  |
| 2026-08-08 09:09:15 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-08-08 10:02:04 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-08-08 10:03:52 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-08-08 10:03:29 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-08 10:01:07 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-08-08 09:07:14 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.038 |  |
| 2026-08-08 10:04:14 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)