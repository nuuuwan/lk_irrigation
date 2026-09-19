# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_16:09:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,279 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 16:09:47 | Magura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-09-19 16:08:06 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.019 |  |
| 2026-09-19 16:07:56 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.045 |  |
| 2026-09-19 16:07:29 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:07:13 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:07:07 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:06:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-19 16:06:30 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-19 16:06:15 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-19 16:05:55 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:05:30 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:05:27 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-09-19 16:05:20 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-19 16:04:47 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:04:38 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:04:36 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-09-19 16:04:20 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-09-19 16:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 16:03:52 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 16:03:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:03:22 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:03:17 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:03:01 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-09-19 16:02:57 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:48 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-19 16:02:46 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:40 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:33 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 16:02:28 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-09-19 16:02:19 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:16 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.072 |  |
| 2026-09-19 16:02:03 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:01:55 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:01:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:01:34 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 16:06:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-19 16:06:15 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-19 16:06:30 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-19 16:03:52 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 16:02:33 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 16:05:20 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-19 16:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 16:02:19 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:01:55 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:01:34 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:07:07 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:01:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:03:22 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:03:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:03 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:03:17 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:05:55 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:04:38 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:05:30 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:07:29 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:07:13 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:04:47 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:46 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:02:40 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:06:18 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:04:36 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-09-19 16:04:20 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-09-19 16:02:48 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-19 15:01:07 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-09-19 16:08:06 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.019 |  |
| 2026-09-19 16:05:27 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-09-19 16:09:47 | Magura (Kalu Ganga) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-09-19 16:02:28 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-09-19 13:07:37 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.037 |  |
| 2026-09-19 16:03:01 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-09-19 16:07:56 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.045 |  |
| 2026-09-19 16:02:16 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)