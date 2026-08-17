# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_13:17:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,941 measurements** from **39** stations.
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
| 2026-08-17 13:17:08 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:12:25 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:12:00 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:07:12 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.018 |  |
| 2026-08-17 13:06:33 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:06:16 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-08-17 13:06:03 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-08-17 13:05:42 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:05:42 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:05:21 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 13:04:41 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:04:28 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:04:26 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:04:10 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-08-17 13:04:02 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:03:56 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.078 |  |
| 2026-08-17 13:03:44 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 13:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-08-17 13:03:23 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:03:15 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-08-17 13:03:13 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 13:03:04 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:02:59 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 13:02:56 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-08-17 13:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-08-17 13:02:29 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-08-17 13:02:23 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:02:22 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:02:12 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:53 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.041 |  |
| 2026-08-17 13:01:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:30 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:25 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-08-17 13:01:22 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:05 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 13:01:03 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 13:00:56 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:00:17 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 13:02:56 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-08-17 13:03:13 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 13:05:21 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 13:01:05 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 13:03:44 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 13:01:03 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 13:02:59 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 13:02:12 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:00:17 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:04:41 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:03:23 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:17:08 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:30 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:12:00 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:04:28 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:05:42 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:03:04 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:06:33 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:00:56 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:01:22 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:02:23 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:04:26 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:04:02 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:05:42 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:12:25 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:02:22 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 13:04:10 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-08-17 13:06:16 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-08-17 13:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-08-17 13:01:25 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-08-17 13:07:12 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.018 |  |
| 2026-08-17 13:06:03 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-08-17 13:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-08-17 13:02:29 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-08-17 13:01:53 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.041 |  |
| 2026-08-17 13:03:15 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-08-17 13:03:56 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)