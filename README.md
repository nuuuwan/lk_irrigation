# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_08:11:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,868 measurements** from **39** stations.
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
| 2026-08-31 08:11:16 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:10:36 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:09:49 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:09:15 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-08-31 08:07:56 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 08:07:32 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 08:07:27 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:06:56 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-08-31 08:06:42 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-08-31 08:06:01 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-31 08:05:24 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:05:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:05:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.153 |  |
| 2026-08-31 08:05:07 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-08-31 08:04:35 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:04:22 | Manampitiya (Mahaweli Ganga) | -0.47 | 🟢 Normal | -0.039 |  |
| 2026-08-31 08:04:05 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:04:00 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-08-31 08:03:58 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:03:51 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:03:50 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:03:37 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:03:37 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:03:29 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:03:05 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.103 |  |
| 2026-08-31 08:02:24 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:02:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:02:06 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:02:05 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:01:32 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:01:20 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:01:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:01:06 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:00:41 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:00:39 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 08:09:15 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-08-31 08:06:01 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-31 07:12:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-31 08:07:56 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 08:00:39 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 08:07:32 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 08:01:20 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:11:56 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:05:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:02:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:45 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:03:37 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:02:05 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:02:24 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:01:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:03:50 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:04:35 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:03:51 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:04:05 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:02:06 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:01:06 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:10:36 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:05:24 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:03:58 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-31 08:07:27 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:11:16 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:03:29 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:00:41 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:09:49 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:03:37 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-08-31 08:06:56 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-08-31 08:05:07 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-08-31 08:04:00 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-08-31 08:06:42 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-08-31 08:04:22 | Manampitiya (Mahaweli Ganga) | -0.47 | 🟢 Normal | -0.039 |  |
| 2026-08-31 07:01:24 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-31 08:03:05 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.103 |  |
| 2026-08-31 08:05:12 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)