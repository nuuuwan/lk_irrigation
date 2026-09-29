# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_02:25:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,659 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 02:25:26 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-30 02:19:18 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.033 |  |
| 2026-09-30 02:16:07 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:14:31 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:13:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:12:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:12:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-30 02:12:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:11:50 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:07:33 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-09-30 02:07:25 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.124 |  |
| 2026-09-30 02:05:32 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-30 02:05:20 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-09-30 02:05:14 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.039 |  |
| 2026-09-30 02:05:02 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:05:00 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.005 |  |
| 2026-09-30 02:04:45 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-30 02:04:41 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-09-30 02:04:24 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-30 02:03:55 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-09-30 02:03:41 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-30 02:03:29 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:03:28 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:56 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:56 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:47 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:12 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:01:41 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.033 |  |
| 2026-09-30 02:01:21 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.033 |  |
| 2026-09-30 02:01:17 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:00:50 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.010 |  |
| 2026-09-30 02:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:00:36 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 02:03:41 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-30 02:12:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-30 02:04:24 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-30 02:04:45 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-30 01:02:46 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-30 02:25:26 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-30 02:05:32 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:14:31 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:01:17 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:13:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:56 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:00:44 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-30 01:08:18 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-30 01:01:48 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:56 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-30 01:09:11 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:03:28 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:03:29 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:16:07 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:47 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:05:02 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:02:12 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-30 02:05:00 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.005 |  |
| 2026-09-30 02:00:36 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.005 |  |
| 2026-09-30 02:05:20 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.005 |  |
| 2026-09-30 01:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.010 |  |
| 2026-09-30 02:00:50 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | -0.010 |  |
| 2026-09-30 02:03:55 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-09-30 02:04:41 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-09-30 02:07:33 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-09-30 02:01:41 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.033 |  |
| 2026-09-30 02:19:18 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.033 |  |
| 2026-09-30 02:05:14 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.039 |  |
| 2026-09-30 02:07:25 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)