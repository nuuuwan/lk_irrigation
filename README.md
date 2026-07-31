# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_11:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 11:10:24 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:09:55 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:08:52 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.288 |  |
| 2026-07-31 11:07:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-07-31 11:07:00 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:06:53 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 11:06:50 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:06:47 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.031 |  |
| 2026-07-31 11:06:40 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.022 |  |
| 2026-07-31 11:05:36 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:05:04 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:04:33 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 11:04:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:04:07 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:03:52 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 11:03:37 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.040 |  |
| 2026-07-31 11:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:03:28 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-31 11:03:20 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:44 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-07-31 11:02:41 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-07-31 11:02:37 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:27 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-31 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 11:02:12 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:07 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:01:58 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:01:42 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:01:32 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 11:07:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-07-31 11:03:28 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-31 10:03:36 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 11:01:08 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 11:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 11:03:52 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 11:06:53 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 11:04:33 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 11:01:04 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:00:06 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:01:32 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 10:08:27 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:10:24 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:07 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:07:00 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:00:13 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:05:36 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:04:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:05:04 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:01:58 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:37 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:01:24 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:04:07 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:06:50 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:00:23 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:03:20 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:09:55 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:12 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:01:42 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-07-31 11:02:44 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-07-31 11:02:27 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-31 11:01:10 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-31 11:02:41 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-07-31 11:06:40 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.022 |  |
| 2026-07-31 11:06:47 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.031 |  |
| 2026-07-31 11:03:37 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.040 |  |
| 2026-07-31 11:08:52 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.288 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)