# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_02:05:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,989 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 02:05:14 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.212 |  |
| 2026-01-04 02:04:42 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-04 02:04:30 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:54 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.005 |  |
| 2026-01-04 02:03:27 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:26 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:25 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.089 |  |
| 2026-01-04 02:03:10 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:08 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:06 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:04 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:02:57 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-04 02:02:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:02:22 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-01-04 02:02:22 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-04 02:02:09 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-01-04 02:02:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:01:42 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-01-04 02:01:27 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:01:23 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:01:12 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-01-04 02:01:08 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:00:12 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:00:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 01:58:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 01:53:10 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-01-04 01:53:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-01-04 01:48:03 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 01:46:53 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-04 01:46:51 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-04 01:18:12 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-04 01:13:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 01:12:05 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 18:08:58 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 17.419 | 🔺 Rising |
| 2026-01-04 01:06:50 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.997 | 🔺 Rising |
| 2026-01-04 00:02:28 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-01-04 01:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-01-04 02:02:09 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-01-04 01:01:13 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-01-03 23:06:52 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-04 00:03:59 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-04 01:12:05 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-04 02:02:57 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-04 02:01:12 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-01-04 02:01:27 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:01:08 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 23:06:51 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:26 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:01:23 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:00:12 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:02:45 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:07 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:10 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:04:30 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 01:46:53 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:27 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-04 00:10:22 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-04 02:03:54 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -0.005 |  |
| 2026-01-04 01:03:42 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-01-04 02:04:42 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-04 02:02:22 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-04 02:01:42 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-01-04 01:05:22 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.012 |  |
| 2026-01-03 23:00:29 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.012 |  |
| 2026-01-04 00:03:00 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-01-04 02:02:22 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-01-04 01:00:46 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.036 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-04 02:03:25 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.089 |  |
| 2026-01-04 02:05:14 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)