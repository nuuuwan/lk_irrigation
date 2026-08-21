# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_03:30:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,031 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 03:30:08 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:14:03 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 03:10:52 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-22 03:10:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:05:24 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:05:15 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.062 |  |
| 2026-08-22 03:04:38 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:04:35 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-08-22 03:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:04:26 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-22 03:04:19 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-22 03:03:53 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:03:38 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 03:04:19 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-22 03:00:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-22 03:01:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-22 03:10:52 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-22 03:04:26 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-22 03:03:10 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-22 03:03:17 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-22 03:14:03 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 03:00:50 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 03:01:09 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-08-22 03:00:51 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.003 |  |
| 2026-08-22 03:05:24 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:38 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:00:49 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:01:09 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:02:30 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:02:38 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:24 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:01:29 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:02:58 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:02:19 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:10:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:03:53 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:02:47 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:02:08 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:02:55 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:03:38 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:30:08 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 02:08:50 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-22 02:29:21 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-22 02:10:59 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:03:50 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-08-22 03:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-08-22 03:04:35 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-08-22 02:04:29 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.051 |  |
| 2026-08-22 03:05:15 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.062 |  |
| 2026-08-22 03:01:19 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)