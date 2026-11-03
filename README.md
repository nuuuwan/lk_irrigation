# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_03:03:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 03:03:14 | Horowpothana (Yan Oya) | 3.13 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-04 03:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:02:55 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.692 |  |
| 2026-11-04 03:02:46 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-11-04 03:02:45 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-11-04 03:02:29 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-11-04 03:02:08 | Moragaswewa (Deduru Oya) | 4.15 | 🟢 Normal | -0.020 |  |
| 2026-11-04 03:01:53 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:01:28 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.128 |  |
| 2026-11-04 03:01:14 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:51:39 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:47:11 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-11-04 02:42:36 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:28:44 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:28:14 | Urawa (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.692 |  |
| 2026-11-04 02:26:25 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-04 02:21:48 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.106 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 02:13:29 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 8.540 | 🔺 Rising |
| 2026-11-04 00:03:29 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-04 02:02:17 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-04 03:02:46 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-11-04 01:14:49 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-04 02:07:08 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-04 02:05:52 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-04 01:06:59 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-04 02:01:58 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-04 02:18:35 | Thawalama (Gin Ganga) | 3.56 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-04 02:03:44 | Giriulla (Maha Oya) | 3.72 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-04 03:03:14 | Horowpothana (Yan Oya) | 3.13 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-04 02:03:39 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-04 02:09:06 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 02:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 03:01:53 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:01:14 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:42:36 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 03:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:51:39 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:28:44 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:01:09 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:03:06 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:07:20 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.015 |  |
| 2026-11-04 03:02:08 | Moragaswewa (Deduru Oya) | 4.15 | 🟢 Normal | -0.020 |  |
| 2026-11-04 02:01:37 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-11-04 02:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-11-04 03:02:29 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-11-04 03:02:45 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-11-04 02:02:21 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.066 |  |
| 2026-11-04 02:21:48 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.106 |  |
| 2026-11-04 03:01:28 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.128 |  |
| 2026-11-04 02:04:18 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.162 |  |
| 2026-11-04 02:06:43 | Moraketiya (Walawe Ganga) | 2.65 | 🟢 Normal | -0.600 |  |
| 2026-11-04 03:02:55 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.692 |  |
| 2026-11-04 01:02:29 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -28.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)