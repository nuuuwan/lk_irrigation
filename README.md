# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_03:16:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,889 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 03:16:03 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:15:20 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.017 |  |
| 2026-09-08 03:13:05 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-08 03:08:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-09-08 03:06:35 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 03:05:53 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 03:05:01 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:04:47 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:04:30 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:04:03 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 03:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-08 03:03:42 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 03:03:24 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:03:22 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.090 |  |
| 2026-09-08 03:03:07 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.085 |  |
| 2026-09-08 03:03:05 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-08 03:02:46 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:24 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:22 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-08 03:02:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:20 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-08 03:02:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:02 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:01:58 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-09-08 03:01:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:01:38 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-08 03:00:56 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 03:02:22 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-08 03:02:20 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-08 03:13:05 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-08 03:01:38 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-08 00:07:37 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-08 03:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 18:10:27 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-08 03:03:42 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 03:04:03 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 03:05:53 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 03:06:35 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 03:16:03 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:00:56 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:24 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:51 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:02 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 18:04:43 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:05:01 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:06:16 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:01:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:03:24 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:02:46 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-08 03:04:47 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:06:57 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-08 02:20:31 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:31:53 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-09-08 02:10:57 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-09-08 02:07:05 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-09-08 03:03:05 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-08 03:15:20 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.017 |  |
| 2026-09-08 03:01:58 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-09-08 03:08:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.033 |  |
| 2026-09-07 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.050 |  |
| 2026-09-08 03:03:07 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.085 |  |
| 2026-09-08 03:03:22 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.090 |  |
| 2026-09-08 02:04:06 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)