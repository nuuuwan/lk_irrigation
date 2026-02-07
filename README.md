# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_02:52:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,077 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 02:52:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.024 |  |
| 2026-02-08 02:46:26 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:38:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-08 02:21:29 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-08 02:20:30 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-08 02:14:09 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.029 |  |
| 2026-02-08 02:11:27 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.018 |  |
| 2026-02-08 02:11:19 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.005 |  |
| 2026-02-08 02:08:32 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-08 02:05:45 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -108.000 |  |
| 2026-02-08 02:05:44 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -108.000 |  |
| 2026-02-08 02:05:43 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -108.000 |  |
| 2026-02-08 02:05:42 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -108.000 |  |
| 2026-02-08 02:05:04 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:04:57 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -468.000 |  |
| 2026-02-08 02:04:56 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -468.000 |  |
| 2026-02-08 02:04:55 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-02-08 02:04:41 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.008 |  |
| 2026-02-08 02:04:38 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:03:33 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:03:30 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-08 02:02:34 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-02-08 02:02:25 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-02-08 02:02:23 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:02:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:01:33 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-02-08 02:01:24 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:01:04 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.005 |  |
| 2026-02-08 02:01:00 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:00:57 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:00:45 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 02:00:13 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:00:12 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 02:38:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-08 02:21:29 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-08 01:15:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-08 02:20:30 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-08 02:00:45 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 02:08:32 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-08 02:00:13 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:00:57 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:01:00 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 01:40:53 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:38 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-08 01:02:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 01:05:44 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:03:33 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:02:23 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:04:38 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:01:24 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 01:37:01 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:46:26 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:02:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:05:04 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:11:19 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.005 |  |
| 2026-02-08 02:01:04 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.005 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-08 02:04:41 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.008 |  |
| 2026-02-08 02:03:30 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-08 02:01:33 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-02-08 01:06:12 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-08 02:02:34 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-02-08 02:02:25 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-02-08 02:11:27 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.018 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-08 02:52:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.024 |  |
| 2026-02-08 02:14:09 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.029 |  |
| 2026-02-08 02:04:55 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-02-08 02:00:12 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-02-08 02:05:45 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -108.000 |  |
| 2026-02-08 02:04:57 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -468.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)