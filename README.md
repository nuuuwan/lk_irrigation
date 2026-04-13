# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_07:21:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,722 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 07:21:40 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-04-13 07:18:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:14:40 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-13 07:14:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:10:58 | Weraganthota (Mahaweli Ganga) | -2.81 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-13 07:09:08 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-13 07:07:42 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 07:07:04 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-13 07:06:36 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-04-13 07:06:34 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.018 |  |
| 2026-04-13 07:06:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-04-13 07:06:06 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:05:51 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.047 |  |
| 2026-04-13 07:05:20 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-04-13 07:05:17 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:04:55 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-04-13 07:03:55 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 07:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-04-13 07:03:31 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.022 |  |
| 2026-04-13 07:03:24 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.042 |  |
| 2026-04-13 07:03:19 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:03:14 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-13 07:02:55 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-13 07:02:50 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:02:27 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.051 |  |
| 2026-04-13 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-04-13 07:01:57 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:01:52 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-04-13 07:01:17 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:01:08 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-13 07:01:00 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 07:00:59 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.002 |  |
| 2026-04-13 07:00:44 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 07:00:19 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.034 |  |
| 2026-04-13 06:31:32 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 07:01:52 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-04-13 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-04-13 07:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-04-13 06:02:39 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-13 07:03:14 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-13 07:03:55 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 07:01:08 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-13 07:10:58 | Weraganthota (Mahaweli Ganga) | -2.81 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-13 06:31:32 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-13 07:14:40 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-13 07:01:00 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 06:07:50 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-13 07:07:04 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-13 07:00:44 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 07:07:42 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 07:01:57 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:18:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:04:09 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:05:17 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:14:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:03:19 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:02:50 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:01:17 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 07:00:59 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.002 |  |
| 2026-04-13 07:09:08 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-13 07:02:55 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-13 07:06:34 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.018 |  |
| 2026-04-13 07:03:31 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.022 |  |
| 2026-04-13 07:06:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-04-13 07:21:40 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-04-13 07:06:36 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.031 |  |
| 2026-04-13 07:05:20 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-04-13 07:00:19 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.034 |  |
| 2026-04-13 07:03:24 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.042 |  |
| 2026-04-13 07:05:51 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.047 |  |
| 2026-04-13 07:04:55 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-04-13 07:02:27 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.051 |  |
| 2026-04-13 06:00:28 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)