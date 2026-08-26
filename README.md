# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_18:15:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,178 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 18:15:53 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.037 |  |
| 2026-08-26 18:09:49 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.018 |  |
| 2026-08-26 18:09:14 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-08-26 18:08:00 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:07:15 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-26 18:06:49 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-26 18:06:32 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.088 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 18:06:49 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-26 18:04:55 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 18:07:15 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-26 18:03:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 18:01:33 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:00:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:02:16 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:01:35 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:03:09 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:01:42 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:02:57 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:02:07 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:03:34 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:04:13 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:08:00 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:01:37 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:04:28 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-26 18:01:27 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-26 18:01:52 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-26 18:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -0.010 |  |
| 2026-08-26 18:09:14 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-08-26 18:04:50 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-08-26 18:02:45 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-26 18:02:16 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-08-26 18:09:49 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.018 |  |
| 2026-08-26 18:03:32 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-08-26 18:01:25 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-08-26 18:04:29 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-08-26 18:02:32 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-08-26 18:15:53 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.037 |  |
| 2026-08-26 18:03:18 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-08-26 18:03:37 | Ellagawa (Kalu Ganga) | 6.68 | 🟢 Normal | -0.051 |  |
| 2026-08-26 18:04:33 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.070 |  |
| 2026-08-26 18:06:32 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.088 |  |
| 2026-08-26 18:03:08 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.096 |  |
| 2026-08-26 18:05:02 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)