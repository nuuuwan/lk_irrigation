# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_07:15:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,856 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 07:15:36 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:13:59 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:12:46 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:12:43 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-25 07:12:28 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:10:07 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-25 07:09:44 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.080 |  |
| 2026-08-25 07:09:27 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.009 |  |
| 2026-08-25 07:09:18 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-25 07:08:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:08:17 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-25 07:07:00 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.059 |  |
| 2026-08-25 07:06:18 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.018 |  |
| 2026-08-25 07:05:46 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-08-25 07:05:30 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.163 |  |
| 2026-08-25 07:05:24 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:04:50 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:04:31 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 07:04:22 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:04:01 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:03:26 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 07:03:03 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 07:03:02 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.089 |  |
| 2026-08-25 07:02:50 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 07:02:36 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 07:02:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 07:02:04 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:01:30 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.060 |  |
| 2026-08-25 07:01:25 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.120 |  |
| 2026-08-25 07:01:20 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:01:17 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 07:01:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:01:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.033 |  |
| 2026-08-25 07:01:01 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 07:00:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:00:27 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:00:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:59:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 07:01:17 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 07:10:07 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-25 07:09:18 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-25 07:02:50 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 07:02:36 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 07:04:31 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 07:08:17 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-25 07:12:43 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-25 07:03:26 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 07:02:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 07:03:03 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 07:01:01 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 07:03:02 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:59:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:12:46 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:01:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:04:50 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:04:01 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:13:59 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:05:24 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:08:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:02:04 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:00:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:04:22 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:15:36 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:01:20 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:00:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:00:27 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:09:27 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | -0.009 |  |
| 2026-08-25 07:06:18 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.018 |  |
| 2026-08-25 07:05:46 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-08-25 06:06:01 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-08-25 07:01:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.033 |  |
| 2026-08-25 07:07:00 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.059 |  |
| 2026-08-25 07:01:30 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.060 |  |
| 2026-08-25 07:09:44 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.080 |  |
| 2026-08-25 07:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.089 |  |
| 2026-08-25 07:01:25 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.120 |  |
| 2026-08-25 07:05:30 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)