# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_06:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,886 measurements** from **39** stations.
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
| 2026-09-19 06:13:45 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:12:40 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | -2.250 |  |
| 2026-09-19 06:12:24 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -2.250 |  |
| 2026-09-19 06:12:09 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | -2.250 |  |
| 2026-09-19 06:11:40 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | -0.001 |  |
| 2026-09-19 06:08:13 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:08:11 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.031 |  |
| 2026-09-19 06:06:58 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.010 |  |
| 2026-09-19 06:06:54 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:06:52 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 06:06:51 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-19 06:06:29 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:05:47 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:05:32 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.033 |  |
| 2026-09-19 06:05:28 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.057 |  |
| 2026-09-19 06:04:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:04:23 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 06:04:20 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-19 06:04:14 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:04:14 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.049 |  |
| 2026-09-19 06:04:10 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.014 |  |
| 2026-09-19 06:03:43 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:03:32 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:03:10 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:02:32 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.308 |  |
| 2026-09-19 06:02:22 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.040 |  |
| 2026-09-19 06:02:14 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:02:08 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-19 06:02:07 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-19 06:01:59 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 06:01:52 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:01:47 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:01:38 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.031 |  |
| 2026-09-19 06:01:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-09-19 06:01:20 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:01:16 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.075 |  |
| 2026-09-19 06:00:52 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:00:42 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.070 |  |
| 2026-09-19 06:00:32 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:00:21 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.033 |  |
| 2026-09-19 05:53:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.230 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 06:01:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-09-19 06:04:20 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-19 06:06:51 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-19 06:02:07 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-19 06:04:23 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 06:06:52 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 06:01:59 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 06:01:20 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:00:42 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:00:32 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:04:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:03:10 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:06:29 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:05:47 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:08:13 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:00:52 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:04:14 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:03:32 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:06:54 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:01:52 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:13:45 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:01:47 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:02:14 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 06:11:40 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | -0.001 |  |
| 2026-09-19 06:06:58 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.010 |  |
| 2026-09-19 06:02:08 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-09-19 06:04:10 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.014 |  |
| 2026-09-19 06:01:38 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.031 |  |
| 2026-09-19 06:08:11 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.031 |  |
| 2026-09-19 06:00:21 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.033 |  |
| 2026-09-19 06:05:32 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.033 |  |
| 2026-09-19 06:02:22 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.040 |  |
| 2026-09-19 06:04:14 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.049 |  |
| 2026-09-19 06:05:28 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.057 |  |
| 2026-09-19 06:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.070 |  |
| 2026-09-19 06:01:16 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.075 |  |
| 2026-09-19 06:02:32 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.308 |  |
| 2026-09-19 06:12:40 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | -2.250 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)