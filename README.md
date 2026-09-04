# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_01:36:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,088 measurements** from **39** stations.
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
| 2026-09-05 01:36:09 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:31:34 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:24:24 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:24:11 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-05 01:17:57 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:16:28 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:09:50 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.043 |  |
| 2026-09-05 01:06:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:05:45 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-05 01:05:22 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-09-05 01:04:42 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-09-05 01:03:47 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:03:28 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-05 01:03:26 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-09-05 01:03:25 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.048 |  |
| 2026-09-05 01:03:05 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:02:43 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-05 01:02:39 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:02:25 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-05 01:02:10 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:02:04 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:01:41 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:01:36 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-05 01:01:16 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:01:10 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-05 01:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:00:36 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 00:45:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | 1.333 | 🔺 Rising |
| 2026-09-05 01:03:26 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-09-05 01:01:10 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-05 01:03:28 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-05 01:24:11 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-05 01:02:43 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-05 01:01:36 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-05 01:02:25 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-05 00:14:20 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:07:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:00:53 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:02:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:02:04 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:24:24 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:03:45 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:21:49 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:00:36 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:36:09 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:02:39 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:01:41 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:31:34 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:02:10 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:17:57 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:06:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:03:47 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:03:05 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:02:31 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:16:28 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:07:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:01:16 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:05:31 | Thanamalwila (Kirindi Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:05:22 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-09-05 01:05:45 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-05 00:26:13 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | -0.016 |  |
| 2026-09-05 01:04:42 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-09-05 01:09:50 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | -0.043 |  |
| 2026-09-05 01:03:25 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.048 |  |
| 2026-09-04 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)