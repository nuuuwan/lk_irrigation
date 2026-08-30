# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_01:22:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 01:22:22 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.008 |  |
| 2026-08-31 01:13:19 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.026 |  |
| 2026-08-31 01:12:44 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-08-31 01:08:55 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.028 |  |
| 2026-08-31 01:08:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-08-31 01:06:56 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-08-31 01:06:43 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-08-31 01:05:45 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-08-31 01:05:29 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.029 |  |
| 2026-08-31 01:05:10 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-08-31 01:05:03 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:04:56 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-08-31 01:04:52 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:04:45 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:04:34 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-08-31 01:04:15 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-31 01:03:02 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.147 |  |
| 2026-08-31 01:02:52 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:49 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:34 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:32 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:30 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-31 01:02:22 | Manampitiya (Mahaweli Ganga) | -0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:01:43 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:01:10 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.011 |  |
| 2026-08-31 01:00:50 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:00:43 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 01:08:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-08-31 01:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-30 18:04:01 | Weraganthota (Mahaweli Ganga) | -3.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 01:00:50 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-31 00:00:55 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:32 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 00:04:51 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:04:45 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-31 00:03:03 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:34 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:00:43 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:13 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 23:07:21 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:04:15 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:04:52 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.000 |  |
| 2026-08-30 23:02:48 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:49 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 00:02:44 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:22 | Manampitiya (Mahaweli Ganga) | -0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:36 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:02:52 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:01:43 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:05:03 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-31 01:22:22 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.008 |  |
| 2026-08-31 01:12:44 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-08-31 01:06:43 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-08-31 01:05:45 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-08-31 01:02:30 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-31 01:04:34 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-08-31 01:04:56 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-08-31 01:01:10 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.011 |  |
| 2026-08-31 01:06:56 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-08-31 01:05:10 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-08-31 01:13:19 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.026 |  |
| 2026-08-31 01:08:55 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.028 |  |
| 2026-08-31 01:05:29 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.029 |  |
| 2026-08-30 22:13:26 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.091 |  |
| 2026-08-31 01:03:02 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)