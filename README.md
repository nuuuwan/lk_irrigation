# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_15:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,532 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 15:03:25 | Moraketiya (Walawe Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-11-24 15:03:21 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.118 |  |
| 2026-11-24 15:03:16 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-11-24 15:03:08 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | -0.059 |  |
| 2026-11-24 15:03:02 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:02:57 | Giriulla (Maha Oya) | 2.53 | 🟢 Normal | -0.070 |  |
| 2026-11-24 15:02:27 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:02:24 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:02:23 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 15:02:19 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-24 15:02:11 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-24 15:01:12 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:21 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:17 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:05 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 15:02:19 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-24 14:04:43 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-24 15:02:11 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-24 14:04:19 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-24 14:01:18 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-24 14:01:43 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-24 14:07:40 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-24 14:05:01 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-24 14:03:12 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-24 15:02:23 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 14:07:25 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 15:02:24 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:21 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:10:56 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:01:12 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:17 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:03:02 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:05:10 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:02:39 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:05 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:02:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:02:27 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-24 14:06:13 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-11-24 14:03:59 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-11-24 14:12:08 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-11-24 14:03:57 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-11-24 15:03:25 | Moraketiya (Walawe Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 14:04:22 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.029 |  |
| 2026-11-24 15:03:16 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-11-24 14:01:40 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-11-24 14:01:23 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.044 |  |
| 2026-11-24 14:06:11 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.055 |  |
| 2026-11-24 15:03:08 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | -0.059 |  |
| 2026-11-24 15:02:57 | Giriulla (Maha Oya) | 2.53 | 🟢 Normal | -0.070 |  |
| 2026-11-24 14:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.101 |  |
| 2026-11-24 14:04:35 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.107 |  |
| 2026-11-24 15:03:21 | Hanwella (Kelani Ganga) | 2.10 | 🟢 Normal | -0.118 |  |
| 2026-11-24 14:01:05 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)