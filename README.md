# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_15:33:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,941 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 15:33:09 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.007 |  |
| 2026-04-14 15:13:44 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:11:37 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:09:56 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:07:32 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:06:33 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:06:22 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.037 |  |
| 2026-04-14 15:05:18 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.057 |  |
| 2026-04-14 15:05:04 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:04:41 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:04:41 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-04-14 15:04:39 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-04-14 15:04:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-14 15:04:32 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:04:20 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-04-14 15:04:11 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-14 15:04:06 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-14 15:04:02 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:30 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-14 15:03:29 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-04-14 15:03:29 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:28 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-14 15:03:27 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:10 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:02:55 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:02:49 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-14 15:02:41 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.047 |  |
| 2026-04-14 15:02:34 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 15:02:49 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-04-14 15:04:11 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-14 15:00:22 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-14 15:01:52 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-14 15:04:06 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-14 14:03:47 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 15:03:29 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:00:25 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:04:32 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:13:44 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:01:30 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:10 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:04:41 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:11:37 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:04:02 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:02:55 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:05:04 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:03:27 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:07:32 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:02:34 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:02:41 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-14 15:06:33 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:39:26 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.006 |  |
| 2026-04-14 15:33:09 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.007 |  |
| 2026-04-14 15:04:20 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-04-14 15:00:57 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-14 15:04:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-14 15:03:28 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-14 15:04:39 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-04-14 15:03:29 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-04-14 15:03:30 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-04-14 15:04:41 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-04-14 15:06:22 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.037 |  |
| 2026-04-14 15:01:01 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-04-14 15:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.047 |  |
| 2026-04-14 15:05:18 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.057 |  |
| 2026-04-14 15:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.071 |  |
| 2026-04-14 15:01:15 | Thanthirimale (Malwathu Oya) | 3.98 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)