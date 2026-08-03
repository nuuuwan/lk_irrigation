# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_02:28:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,285 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 02:28:14 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:26:42 | Peradeniya (Mahaweli Ganga) | 6.68 | 🟡 Alert | -0.312 |  |
| 2026-08-04 02:24:24 | Rathnapura (Kalu Ganga) | 7.71 | 🟠 Minor Flood | -0.068 |  |
| 2026-08-04 02:16:23 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-04 02:09:23 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:08:55 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-04 02:08:37 | Kithulgala (Kelani Ganga) | 2.82 | 🟢 Normal | -0.113 |  |
| 2026-08-04 02:08:06 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-04 02:07:54 | Glencourse (Kelani Ganga) | 16.00 | 🟡 Alert | -0.293 |  |
| 2026-08-04 02:06:46 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.111 |  |
| 2026-08-04 02:06:18 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.499 |  |
| 2026-08-04 02:06:10 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:05:25 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-08-04 02:05:06 | Badalgama (Maha Oya) | 4.65 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-08-04 02:03:34 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.099 |  |
| 2026-08-04 02:03:16 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 02:03:07 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:03:07 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | -0.051 |  |
| 2026-08-04 02:02:51 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:02:22 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:02:20 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-04 02:01:47 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | -0.500 |  |
| 2026-08-04 02:01:46 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 02:01:45 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-08-04 02:01:44 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 02:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-08-04 02:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.012 |  |
| 2026-08-04 02:00:12 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:48:16 | Thawalama (Gin Ganga) | 3.37 | 🟢 Normal | -0.499 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 02:24:24 | Rathnapura (Kalu Ganga) | 7.71 | 🟠 Minor Flood | -0.068 |  |
| 2026-08-04 02:05:25 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-08-04 02:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-08-04 02:07:54 | Glencourse (Kelani Ganga) | 16.00 | 🟡 Alert | -0.293 |  |
| 2026-08-04 02:26:42 | Peradeniya (Mahaweli Ganga) | 6.68 | 🟡 Alert | -0.312 |  |
| 2026-08-04 02:05:06 | Badalgama (Maha Oya) | 4.65 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-08-04 00:06:57 | Pitabeddara (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-04 02:08:55 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-04 02:02:20 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-04 02:03:16 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-04 02:16:23 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-04 02:01:46 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 02:01:44 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 02:08:06 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-04 01:16:29 | Panadugama (Nilwala Ganga) | 4.86 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-04 02:09:23 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:03:07 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:19:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:02:51 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:00:12 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:02:22 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:04:50 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:06:10 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:28:14 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.012 |  |
| 2026-08-04 01:03:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-08-04 02:01:45 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-08-04 01:06:52 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-08-04 02:03:07 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | -0.051 |  |
| 2026-08-03 23:13:30 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.058 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-04 02:03:34 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.099 |  |
| 2026-08-04 02:06:46 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.111 |  |
| 2026-08-04 02:08:37 | Kithulgala (Kelani Ganga) | 2.82 | 🟢 Normal | -0.113 |  |
| 2026-08-04 01:03:21 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.138 |  |
| 2026-08-04 02:06:18 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.499 |  |
| 2026-08-04 02:01:47 | Giriulla (Maha Oya) | 3.65 | 🟢 Normal | -0.500 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)