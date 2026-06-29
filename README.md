# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_01:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,006 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 01:03:20 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:03:02 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-06-30 01:02:47 | Rathnapura (Kalu Ganga) | 5.17 | 🟢 Normal | -0.161 |  |
| 2026-06-30 01:02:36 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:02:32 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-30 01:02:25 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 01:02:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:02:20 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-30 01:02:14 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-30 01:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-30 01:01:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:01:23 | Ellagawa (Kalu Ganga) | 7.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-30 01:01:07 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 01:00:58 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:00:41 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-30 01:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 00:09:21 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-06-30 00:03:19 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-06-30 01:02:20 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-30 01:01:23 | Ellagawa (Kalu Ganga) | 7.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-30 01:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-30 01:00:41 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-30 01:02:25 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 00:10:02 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-30 01:02:32 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-30 01:01:07 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 00:05:00 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 01:03:20 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:03:53 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:02:36 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 00:02:32 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:01:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 00:01:27 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:04:05 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-30 00:09:37 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-06-30 00:04:53 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:02:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 00:03:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:00:58 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-30 00:02:34 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-30 00:08:01 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 00:03:35 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 01:02:14 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-06-30 01:03:02 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-06-30 01:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-06-30 00:01:39 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.031 |  |
| 2026-06-30 00:05:41 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.033 |  |
| 2026-06-30 00:09:41 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.046 |  |
| 2026-06-30 00:03:50 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-06-30 00:04:39 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.058 |  |
| 2026-06-30 00:05:44 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.060 |  |
| 2026-06-30 00:02:43 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.089 |  |
| 2026-06-30 00:04:41 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.142 |  |
| 2026-06-30 01:02:47 | Rathnapura (Kalu Ganga) | 5.17 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)