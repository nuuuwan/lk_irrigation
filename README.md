# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_06:08:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,979 measurements** from **39** stations.
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
| 2026-08-14 06:08:58 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-14 06:08:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:07:36 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.009 |  |
| 2026-08-14 06:06:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.102 |  |
| 2026-08-14 06:06:39 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-08-14 06:05:47 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:05:12 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-14 06:05:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:04:53 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:04:43 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:04:38 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:04:14 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-08-14 06:04:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:03:45 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-08-14 06:03:41 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:02:46 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-14 06:02:37 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 06:02:35 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:02:33 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:02:19 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-14 06:01:56 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:49 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.054 |  |
| 2026-08-14 06:01:49 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.012 |  |
| 2026-08-14 06:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-08-14 06:01:42 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:41 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:35 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:32 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:07 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-08-14 06:01:01 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:00:24 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-14 06:00:19 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.026 |  |
| 2026-08-14 06:00:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:31:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.102 |  |
| 2026-08-14 05:26:17 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 06:05:12 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-14 06:02:19 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-14 05:01:08 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-14 06:00:24 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-14 06:08:58 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-14 06:02:37 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-14 06:02:33 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:02:35 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:05:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:26:17 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:03:41 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:04:38 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:13:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:41 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:44 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:01:16 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:00:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:04:53 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:05:47 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:56 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:04:43 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:32 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:04:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:35 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:01 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:08:30 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:01:42 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-14 06:07:36 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.009 |  |
| 2026-08-14 06:02:46 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-14 06:04:14 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-08-14 06:01:07 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-08-14 06:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-08-14 06:01:49 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.012 |  |
| 2026-08-14 06:03:45 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-08-14 06:00:19 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.026 |  |
| 2026-08-14 06:06:39 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-08-14 06:01:49 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.054 |  |
| 2026-08-14 06:06:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)