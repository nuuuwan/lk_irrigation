# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_01:29:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,400 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 01:29:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-05 01:14:29 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -2.769 |  |
| 2026-04-05 01:14:24 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.005 |  |
| 2026-04-05 01:14:03 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -2.769 |  |
| 2026-04-05 01:10:55 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-05 01:09:14 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-05 01:08:18 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 01:07:48 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.332 |  |
| 2026-04-05 01:07:08 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:06:48 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:06:03 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.051 |  |
| 2026-04-05 01:05:46 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-05 01:04:13 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:03:58 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-05 01:03:55 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-04-05 01:03:50 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:03:15 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:03:06 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.130 |  |
| 2026-04-05 01:03:04 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-05 01:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-04-05 01:02:42 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:02:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:02:20 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-04-05 01:02:11 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.242 |  |
| 2026-04-05 01:02:05 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:01:54 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-04-05 01:01:48 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-05 01:01:20 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:01:05 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-05 01:00:59 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-05 01:00:52 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-04-05 01:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:00:20 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:56:11 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:54:40 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 01:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-04-05 01:29:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-05 01:10:55 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-05 01:00:59 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-05 01:01:48 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-05 00:02:11 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 01:05:46 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-05 01:08:18 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 01:01:05 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-05 01:14:24 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.005 |  |
| 2026-04-05 01:00:20 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:02:20 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:03:15 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:02:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:04:13 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:02:05 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:01:54 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-04-05 00:10:31 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:07:08 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:02:42 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:03:50 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:01:20 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:06:48 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-05 01:09:14 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-05 01:03:58 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-05 01:03:04 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-05 01:00:52 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-04-05 00:54:40 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.025 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-05 01:03:55 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-05 01:06:03 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.051 |  |
| 2026-04-05 01:03:06 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.130 |  |
| 2026-04-05 01:02:11 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.242 |  |
| 2026-04-05 01:07:48 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.332 |  |
| 2026-04-05 01:14:29 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -2.769 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)