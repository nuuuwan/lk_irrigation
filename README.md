# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_06:16:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,094 measurements** from **39** stations.
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
| 2026-09-17 06:16:52 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.008 |  |
| 2026-09-17 06:13:08 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-17 06:12:02 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-17 06:08:49 | Baddegama (Gin Ganga) | 3.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 06:08:19 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.009 |  |
| 2026-09-17 06:08:16 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-09-17 06:08:04 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.023 |  |
| 2026-09-17 06:07:33 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 06:06:20 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.076 |  |
| 2026-09-17 06:05:45 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.058 |  |
| 2026-09-17 06:05:35 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-17 06:05:30 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:04:45 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:04:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:04:20 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-17 06:03:57 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-17 06:03:25 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 06:02:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-17 06:02:46 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 06:02:40 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:02:27 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-09-17 06:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:02:20 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-09-17 06:02:18 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:02:18 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:01:59 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.042 |  |
| 2026-09-17 06:01:37 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-17 06:01:35 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-09-17 06:01:34 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.031 |  |
| 2026-09-17 06:01:17 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.234 |  |
| 2026-09-17 06:01:08 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:01:04 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:00:56 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-09-17 06:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-17 06:00:48 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-17 06:00:29 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.300 |  |
| 2026-09-17 05:48:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.61 | 🟢 Normal | -0.234 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 06:02:27 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-09-17 06:05:35 | Magura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-17 06:13:08 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-17 06:02:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-17 06:04:20 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-17 06:02:46 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-17 06:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-17 06:08:49 | Baddegama (Gin Ganga) | 3.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-17 06:12:02 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-17 06:03:25 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-17 06:00:48 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-17 06:07:33 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-17 06:00:56 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-09-17 06:01:17 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:01:04 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:02:18 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:04:45 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:01:08 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:05:30 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:02:40 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:04:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:02:18 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 06:16:52 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.008 |  |
| 2026-09-17 06:08:19 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.009 |  |
| 2026-09-17 06:03:57 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-17 06:08:16 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.019 |  |
| 2026-09-17 06:01:37 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-17 06:01:35 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-09-17 06:08:04 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.023 |  |
| 2026-09-17 06:02:20 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-09-17 06:01:34 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.031 |  |
| 2026-09-17 06:01:59 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.042 |  |
| 2026-09-17 06:05:45 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.058 |  |
| 2026-09-17 06:06:20 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.076 |  |
| 2026-09-17 06:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | -0.234 |  |
| 2026-09-17 06:00:29 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)