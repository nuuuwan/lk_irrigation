# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_13:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,286 measurements** from **39** stations.
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
| 2026-11-17 13:03:03 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:03:00 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:02:57 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-11-17 13:02:47 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:02:46 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:02:36 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:02:23 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.031 |  |
| 2026-11-17 13:02:20 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:02:17 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | -0.021 |  |
| 2026-11-17 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-17 13:02:06 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.273 |  |
| 2026-11-17 13:02:03 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:01:59 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:01:34 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:01:26 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:01:04 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:00:07 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 12:04:07 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-17 13:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-17 12:03:29 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 13:02:20 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:01:04 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:01:34 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:01:26 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:03:00 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-11-17 12:06:04 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-17 12:01:19 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:00:07 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 12:04:31 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-17 12:04:01 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:02:36 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 12:07:25 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:02:03 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-17 12:03:49 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-17 12:02:56 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-17 13:03:03 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-11-17 12:03:34 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:02:47 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-17 12:00:10 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:01:59 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-17 13:02:46 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.010 |  |
| 2026-11-17 12:04:00 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-17 12:06:34 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-17 12:00:58 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-11-17 12:08:02 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-11-17 12:02:24 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-11-17 12:04:05 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-11-17 12:02:45 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-11-17 13:02:17 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | -0.021 |  |
| 2026-11-17 13:02:23 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.031 |  |
| 2026-11-17 12:05:27 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.035 |  |
| 2026-11-17 12:00:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.040 |  |
| 2026-11-17 13:02:57 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-11-17 12:07:05 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.077 |  |
| 2026-11-17 13:02:06 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.273 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)