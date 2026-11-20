# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_21:03:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,251 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 21:03:02 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 21:02:56 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:38 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:32 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:30 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:14 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.041 |  |
| 2026-11-20 21:02:09 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:01 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:52 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 21:01:46 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-20 21:01:43 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:37 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:24 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:00:21 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 21:00:20 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 20:19:03 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 20:06:23 | Thawalama (Gin Ganga) | 3.15 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-20 20:02:40 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-20 20:04:59 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-20 20:00:31 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-20 20:05:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-20 20:04:39 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-20 20:02:33 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 21:00:21 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 20:06:09 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-20 21:01:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 21:00:20 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 21:03:02 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 21:02:38 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:24 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 20:02:50 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:52 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-20 20:03:34 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 20:07:05 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:32 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 20:04:22 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:56 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:01 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:30 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-20 20:09:22 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:37 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:01:43 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-20 21:02:09 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-20 20:04:58 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.001 |  |
| 2026-11-20 21:01:46 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-20 20:05:41 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-20 20:01:49 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.012 |  |
| 2026-11-20 18:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-20 20:02:21 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-11-20 21:02:14 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.041 |  |
| 2026-11-20 20:05:57 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.261 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)