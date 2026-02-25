# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_16:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,796 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 16:02:46 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:39 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-02-25 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-02-25 16:02:24 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:18 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:15 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-02-25 16:02:15 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-25 16:02:02 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:01:55 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 16:01:49 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:01:14 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | -0.111 |  |
| 2026-02-25 16:00:54 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-02-25 16:00:45 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:00:29 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:20:05 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -36.000 |  |
| 2026-02-25 15:20:03 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -36.000 |  |
| 2026-02-25 15:13:59 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-25 15:13:45 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.302 |  |
| 2026-02-25 15:11:58 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-02-25 15:08:27 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-25 15:07:49 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:07:47 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.302 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 15:04:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-25 15:05:01 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-25 15:00:30 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-25 15:04:55 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-25 16:02:15 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-25 16:01:55 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 15:13:59 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-25 16:00:29 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:01:49 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:18 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:00:45 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:01:35 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:13 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:32 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:46 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:05:27 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:24 | Dunamale (Aththanagalu Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:24 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:07:05 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:07:17 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:02:05 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-02-25 15:03:58 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:02:02 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-25 14:08:58 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-02-25 15:11:58 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-02-25 15:08:27 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-25 15:03:43 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-25 15:03:21 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-25 16:02:39 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-02-25 16:00:54 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-02-25 16:02:15 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-02-25 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-02-25 15:06:51 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.077 |  |
| 2026-02-25 16:01:14 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | -0.111 |  |
| 2026-02-25 15:13:45 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.302 |  |
| 2026-02-25 15:20:05 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)