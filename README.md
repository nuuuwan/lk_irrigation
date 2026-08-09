# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_19:17:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,016 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 19:17:11 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.031 |  |
| 2026-08-09 19:12:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-09 19:10:44 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-08-09 19:10:14 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.026 |  |
| 2026-08-09 19:09:26 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.018 |  |
| 2026-08-09 19:08:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:08:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:07:41 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:07:25 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 19:06:42 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.019 |  |
| 2026-08-09 19:06:01 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:05:17 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:05:13 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:05:11 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 19:05:02 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-09 19:04:51 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:04:47 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-09 19:04:44 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-08-09 19:04:12 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.030 |  |
| 2026-08-09 19:03:53 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-08-09 19:03:44 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:03:37 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-09 19:02:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-08-09 19:02:32 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.035 |  |
| 2026-08-09 19:02:29 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-09 19:02:23 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-09 19:02:13 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:48 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:47 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:26 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:02 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:01 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:00:55 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:00:21 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-09 19:00:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:00:11 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 19:10:44 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-08-09 19:03:53 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-08-09 19:05:02 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-09 19:00:21 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-09 19:03:37 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-09 19:02:23 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-09 19:02:29 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-09 19:07:25 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 19:12:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 19:05:11 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 19:05:13 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:08:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:08:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:00:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:02:13 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:00:55 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:04:51 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:26 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:02 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:47 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:07:41 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:05:17 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:06:01 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:03:44 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:48 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:01:01 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-09 19:04:44 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-08-09 19:04:47 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-09 19:00:11 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-09 19:09:26 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.018 |  |
| 2026-08-09 19:06:42 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.019 |  |
| 2026-08-09 19:10:14 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.026 |  |
| 2026-08-09 19:04:12 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.030 |  |
| 2026-08-09 19:17:11 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.031 |  |
| 2026-08-09 19:02:32 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.035 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-09 19:02:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)