# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_15:23:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,856 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 15:23:07 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:19:11 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-09-13 15:18:41 | Panadugama (Nilwala Ganga) | 0.29 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-09-13 15:14:23 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:09:27 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-09-13 15:08:57 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:08:06 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.190 |  |
| 2026-09-13 15:07:53 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-13 15:07:31 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:07:23 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-13 15:07:19 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:06:27 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-09-13 15:05:57 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-13 15:05:25 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-13 15:05:18 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:05:02 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:04:59 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:04:41 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-13 15:04:37 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-13 15:04:33 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.258 |  |
| 2026-09-13 15:04:31 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-13 15:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 15:04:15 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:03:59 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:03:29 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:03:19 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 15:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:02:34 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-09-13 15:02:31 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-09-13 15:02:29 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:02:27 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-09-13 15:02:18 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.097 |  |
| 2026-09-13 15:02:09 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-13 15:02:02 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:01:39 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-13 15:01:36 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:01:30 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:01:29 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.723 | 🔺 Rising |
| 2026-09-13 15:01:07 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:00:35 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 15:00:28 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 14:51:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.723 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 15:19:11 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-09-13 15:01:29 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.723 | 🔺 Rising |
| 2026-09-13 15:02:27 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-09-13 15:07:23 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-13 15:05:25 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-13 15:07:53 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-13 15:04:31 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-13 15:05:57 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-13 15:02:09 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-13 15:04:41 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-13 15:03:19 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 15:00:35 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 15:04:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 15:02:02 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:00:28 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:01:30 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:07:31 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:03:59 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:14:23 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:23:07 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:07:19 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:05:02 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:05:18 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:04:59 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:08:57 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:02:29 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:01:07 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:01:36 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:04:15 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-13 15:09:27 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-09-13 15:02:31 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-09-13 15:04:37 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-13 15:01:39 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-13 15:02:34 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-09-13 15:06:27 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-09-13 15:02:18 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.097 |  |
| 2026-09-13 15:08:06 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.190 |  |
| 2026-09-13 15:04:33 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.258 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)