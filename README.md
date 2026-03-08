# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_04:17:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,111 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 04:17:35 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.008 |  |
| 2026-03-09 04:13:23 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-03-09 04:12:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-09 04:10:46 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:09:31 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -1.800 |  |
| 2026-03-09 04:09:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -1.800 |  |
| 2026-03-09 04:07:48 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:07:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-09 04:06:16 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-03-09 04:05:39 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:04:31 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-09 04:04:15 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:54 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:46 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 04:03:45 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:35 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-09 04:03:35 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:33 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:33 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:21 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-09 04:03:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.058 |  |
| 2026-03-09 04:02:51 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 04:02:46 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-09 04:02:10 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:02:08 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:01:54 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:01:47 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:01:36 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:01:13 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.150 |  |
| 2026-03-09 04:01:08 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-09 04:01:01 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-09 04:00:59 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-09 04:00:31 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 04:03:21 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-03-09 04:04:31 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-09 04:07:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-09 04:01:08 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-09 04:02:46 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-09 04:03:35 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-09 04:01:01 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-09 04:00:31 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 18:00:14 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 03:22:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-09 04:03:46 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 04:02:51 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 04:12:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-09 04:01:47 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:33 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:33 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:31:40 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 02:54:21 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:03:45 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:05:39 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:10:46 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-03-09 03:01:59 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:01:54 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:02:08 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:00:59 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:01:36 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:07:48 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:18 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:04:15 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 03:04:47 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:02:10 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 04:13:23 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-03-09 04:17:35 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.008 |  |
| 2026-03-09 04:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-09 04:06:16 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-03-09 04:03:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.058 |  |
| 2026-03-09 04:01:13 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.150 |  |
| 2026-03-09 04:09:31 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -1.800 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)