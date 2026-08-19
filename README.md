# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_11:16:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **237,642 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 11:16:44 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:15:59 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:12:53 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-19 11:10:53 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:10:22 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-08-19 11:08:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-19 11:08:19 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:07:03 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-08-19 11:06:49 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-08-19 11:06:20 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:06:15 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 11:04:25 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-08-19 11:06:49 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-08-19 11:12:53 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-19 11:04:52 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 11:03:57 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 11:01:58 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:00:10 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:02:54 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:01:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:10:53 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:00:47 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:02:19 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:15:59 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:02:11 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:04:55 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:00:09 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:08:19 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:00:41 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:02:09 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:06:20 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:05:03 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:16:44 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:01:59 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:02:44 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-08-19 11:07:03 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-08-19 11:03:30 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-08-19 11:02:05 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-08-19 11:08:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-19 11:10:22 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-08-19 11:02:39 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-08-19 11:04:08 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-08-19 11:02:10 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.020 |  |
| 2026-08-19 11:01:55 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-08-19 11:02:38 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.021 |  |
| 2026-08-19 11:06:15 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-08-19 11:04:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-08-19 11:01:25 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | -0.046 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)