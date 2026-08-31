# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_11:13:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 11:13:23 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:12:12 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:11:42 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-08-31 11:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.073 |  |
| 2026-08-31 11:09:22 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-08-31 11:09:19 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:08:53 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:08:36 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-31 11:06:49 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-31 11:06:45 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:06:21 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.120 |  |
| 2026-08-31 11:06:11 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:05:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:04:30 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.010 |  |
| 2026-08-31 11:04:21 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:04:18 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:04:12 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:04:11 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:42 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:42 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-08-31 11:03:41 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.108 |  |
| 2026-08-31 11:03:11 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:10 | Manampitiya (Mahaweli Ganga) | -0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:08 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:08 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:07 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:02:42 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:02:39 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-08-31 11:02:22 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-31 11:02:14 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:02:03 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:01:56 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:01:46 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-08-31 11:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:01:44 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-31 11:01:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:01:42 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:01:34 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-31 11:01:21 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.120 |  |
| 2026-08-31 11:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:00:23 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.078 |  |
| 2026-08-31 11:00:22 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 10:59:16 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 11:08:36 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-31 11:02:22 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-31 11:01:34 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-31 11:06:49 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-31 11:01:42 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:00:22 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:08 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:01:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:05:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:09:19 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:12:12 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:02:14 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:08 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:06:11 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:01:56 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:02:03 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:04:21 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:08:53 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:42 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:10 | Manampitiya (Mahaweli Ganga) | -0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:04:11 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:13:23 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:07 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:06:45 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:03:11 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 11:04:30 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.010 |  |
| 2026-08-31 11:01:46 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-08-31 11:03:42 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-08-31 11:01:44 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-31 11:11:42 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-08-31 11:09:22 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-08-31 11:02:39 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-08-31 11:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.073 |  |
| 2026-08-31 11:00:23 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.078 |  |
| 2026-08-31 11:03:41 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.108 |  |
| 2026-08-31 11:06:21 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)