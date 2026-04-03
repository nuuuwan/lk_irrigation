# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_12:23:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,006 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 12:23:36 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:16:12 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:13:15 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.058 |  |
| 2026-04-03 12:11:50 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:10:44 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.017 |  |
| 2026-04-03 12:10:14 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:10:05 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.024 |  |
| 2026-04-03 12:08:38 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:08:27 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:08:18 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:07:54 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:07:26 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:06:38 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:06:01 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:05:40 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:05:18 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:05:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:05:03 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:04:40 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-04-03 12:04:27 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-03 12:04:06 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-03 12:04:05 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:03:48 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.051 |  |
| 2026-04-03 12:03:26 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.040 |  |
| 2026-04-03 12:03:24 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-04-03 12:03:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-03 12:03:01 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-04-03 12:02:52 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-04-03 12:02:42 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:02:37 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:02:35 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:02:14 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-03 12:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-03 12:02:07 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.079 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 12:03:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-03 12:02:52 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-04-03 12:01:11 | Thanthirimale (Malwathu Oya) | 3.07 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-04-03 12:03:24 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-04-03 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-03 12:04:06 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-03 12:04:27 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-03 12:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 12:06:01 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:02:35 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:08:27 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:05:03 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:01:25 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:05:40 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:05:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-03 11:11:55 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:04:05 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:07:26 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:10:14 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:08:18 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:00:59 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:11:50 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:00:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:07:54 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:05:18 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:16:12 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:23:36 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:02:42 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:02:37 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 12:04:40 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-04-03 12:10:44 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.017 |  |
| 2026-04-03 12:02:14 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-03 12:10:05 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.024 |  |
| 2026-04-03 12:03:01 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-04-03 12:03:26 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.040 |  |
| 2026-04-03 12:03:48 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.051 |  |
| 2026-04-03 12:13:15 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.058 |  |
| 2026-04-03 12:02:07 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.079 |  |
| 2026-04-03 12:00:14 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)