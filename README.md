# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_14:27:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,305 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 14:27:43 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.054 |  |
| 2026-09-18 14:26:50 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:19:29 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.080 |  |
| 2026-09-18 14:13:09 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.026 |  |
| 2026-09-18 14:09:45 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 14:09:02 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-09-18 14:00:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-18 14:09:45 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-18 14:08:32 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-18 14:04:11 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 14:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 14:07:04 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 14:02:06 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:08:00 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:02:36 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:01:07 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:26:50 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:02:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:02:14 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:00:31 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:08:34 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:03:16 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:01:37 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:03:04 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:01:44 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:02:03 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:08:13 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:06:02 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:01:18 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-18 14:03:39 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-09-18 14:05:30 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.010 |  |
| 2026-09-18 14:04:15 | Ellagawa (Kalu Ganga) | 4.91 | 🟢 Normal | -0.010 |  |
| 2026-09-18 14:02:53 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-09-18 14:04:21 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-09-18 14:02:44 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-18 14:00:17 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-09-18 13:01:15 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-09-18 14:07:46 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-09-18 14:05:28 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-09-18 14:13:09 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.026 |  |
| 2026-09-18 14:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.33 | 🟢 Normal | -0.040 |  |
| 2026-09-18 14:27:43 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.054 |  |
| 2026-09-18 14:19:29 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.080 |  |
| 2026-09-18 14:04:01 | Magura (Kalu Ganga) | 3.81 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)