# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_14:13:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,979 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 14:13:25 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:13:19 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:11:41 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-17 14:10:50 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:10:37 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 14:08:20 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:08:09 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 14:08:05 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.018 |  |
| 2026-08-17 14:06:16 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-17 14:05:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-17 14:05:28 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:05:24 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 14:05:11 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 14:04:55 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:04:27 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 14:04:24 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:03:48 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:03:41 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:03:40 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:03:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-17 14:02:52 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:02:38 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-17 14:02:38 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:02:20 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:02:09 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:57 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 14:01:52 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.041 |  |
| 2026-08-17 14:01:51 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 14:01:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:30 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-08-17 14:01:27 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:24 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:23 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:12 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.033 |  |
| 2026-08-17 14:00:15 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:00:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 14:05:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-17 14:03:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-17 14:02:38 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-17 14:11:41 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-17 14:01:51 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 14:01:57 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 14:04:27 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 14:05:11 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 14:08:09 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 14:05:24 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 14:10:37 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 14:05:28 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:00:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:02:20 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:00:15 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:10:50 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:05:42 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:13:25 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:03:40 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:03:41 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:02:09 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:08:20 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:23 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:05:42 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:24 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:01:27 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:04:55 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:02:52 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:04:24 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:03:48 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:02:38 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-08-17 14:01:30 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-08-17 14:08:05 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.018 |  |
| 2026-08-17 14:06:16 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-17 14:01:12 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.033 |  |
| 2026-08-17 14:01:52 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)