# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_19:15:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,907 measurements** from **39** stations.
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
| 2026-08-10 19:15:11 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:11:46 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.008 |  |
| 2026-08-10 19:11:33 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.039 |  |
| 2026-08-10 19:08:48 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:08:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:08:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:08:18 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.063 |  |
| 2026-08-10 19:07:07 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.056 |  |
| 2026-08-10 19:06:50 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.080 |  |
| 2026-08-10 19:06:12 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:05:53 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 19:05:33 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.028 |  |
| 2026-08-10 19:05:17 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:04:55 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-08-10 19:04:50 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:04:09 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.029 |  |
| 2026-08-10 19:03:46 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 19:03:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:03:37 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-10 19:03:23 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:03:20 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:03:17 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:02:53 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.020 |  |
| 2026-08-10 19:02:47 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-08-10 19:02:08 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.061 |  |
| 2026-08-10 19:01:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-08-10 19:01:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:01:35 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.020 |  |
| 2026-08-10 19:01:26 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:01:07 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:00:52 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:00:52 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:00:45 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-10 19:00:08 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 18:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-10 19:03:46 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 19:05:53 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 19:02:47 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:00:08 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:01:26 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:01:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:03:23 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:00:52 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:02:17 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:03:20 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:03:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:04:50 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:08:48 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:08:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:05:17 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:08:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:15:11 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:03:17 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:01:07 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:00:52 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 19:11:46 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.008 |  |
| 2026-08-10 19:03:37 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-10 19:00:45 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-10 19:01:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-08-10 19:04:55 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-08-10 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-10 19:01:35 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.020 |  |
| 2026-08-10 19:02:53 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.020 |  |
| 2026-08-10 19:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-08-10 19:05:33 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.028 |  |
| 2026-08-10 19:04:09 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.029 |  |
| 2026-08-10 18:00:40 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-08-10 19:11:33 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.039 |  |
| 2026-08-10 19:07:07 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.056 |  |
| 2026-08-10 19:02:08 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.061 |  |
| 2026-08-10 19:08:18 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.063 |  |
| 2026-08-10 19:06:50 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)