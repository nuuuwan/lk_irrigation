# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_23:40:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,524 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 23:40:07 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:28:37 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.007 |  |
| 2026-05-26 23:16:20 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-26 23:12:27 | Glencourse (Kelani Ganga) | 11.92 | 🟢 Normal | -0.067 |  |
| 2026-05-26 23:09:34 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-05-26 23:08:30 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-26 23:08:23 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 23:07:00 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 23:05:48 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:05:35 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 23:05:26 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:04:52 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-26 23:04:44 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 23:04:25 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:04:18 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-26 23:03:43 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:03:29 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 23:03:04 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:02:50 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-05-26 23:02:28 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:02:23 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:02:20 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.070 |  |
| 2026-05-26 23:02:13 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 23:02:13 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.050 |  |
| 2026-05-26 23:02:13 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.074 |  |
| 2026-05-26 23:01:46 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:01:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:01:20 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-05-26 23:01:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:00:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:00:18 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 22:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-26 23:01:20 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-05-26 23:08:30 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-26 23:02:13 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 23:03:29 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 23:16:20 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-26 23:04:52 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-26 23:04:44 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 23:08:23 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 23:05:35 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 23:07:00 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-26 23:02:23 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:00:59 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:01:46 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:01:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:03:04 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:00:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:03:43 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:02:28 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:40:07 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:00:18 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:04:25 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:05:14 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:05:26 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:05:48 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:01:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-26 22:02:13 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:28:37 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.007 |  |
| 2026-05-26 23:09:34 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-05-26 21:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-26 23:04:18 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-26 23:02:50 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-26 23:02:13 | Hanwella (Kelani Ganga) | 4.50 | 🟢 Normal | -0.050 |  |
| 2026-05-26 23:12:27 | Glencourse (Kelani Ganga) | 11.92 | 🟢 Normal | -0.067 |  |
| 2026-05-26 23:02:20 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.070 |  |
| 2026-05-26 23:02:13 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)