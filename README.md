# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_02:04:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,768 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 02:04:45 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:04:21 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:04:16 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-19 02:03:43 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 02:03:20 | Manampitiya (Mahaweli Ganga) | 4.99 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-19 02:03:07 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-19 02:02:59 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 02:02:55 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:43 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:32 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.100 |  |
| 2025-12-19 02:02:29 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -2.000 |  |
| 2025-12-19 02:02:16 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 02:02:11 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -2.000 |  |
| 2025-12-19 02:02:11 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | -0.050 |  |
| 2025-12-19 02:02:10 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:02 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:01 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:01:54 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2025-12-19 02:01:45 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:01:07 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:01:03 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:01:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.042 |  |
| 2025-12-19 01:20:19 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:20:15 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:20:01 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:10:08 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:09:25 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:09:04 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-19 01:08:05 | Horowpothana (Yan Oya) | 5.63 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-19 01:07:41 | Padiyathalawa (Maduru Oya) | 1.68 | 🟢 Normal | 0.180 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 02:03:20 | Manampitiya (Mahaweli Ganga) | 4.99 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-19 02:04:16 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-19 01:08:05 | Horowpothana (Yan Oya) | 5.63 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-19 01:04:30 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-19 01:09:04 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-19 02:02:59 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 01:06:47 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 02:02:16 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 02:03:43 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 02:02:43 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:10:08 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:03:07 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:01:07 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:10 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:55 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:01:45 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:02:30 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:20:19 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:02 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:01 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:01:03 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:04:45 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:04:21 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:02:56 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:20:15 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:06:24 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-19 02:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-19 01:06:08 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.012 |  |
| 2025-12-19 02:01:54 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2025-12-19 02:01:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.042 |  |
| 2025-12-19 02:02:11 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | -0.050 |  |
| 2025-12-19 01:04:26 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.050 |  |
| 2025-12-19 02:02:32 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.100 |  |
| 2025-12-19 01:02:03 | Nakkala (Kumbukkan Oya) | 1.95 | 🟢 Normal | -0.107 |  |
| 2025-12-19 00:07:32 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.123 |  |
| 2025-12-19 02:02:29 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -2.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)