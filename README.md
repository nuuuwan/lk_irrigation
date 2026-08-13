# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_18:30:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,564 measurements** from **39** stations.
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
| 2026-08-13 18:30:54 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:13:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:12:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:12:53 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:08:41 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:08:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:29 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:05:27 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:04:55 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:04:41 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-08-13 18:04:26 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:03:48 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.090 |  |
| 2026-08-13 18:03:21 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-13 18:03:13 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:03:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-08-13 18:02:34 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:02:21 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-13 18:02:19 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-08-13 18:02:13 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.068 |  |
| 2026-08-13 18:02:08 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 18:02:08 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:04 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:02 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:02:01 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:01:58 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:01:56 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:01:53 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-08-13 18:01:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-08-13 18:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.071 |  |
| 2026-08-13 18:01:18 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:01:11 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 18:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:00:36 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 18:00:23 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:00:21 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 18:00:19 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:00:10 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 18:02:21 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-13 18:00:21 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 18:03:21 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-13 18:02:08 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 18:01:11 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 18:00:36 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 18:04:26 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:12:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:08 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:13:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:04:55 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:12:53 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:01:18 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:05:27 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:00:10 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:01:56 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:00:23 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:03:13 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:30:54 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:08:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:04 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:02:19 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-08-13 18:04:41 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-08-13 18:06:29 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:02:34 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:02:01 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-13 18:00:19 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-08-13 18:01:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-08-13 18:01:53 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-08-13 18:02:02 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:01:58 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.040 |  |
| 2026-08-13 18:03:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-08-13 18:02:13 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.068 |  |
| 2026-08-13 18:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.071 |  |
| 2026-08-13 18:03:48 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)