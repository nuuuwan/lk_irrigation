# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_04:33:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,395 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 04:33:59 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-15 04:23:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-04-15 04:22:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-04-15 04:18:02 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.016 |  |
| 2026-04-15 04:13:44 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:13:19 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-15 04:08:57 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-04-15 04:08:41 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:08:28 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:07:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-04-15 04:07:20 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-15 04:06:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.005 |  |
| 2026-04-15 04:04:45 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-15 04:04:42 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-04-15 04:04:39 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:03:26 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-04-15 04:03:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:02:43 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.031 |  |
| 2026-04-15 04:02:23 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-15 04:02:22 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:02:18 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.401 | 🔺 Rising |
| 2026-04-15 04:02:09 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:01:42 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:01:41 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:01:23 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:01:21 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.005 |  |
| 2026-04-15 04:01:11 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-04-15 04:01:07 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 04:00:57 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-15 04:00:41 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:00:34 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.340 |  |
| 2026-04-15 04:00:29 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.114 |  |
| 2026-04-15 04:00:08 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:59:51 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 04:23:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-04-15 04:02:18 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.401 | 🔺 Rising |
| 2026-04-15 04:03:26 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-04-15 04:33:59 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-15 04:04:45 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-15 04:01:11 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 04:01:07 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 04:07:20 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-15 04:01:21 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.005 |  |
| 2026-04-15 00:19:42 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:13:44 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:08:28 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:01:41 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:04:39 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:08:41 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:03:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:00:41 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:00:08 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:01:23 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:02:22 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:01:42 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:02:09 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 04:06:01 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.005 |  |
| 2026-04-15 03:07:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-15 04:08:57 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-04-15 04:13:19 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-15 04:02:23 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-15 04:00:57 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-04-15 04:18:02 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.016 |  |
| 2026-04-15 04:07:27 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-04-15 04:04:42 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-15 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-04-15 04:02:43 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.031 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-15 03:02:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-15 04:00:29 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.114 |  |
| 2026-04-15 04:00:34 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.340 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)