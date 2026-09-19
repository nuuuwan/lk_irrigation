# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_07:15:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,924 measurements** from **39** stations.
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
| 2026-09-19 07:15:02 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.025 |  |
| 2026-09-19 07:15:02 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:13:47 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.033 |  |
| 2026-09-19 07:10:29 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-09-19 07:09:42 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-19 07:07:53 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-19 07:07:04 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:07:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:06:57 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.009 |  |
| 2026-09-19 07:06:35 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-09-19 07:06:08 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:05:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:05:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:04:57 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 07:04:14 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | -0.071 |  |
| 2026-09-19 07:04:04 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.117 |  |
| 2026-09-19 07:03:27 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.011 |  |
| 2026-09-19 07:03:10 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.002 |  |
| 2026-09-19 07:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-19 07:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2026-09-19 07:02:49 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:02:40 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-19 07:02:39 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.022 |  |
| 2026-09-19 07:02:37 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-09-19 07:02:31 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-09-19 07:02:19 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 07:02:18 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.050 |  |
| 2026-09-19 07:02:06 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 07:02:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:02:05 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-09-19 07:01:22 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-19 07:01:17 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:01:14 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 07:01:01 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:00:32 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:00:29 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:00:24 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-19 06:58:26 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 07:01:22 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-19 07:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-19 07:02:40 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-19 07:04:57 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 07:07:53 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-19 07:02:06 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 07:01:14 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 07:02:19 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 07:09:42 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-19 07:03:10 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.002 |  |
| 2026-09-19 07:02:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:00:29 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:15:02 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:58:26 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:05:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:05:38 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:07:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:00:32 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:07:04 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:02:49 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:06:08 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 07:01:17 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:11:40 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | -0.001 |  |
| 2026-09-19 07:06:57 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.009 |  |
| 2026-09-19 07:00:24 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-19 07:10:29 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-09-19 07:03:27 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.011 |  |
| 2026-09-19 07:06:35 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-09-19 07:02:05 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-09-19 07:02:37 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-09-19 07:02:39 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.022 |  |
| 2026-09-19 07:15:02 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.025 |  |
| 2026-09-19 07:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.029 |  |
| 2026-09-19 07:02:31 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.031 |  |
| 2026-09-19 07:13:47 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.033 |  |
| 2026-09-19 06:00:21 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.033 |  |
| 2026-09-19 07:02:18 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.050 |  |
| 2026-09-19 07:04:14 | Glencourse (Kelani Ganga) | 10.06 | 🟢 Normal | -0.071 |  |
| 2026-09-19 07:04:04 | Magura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)