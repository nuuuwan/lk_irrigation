# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_10:24:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 10:24:31 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.017 |  |
| 2026-04-09 10:13:02 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:07:57 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:06:03 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.029 |  |
| 2026-04-09 10:05:26 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.011 |  |
| 2026-04-09 10:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-04-09 10:04:45 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-09 10:04:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-09 10:04:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:04:15 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:03:46 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:03:41 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:03:38 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-04-09 10:03:23 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 10:03:19 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.058 |  |
| 2026-04-09 10:03:07 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:03:02 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:03:00 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:02:55 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-09 10:02:54 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.006 |  |
| 2026-04-09 10:02:48 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 10:02:42 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:02:34 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:02:19 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.060 |  |
| 2026-04-09 10:02:12 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | -0.042 |  |
| 2026-04-09 10:01:54 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:47 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:45 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.299 |  |
| 2026-04-09 10:01:23 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.072 |  |
| 2026-04-09 10:01:21 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:14 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:10 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 10:01:08 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:08 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:00:42 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:00:41 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:00:37 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-04-09 10:00:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 10:02:55 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-09 10:03:23 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 10:01:10 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 10:02:48 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 10:04:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-09 10:02:34 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:00:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:14 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:03:00 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:08 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:13:02 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:21 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:00:42 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:08 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:04:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:47 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:00:41 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:07:57 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:01:54 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:02:42 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-09 10:02:54 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.006 |  |
| 2026-04-09 10:04:45 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-09 10:03:07 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:03:46 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:04:15 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:03:02 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:03:41 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:05:26 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.011 |  |
| 2026-04-09 10:24:31 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.017 |  |
| 2026-04-09 10:06:03 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.029 |  |
| 2026-04-09 10:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-04-09 10:03:38 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-04-09 10:02:12 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | -0.042 |  |
| 2026-04-09 10:00:37 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-04-09 10:03:19 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.058 |  |
| 2026-04-09 10:02:19 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.060 |  |
| 2026-04-09 10:01:23 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.072 |  |
| 2026-04-09 10:01:45 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)