# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_21:12:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,085 measurements** from **39** stations.
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
| 2026-09-13 21:12:28 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-09-13 21:11:20 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-13 21:11:00 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.026 |  |
| 2026-09-13 21:09:52 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-09-13 21:09:33 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:09:32 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 21:09:20 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-13 21:09:12 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-13 21:08:50 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:06:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:06:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 21:06:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-09-13 21:06:19 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-13 21:05:22 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-09-13 21:04:58 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-09-13 21:04:42 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:04:35 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-13 21:04:02 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.060 |  |
| 2026-09-13 21:03:58 | Magura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 21:03:49 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:03:37 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:03:31 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.045 |  |
| 2026-09-13 21:03:20 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:03:15 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-09-13 21:02:38 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:02:36 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-09-13 21:02:29 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:02:19 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:02:05 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.061 |  |
| 2026-09-13 21:01:24 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 21:01:11 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 21:00:58 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:00:51 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:00:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 21:04:58 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-09-13 21:06:19 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-13 21:09:20 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-13 21:11:20 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-13 21:09:12 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-13 21:03:58 | Magura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 21:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 21:06:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 21:01:11 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 21:09:32 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:02:38 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:00:51 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:08:50 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:09:33 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:03:49 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:02:19 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:00:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:03:37 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 20:09:33 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:00:58 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:03:20 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:04:42 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:01:24 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:06:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:02:29 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 21:09:52 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-09-13 21:04:35 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-13 21:05:22 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-09-13 21:06:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-09-13 21:02:36 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-09-13 21:12:28 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-09-13 21:11:00 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.026 |  |
| 2026-09-13 21:03:31 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.045 |  |
| 2026-09-13 21:03:15 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-09-13 21:04:02 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.060 |  |
| 2026-09-13 21:02:05 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)