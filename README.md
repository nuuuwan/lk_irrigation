# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_16:16:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,796 measurements** from **39** stations.
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
| 2026-09-14 16:16:12 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:14:26 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:13:40 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-09-14 16:10:07 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.039 |  |
| 2026-09-14 16:10:06 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 16:09:31 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:09:22 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-14 16:09:20 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-14 16:08:25 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.029 |  |
| 2026-09-14 16:08:10 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-14 16:08:09 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:06:28 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:06:28 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-14 16:06:09 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.039 |  |
| 2026-09-14 16:05:43 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-14 16:05:43 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 16:05:29 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-14 16:05:04 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:05:04 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:04:58 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-09-14 16:04:49 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-09-14 16:04:21 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:04:12 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | -0.010 |  |
| 2026-09-14 16:03:37 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:03:31 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-14 16:03:27 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-09-14 16:02:57 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-14 16:02:52 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-09-14 16:02:25 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:02:14 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:02:01 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 16:01:47 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-14 16:01:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:01:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 16:00:55 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:00:51 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-14 16:00:18 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 16:09:22 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-14 16:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-09-14 16:01:47 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-14 16:02:57 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-14 16:06:28 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-14 16:08:10 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-14 16:05:29 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-14 16:05:43 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-14 16:00:51 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-14 16:01:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 16:02:01 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 16:05:43 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 16:10:06 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 16:02:25 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:02:52 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:01:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:27:09 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:14:26 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:09:31 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:02:14 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:03:27 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:16:12 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:05:04 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:04:21 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:00:18 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:05:04 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:03:37 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:06:28 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:00:55 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:08:09 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 16:13:40 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-09-14 16:04:49 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-09-14 16:03:31 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-14 16:04:12 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | -0.010 |  |
| 2026-09-14 16:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-09-14 16:04:58 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-09-14 16:08:25 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.029 |  |
| 2026-09-14 16:06:09 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.039 |  |
| 2026-09-14 16:10:07 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)