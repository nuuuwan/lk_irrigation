# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_13:41:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,149 measurements** from **39** stations.
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
| 2026-08-15 13:41:42 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:24:59 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.058 |  |
| 2026-08-15 13:14:36 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.009 |  |
| 2026-08-15 13:10:53 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:08:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:07:52 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:07:50 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -0.133 |  |
| 2026-08-15 13:06:54 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.078 |  |
| 2026-08-15 13:06:39 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:06:36 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-15 13:05:46 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:05:41 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:05:20 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-15 13:04:54 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-08-15 13:04:46 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 13:04:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-08-15 13:00:52 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-15 13:03:20 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-15 13:02:34 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 13:05:20 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-15 13:02:23 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:01:08 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 12:01:47 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:01:34 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:03:45 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:10:53 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:05:46 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:03:11 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:03:07 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:06:39 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:05:41 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:07:52 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:08:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:02:15 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:02:21 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:03:40 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:41:42 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:03:28 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 12:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:02:18 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 13:14:36 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.009 |  |
| 2026-08-15 13:04:46 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | -0.009 |  |
| 2026-08-15 12:08:08 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-08-15 13:06:36 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-15 13:03:01 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-08-15 13:04:54 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-08-15 13:02:01 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-08-15 13:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-08-15 13:01:45 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-08-15 13:24:59 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.058 |  |
| 2026-08-15 13:06:54 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.078 |  |
| 2026-08-15 13:07:50 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -0.133 |  |
| 2026-08-15 13:04:17 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)