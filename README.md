# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_03:13:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,985 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 03:13:00 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.088 |  |
| 2026-07-01 03:11:16 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:10:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-01 03:09:44 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.028 |  |
| 2026-07-01 03:08:43 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -5.684 |  |
| 2026-07-01 03:08:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:08:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.051 |  |
| 2026-07-01 03:08:24 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -5.684 |  |
| 2026-07-01 03:07:32 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:07:14 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -273.103 |  |
| 2026-07-01 03:06:45 | Pitabeddara (Nilwala Ganga) | 2.92 | 🟢 Normal | -273.103 |  |
| 2026-07-01 03:06:16 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-07-01 03:06:07 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:05:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:05:30 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:05:10 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.010 |  |
| 2026-07-01 03:04:14 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:03:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-07-01 03:03:31 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:03:17 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-01 03:03:11 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:03:01 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.005 |  |
| 2026-07-01 03:02:42 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.066 |  |
| 2026-07-01 03:02:40 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.031 |  |
| 2026-07-01 03:02:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-01 03:02:31 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 03:02:27 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-01 03:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-07-01 03:01:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:01:24 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.129 |  |
| 2026-07-01 03:01:15 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:01:08 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:26:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 03:10:06 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-01 01:06:42 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-01 03:02:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-01 03:03:17 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-01 03:02:31 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 03:03:11 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:01:15 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:00:26 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:01:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:04:14 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:00:52 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:07:32 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:05:30 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:11:16 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:03:31 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:05:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:06:07 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:02:00 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:08:16 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 03:01:08 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:21:35 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:12:20 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-07-01 03:03:01 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.005 |  |
| 2026-07-01 03:06:16 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-07-01 03:05:10 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.010 |  |
| 2026-06-30 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-01 03:02:27 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-01 03:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-07-01 03:09:44 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.028 |  |
| 2026-07-01 03:03:35 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-07-01 03:02:40 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.031 |  |
| 2026-07-01 03:08:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.051 |  |
| 2026-07-01 03:02:42 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.066 |  |
| 2026-07-01 02:02:11 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.074 |  |
| 2026-07-01 03:13:00 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.088 |  |
| 2026-07-01 03:01:24 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.129 |  |
| 2026-07-01 03:08:43 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -5.684 |  |
| 2026-07-01 03:07:14 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -273.103 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)