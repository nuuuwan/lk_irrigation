# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_15:24:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 15:24:20 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:22:25 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:13:09 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-07-04 15:13:07 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-07-04 15:11:01 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-04 15:08:28 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:08:12 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 15:07:00 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-07-04 15:06:36 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-07-04 15:06:12 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 15:05:26 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-04 15:04:56 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-07-04 15:04:55 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:04:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-04 15:04:47 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:04:43 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:04:12 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-07-04 15:04:11 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 15:03:46 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-04 15:03:22 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-07-04 15:03:18 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-07-04 15:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-07-04 15:03:11 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:03:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:02:45 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:02:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:02:44 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 15:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 15:02:08 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 15:02:01 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:02:00 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-04 15:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:01:39 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:01:18 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:00:59 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 15:00:53 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:00:52 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:00:41 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:00:09 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.055 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 15:13:09 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-07-04 15:03:22 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-07-04 15:07:00 | Holombuwa (Kelani Ganga) | 1.54 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-07-04 15:03:18 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-07-04 15:04:56 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-07-04 15:04:12 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-07-04 15:04:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-04 15:05:26 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-04 15:00:09 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-04 15:00:59 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 15:11:01 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-04 15:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 15:02:44 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 15:02:08 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 15:06:12 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 15:08:12 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 15:04:11 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 15:01:18 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:01:39 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:00:53 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:00:41 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:02:01 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:24:20 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:04:43 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:08:28 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:02:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:00:52 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:03:11 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:02:45 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:22:25 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:04:47 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:03:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:04:55 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-04 15:03:46 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-07-04 15:06:36 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-07-04 15:02:00 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-07-04 15:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-07-04 14:04:47 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)