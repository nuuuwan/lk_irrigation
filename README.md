# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_00:22:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 00:22:56 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.037 |  |
| 2026-09-16 00:18:22 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:18:18 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:17:18 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-16 00:15:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:15:04 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:11:35 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:10:09 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-16 00:10:05 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.294 |  |
| 2026-09-16 00:08:34 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:08:32 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-16 00:08:23 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | -18.000 |  |
| 2026-09-16 00:08:21 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -18.000 |  |
| 2026-09-16 00:08:20 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -18.000 |  |
| 2026-09-16 00:07:07 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:06:57 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-09-16 00:06:54 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.037 |  |
| 2026-09-16 00:06:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.049 |  |
| 2026-09-16 00:05:38 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.019 |  |
| 2026-09-16 00:05:36 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-16 00:05:34 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-09-16 00:05:32 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-16 00:05:14 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:04:55 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-16 00:03:44 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:03:26 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | -0.023 |  |
| 2026-09-16 00:03:23 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.052 |  |
| 2026-09-16 00:03:18 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.070 |  |
| 2026-09-16 00:02:57 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | -0.079 |  |
| 2026-09-16 00:02:51 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-09-16 00:02:45 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-16 00:02:29 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.117 |  |
| 2026-09-16 00:02:25 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 00:01:56 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:01:27 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-16 00:01:24 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-16 00:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:01:15 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:00:43 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.084 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 00:05:34 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-09-16 00:01:24 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-16 00:10:09 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-16 00:04:55 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-16 00:01:27 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-16 00:05:32 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-16 00:05:36 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-16 00:08:32 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-16 00:02:25 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 00:17:18 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-15 23:48:17 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.004 |  |
| 2026-09-16 00:11:35 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:15:04 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:18:22 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:07:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:07:07 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:01:15 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:01:56 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:05:14 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:15:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:18:18 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 00:08:34 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-16 00:02:45 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-16 00:05:38 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.019 |  |
| 2026-09-16 00:02:51 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-09-16 00:03:26 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | -0.023 |  |
| 2026-09-16 00:22:56 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.037 |  |
| 2026-09-16 00:06:57 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-09-15 18:02:40 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.039 |  |
| 2026-09-16 00:06:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.049 |  |
| 2026-09-16 00:03:23 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.052 |  |
| 2026-09-16 00:03:18 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.070 |  |
| 2026-09-16 00:02:57 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | -0.079 |  |
| 2026-09-16 00:00:43 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.084 |  |
| 2026-09-16 00:02:29 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.117 |  |
| 2026-09-16 00:10:05 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.294 |  |
| 2026-09-16 00:08:23 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)