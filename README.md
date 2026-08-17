# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_09:11:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,781 measurements** from **39** stations.
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
| 2026-08-17 09:11:29 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-17 09:06:43 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.009 |  |
| 2026-08-17 09:06:04 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:05:38 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:05:25 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.091 |  |
| 2026-08-17 09:05:22 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:05:12 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-17 09:05:08 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:05:00 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:04:49 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:04:49 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-17 09:04:48 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:04:19 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-17 09:04:16 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:04:13 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-17 09:04:07 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 09:03:44 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.050 |  |
| 2026-08-17 09:03:27 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:27 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:24 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:20 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:20 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | -0.049 |  |
| 2026-08-17 09:03:00 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:02:58 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.125 |  |
| 2026-08-17 09:02:30 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-08-17 09:02:21 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:02:13 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 09:01:58 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:01:48 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.039 |  |
| 2026-08-17 09:01:46 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:01:39 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:01:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 09:01:07 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:00:42 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 09:04:19 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-17 09:11:29 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-17 09:05:12 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-17 09:04:13 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-17 08:08:36 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 09:04:49 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-17 09:04:07 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 09:02:13 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 09:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 09:01:58 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:27 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:01:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:04:49 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:05:22 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:06:04 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:04:48 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:24 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:05:38 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:27 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:20 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:05:00 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:05:08 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:03:20 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:00:42 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-17 08:06:02 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:04:16 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:01:46 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 09:06:43 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.009 |  |
| 2026-08-17 09:02:21 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:01:39 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:03:00 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:01:07 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-17 09:02:30 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-08-17 08:09:51 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.026 |  |
| 2026-08-17 09:01:48 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.039 |  |
| 2026-08-17 09:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | -0.049 |  |
| 2026-08-17 09:03:44 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.050 |  |
| 2026-08-17 09:05:25 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.091 |  |
| 2026-08-17 09:02:58 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)