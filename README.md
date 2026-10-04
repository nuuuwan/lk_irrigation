# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_01:25:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,138 measurements** from **39** stations.
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
| 2026-10-05 01:25:31 | Holombuwa (Kelani Ganga) | 1.39 | 🟢 Normal | -0.041 |  |
| 2026-10-05 01:20:36 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -576.000 |  |
| 2026-10-05 01:20:35 | Magura (Kalu Ganga) | 2.76 | 🟢 Normal | -576.000 |  |
| 2026-10-05 01:20:34 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | -576.000 |  |
| 2026-10-05 01:18:35 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-10-05 01:16:48 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.056 |  |
| 2026-10-05 01:13:45 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 01:09:35 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 01:07:07 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-05 01:05:57 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-05 01:05:45 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-05 01:04:46 | Glencourse (Kelani Ganga) | 12.81 | 🟢 Normal | -0.097 |  |
| 2026-10-05 01:04:43 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.098 |  |
| 2026-10-05 01:03:46 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 01:03:41 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-10-05 01:03:31 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-10-05 01:03:07 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:02:53 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-05 01:02:51 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-05 01:02:44 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:02:42 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 01:02:34 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-05 01:02:32 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:01:29 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:01:23 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:00:49 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-05 01:00:19 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 01:03:41 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-10-05 01:05:57 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-05 00:08:13 | Peradeniya (Mahaweli Ganga) | 3.96 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-10-05 01:02:53 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-04 23:02:35 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-05 01:02:34 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-05 01:07:07 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-05 01:05:45 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-05 01:02:51 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-05 01:09:35 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 01:00:19 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-05 01:13:45 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 01:02:42 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 00:05:16 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-04 18:03:37 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 01:03:46 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 00:03:46 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:01:29 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:00:49 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:18 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:01:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:06:07 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:00:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:03:07 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:02:44 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 00:02:31 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 01:01:23 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-04 18:00:10 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-05 00:12:50 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.017 |  |
| 2026-10-05 01:03:31 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-10-04 23:01:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.022 |  |
| 2026-10-05 00:08:19 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-10-05 01:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-05 01:25:31 | Holombuwa (Kelani Ganga) | 1.39 | 🟢 Normal | -0.041 |  |
| 2026-10-05 01:18:35 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.041 |  |
| 2026-10-05 01:16:48 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.056 |  |
| 2026-10-05 01:04:46 | Glencourse (Kelani Ganga) | 12.81 | 🟢 Normal | -0.097 |  |
| 2026-10-05 01:04:43 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.098 |  |
| 2026-10-05 01:20:36 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)