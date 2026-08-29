# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_16:02:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,360 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 16:02:41 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:02:35 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-08-29 16:02:29 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:02:14 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:02:05 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-29 16:01:54 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:01:12 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:01:07 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.035 |  |
| 2026-08-29 16:00:22 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-29 15:26:39 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 15:03:23 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-29 15:07:24 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-29 15:05:03 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-29 15:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-29 15:02:22 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-29 15:02:36 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-29 15:08:07 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-29 15:04:26 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-29 15:01:30 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 15:00:49 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 16:01:54 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:02:29 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:41 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:02:41 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:09:07 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:02:14 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:01:12 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:49 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:17 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:03:23 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:00:57 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:01:15 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:03:55 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:12:02 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:06:05 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 15:07:43 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-08-29 15:04:08 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-08-29 15:04:26 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-29 16:02:05 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-29 16:00:22 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-29 15:02:27 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-08-29 15:08:30 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-08-29 16:02:35 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-08-29 16:01:07 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.035 |  |
| 2026-08-29 15:02:30 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.041 |  |
| 2026-08-29 15:05:27 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)