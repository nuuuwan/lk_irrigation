# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_10:25:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,847 measurements** from **39** stations.
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
| 2026-08-07 10:25:57 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:25:19 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:13:31 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-07 10:11:31 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-07 10:10:34 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:09:36 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-08-07 10:09:12 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.045 |  |
| 2026-08-07 10:08:37 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.018 |  |
| 2026-08-07 10:07:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:07:34 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-07 10:06:00 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 10:05:41 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:05:36 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:05:29 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-07 10:05:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:04:49 | Glencourse (Kelani Ganga) | 11.26 | 🟢 Normal | -0.029 |  |
| 2026-08-07 10:04:32 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:04:15 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-07 10:04:12 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.009 |  |
| 2026-08-07 10:03:41 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.060 |  |
| 2026-08-07 10:03:19 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:03:04 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.030 |  |
| 2026-08-07 10:02:55 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-08-07 10:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:02:47 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.052 |  |
| 2026-08-07 10:02:44 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-08-07 10:02:29 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:02:28 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:02:04 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:01:39 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:01:36 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-08-07 10:01:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:01:28 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-07 10:01:11 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:00:56 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-08-07 10:00:48 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:00:10 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:00:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:59:33 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-07 10:09:36 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-08-07 10:05:29 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-07 10:13:31 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-07 10:04:15 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-07 10:07:34 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-07 10:01:28 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-07 10:06:00 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 10:05:41 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:00:48 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:01:32 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:00:10 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:10:34 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:07:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:02:29 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:01:39 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:04:32 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:05:36 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:02:28 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:00:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:03:19 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:05:26 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:02:04 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:01:11 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:25:57 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:04:26 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:25:19 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-08-07 10:04:12 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.009 |  |
| 2026-08-07 10:11:31 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-07 10:01:36 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-08-07 10:08:37 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.018 |  |
| 2026-08-07 10:02:44 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-08-07 10:02:55 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-08-07 10:00:56 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-08-07 10:04:49 | Glencourse (Kelani Ganga) | 11.26 | 🟢 Normal | -0.029 |  |
| 2026-08-07 10:03:04 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.030 |  |
| 2026-08-07 10:09:12 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.045 |  |
| 2026-08-07 10:02:47 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.052 |  |
| 2026-08-07 10:03:41 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)