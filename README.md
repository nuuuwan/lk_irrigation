# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_16:03:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,574 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 16:03:40 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-24 16:03:28 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.120 |  |
| 2026-11-24 16:03:21 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.051 |  |
| 2026-11-24 16:02:55 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 16:02:50 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 16:02:44 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:02:39 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 16:02:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-24 16:02:11 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.051 |  |
| 2026-11-24 16:02:08 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 16:01:59 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:55 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:24 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-24 16:01:15 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.035 |  |
| 2026-11-24 16:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-24 16:01:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:00:10 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 15:02:19 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-11-24 15:03:32 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-11-24 16:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-24 15:06:27 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-24 16:02:55 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 15:02:11 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-24 16:02:50 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 15:07:00 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 16:02:39 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 16:02:08 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-24 16:01:55 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:00:17 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:59 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:01:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:04:09 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:04:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 16:02:44 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 15:05:15 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-24 16:02:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-24 16:03:40 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-24 15:06:28 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.019 |  |
| 2026-11-24 16:01:24 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-24 15:03:25 | Moraketiya (Walawe Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 15:03:59 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-24 16:00:10 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | -0.032 |  |
| 2026-11-24 16:01:15 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.035 |  |
| 2026-11-24 15:06:14 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.037 |  |
| 2026-11-24 15:06:36 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -0.039 |  |
| 2026-11-24 16:02:11 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.051 |  |
| 2026-11-24 16:03:21 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.051 |  |
| 2026-11-24 15:07:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.056 |  |
| 2026-11-24 15:03:08 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | -0.059 |  |
| 2026-11-24 15:03:40 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.071 |  |
| 2026-11-24 15:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.077 |  |
| 2026-11-24 16:03:28 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.120 |  |
| 2026-11-24 15:07:13 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -1.241 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)