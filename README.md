# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_01:32:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,259 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 01:32:49 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:31:26 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.087 |  |
| 2026-05-13 01:30:41 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.014 |  |
| 2026-05-13 01:26:44 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-13 01:14:13 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:09:40 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.126 |  |
| 2026-05-13 01:07:36 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.120 |  |
| 2026-05-13 01:07:25 | Siyambalanduwa (Heda Oya) | 2.42 | 🟢 Normal | -0.131 |  |
| 2026-05-13 01:06:53 | Katharagama (Menik Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-05-13 01:06:47 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.065 |  |
| 2026-05-13 01:05:49 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:05:40 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-13 01:05:32 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 01:05:29 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:04:49 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-13 01:04:43 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:04:40 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:04:30 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.020 |  |
| 2026-05-13 01:04:23 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-13 01:03:56 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-13 01:03:55 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-05-13 01:03:16 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:03:14 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.796 |  |
| 2026-05-13 01:03:06 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.071 |  |
| 2026-05-13 01:02:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-05-13 01:02:15 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:02:13 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.119 |  |
| 2026-05-13 01:01:35 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:01:24 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.055 |  |
| 2026-05-13 01:01:10 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:00:27 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 01:05:40 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-13 01:04:23 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-13 00:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-13 01:03:56 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-13 00:11:51 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-13 01:26:44 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 01:05:32 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 01:05:49 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:04:43 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:05:29 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:03:16 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:02:55 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:32:49 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-13 01:14:13 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:11:44 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.009 |  |
| 2026-05-13 01:04:40 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:02:15 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:01:10 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:01:35 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:04:49 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-13 01:30:41 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.014 |  |
| 2026-05-13 01:06:53 | Katharagama (Menik Ganga) | 1.58 | 🟢 Normal | -0.019 |  |
| 2026-05-13 01:03:55 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-05-13 01:04:30 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-13 01:00:27 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-05-13 01:02:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-13 01:01:24 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | -0.055 |  |
| 2026-05-13 01:06:47 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.065 |  |
| 2026-05-13 01:03:06 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.071 |  |
| 2026-05-13 01:31:26 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.087 |  |
| 2026-05-13 01:02:13 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.119 |  |
| 2026-05-13 01:07:36 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.120 |  |
| 2026-05-13 01:09:40 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.126 |  |
| 2026-05-13 01:07:25 | Siyambalanduwa (Heda Oya) | 2.42 | 🟢 Normal | -0.131 |  |
| 2026-05-13 01:03:14 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.796 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)