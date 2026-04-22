# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_03:11:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 03:11:52 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -36.000 |  |
| 2026-04-23 03:11:51 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -36.000 |  |
| 2026-04-23 03:11:50 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -36.000 |  |
| 2026-04-23 03:11:49 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -36.000 |  |
| 2026-04-23 03:10:46 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.098 |  |
| 2026-04-23 03:08:38 | Thanamalwila (Kirindi Oya) | 2.56 | 🟢 Normal | -0.128 |  |
| 2026-04-23 03:06:05 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-04-23 03:06:04 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:05:04 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.079 |  |
| 2026-04-23 03:04:56 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 4.114 | 🔺 Rising |
| 2026-04-23 03:04:40 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 21.176 | 🔺 Rising |
| 2026-04-23 03:04:30 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.177 |  |
| 2026-04-23 03:04:30 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 03:04:23 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 21.176 | 🔺 Rising |
| 2026-04-23 03:04:21 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 4.114 | 🔺 Rising |
| 2026-04-23 03:04:16 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-23 03:04:07 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 03:04:03 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 21.176 | 🔺 Rising |
| 2026-04-23 03:03:52 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-23 03:03:50 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-23 03:03:47 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-23 03:03:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:02:58 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-04-23 03:02:38 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-04-23 03:02:30 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-04-23 03:02:24 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:02:22 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-04-23 03:02:20 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-04-23 03:02:11 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:01:40 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-04-23 03:01:09 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-04-23 03:01:06 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:01:02 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:00:48 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | -0.080 |  |
| 2026-04-23 03:00:39 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.065 |  |
| 2026-04-23 02:46:15 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.098 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 03:03:52 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-23 03:04:40 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 21.176 | 🔺 Rising |
| 2026-04-23 03:04:56 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 4.114 | 🔺 Rising |
| 2026-04-23 03:02:58 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-04-23 03:02:22 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-04-23 02:00:34 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-23 03:03:47 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-23 03:04:30 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 03:04:16 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-23 03:04:07 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 01:05:04 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-23 02:19:30 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-23 03:01:06 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:02:24 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:02:11 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:03:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-23 02:10:44 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:06:04 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-23 03:01:02 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 00:12:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-23 03:02:38 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-23 03:01:40 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-04-23 03:06:05 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-04-23 02:07:23 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-04-23 03:02:20 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-04-23 03:02:30 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-04-23 00:07:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.039 |  |
| 2026-04-23 03:01:09 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-04-23 03:00:39 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.065 |  |
| 2026-04-23 03:05:04 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.079 |  |
| 2026-04-23 03:00:48 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | -0.080 |  |
| 2026-04-23 03:10:46 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.098 |  |
| 2026-04-23 03:08:38 | Thanamalwila (Kirindi Oya) | 2.56 | 🟢 Normal | -0.128 |  |
| 2026-04-23 03:04:30 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.177 |  |
| 2026-04-23 02:05:30 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -4.909 |  |
| 2026-04-23 03:11:52 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)