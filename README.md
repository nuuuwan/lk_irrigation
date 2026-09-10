# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_22:04:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **257,427 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 22:04:27 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:04:24 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-09-10 22:04:18 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:04:14 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-10 22:04:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:04:06 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.041 |  |
| 2026-09-10 22:03:40 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:03:28 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-09-10 22:03:19 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:59 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:58 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:52 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-09-10 22:02:46 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-10 22:02:43 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:43 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:01:50 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-09-10 22:01:34 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:01:22 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:01:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:01:15 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:00:45 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 22:00:38 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:00:18 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 21:58:11 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 22:01:50 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-09-10 22:02:46 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-10 21:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-10 22:04:14 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-10 22:00:45 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 21:01:13 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 22:00:18 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:49 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:01:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:59 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:00:38 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 18:02:58 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 21:09:09 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:52 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:03:19 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-09-10 21:12:32 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-10 21:06:47 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:03:40 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:01:15 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:43 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:04:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:04:27 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:04:18 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:01:22 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:58 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-10 18:01:51 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 21:04:56 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:01:34 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:02:43 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-10 22:04:24 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-09-10 22:03:28 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-09-10 21:07:46 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.026 |  |
| 2026-09-10 21:04:40 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-09-10 20:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.037 |  |
| 2026-09-10 22:02:46 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-09-10 22:04:06 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.041 |  |
| 2026-09-10 21:07:39 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.048 |  |
| 2026-09-10 18:00:21 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |
| 2026-09-10 21:13:05 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.794 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)