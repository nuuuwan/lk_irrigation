# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_03:15:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,313 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 03:15:55 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:14:13 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:13:37 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.029 |  |
| 2026-10-24 03:11:55 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -7.448 |  |
| 2026-10-24 03:11:26 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -7.448 |  |
| 2026-10-24 03:10:59 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:07:59 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.027 |  |
| 2026-10-24 03:07:30 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.040 |  |
| 2026-10-24 03:07:28 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.009 |  |
| 2026-10-24 03:07:23 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -2.361 |  |
| 2026-10-24 03:06:38 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.026 |  |
| 2026-10-24 03:05:47 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:05:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:05:18 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-10-24 03:05:15 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 03:05:14 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-24 03:05:09 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-10-24 03:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.58 | 🟢 Normal | -2.361 |  |
| 2026-10-24 03:05:04 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-24 03:04:31 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:04:10 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:04:05 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-10-24 03:04:03 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-10-24 03:03:53 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-24 03:03:50 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-24 03:03:47 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-24 03:03:41 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.129 |  |
| 2026-10-24 03:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.52 | 🟢 Normal | -2.361 |  |
| 2026-10-24 03:03:16 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:03:15 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-10-24 03:02:48 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:02:20 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | -0.069 |  |
| 2026-10-24 03:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-10-24 03:01:12 | Moragaswewa (Deduru Oya) | 3.81 | 🟢 Normal | -0.040 |  |
| 2026-10-24 03:00:56 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 03:05:04 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-24 03:05:15 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 02:01:16 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 03:04:10 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:07:23 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:03:16 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:02:48 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:15:55 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:14:13 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:05:47 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:05:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 03:10:59 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:10:02 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.005 |  |
| 2026-10-24 03:07:28 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.009 |  |
| 2026-10-24 03:03:47 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-24 03:05:14 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-24 03:03:50 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-24 03:03:53 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-24 03:05:18 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-10-24 03:03:15 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 03:06:38 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.026 |  |
| 2026-10-24 03:07:59 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.027 |  |
| 2026-10-24 03:13:37 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | -0.029 |  |
| 2026-10-24 03:04:05 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-10-24 03:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-10-24 03:04:03 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-10-24 03:07:30 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.040 |  |
| 2026-10-24 03:01:12 | Moragaswewa (Deduru Oya) | 3.81 | 🟢 Normal | -0.040 |  |
| 2026-10-24 03:00:56 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.042 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-24 03:05:09 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.051 |  |
| 2026-10-24 03:02:20 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | -0.069 |  |
| 2026-10-24 03:03:41 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.129 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-24 03:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -2.361 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |
| 2026-10-24 03:11:55 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -7.448 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)