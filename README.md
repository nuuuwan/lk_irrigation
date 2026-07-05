# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_20:27:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 20:27:17 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.007 |  |
| 2026-07-05 20:13:42 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:09:30 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:09:25 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:09:25 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-07-05 20:09:05 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:08:40 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-07-05 20:06:42 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:06:20 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.040 |  |
| 2026-07-05 20:05:46 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-07-05 20:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.228 |  |
| 2026-07-05 20:05:21 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:05:20 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:05:12 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.078 |  |
| 2026-07-05 20:05:01 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:04:50 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-05 20:03:58 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:03:50 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.041 |  |
| 2026-07-05 20:03:40 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:03:36 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:03:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.095 |  |
| 2026-07-05 20:03:24 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:02:51 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:02:50 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.037 |  |
| 2026-07-05 20:02:48 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.029 |  |
| 2026-07-05 20:02:46 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:02:29 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.044 |  |
| 2026-07-05 20:02:23 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:02:15 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.060 |  |
| 2026-07-05 20:02:12 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:01:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:01:45 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:01:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-07-05 20:00:50 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:00:39 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:00:20 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-07-05 19:55:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.228 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 20:09:25 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-07-05 20:04:50 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-05 20:00:39 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:00:50 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:02:23 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:01:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:02:51 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:03:24 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:03:58 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:03:36 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:09:25 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:06:42 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:13:42 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:02:12 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:09:05 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:05:21 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 20:27:17 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.007 |  |
| 2026-07-05 20:05:01 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:01:45 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:05:20 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:02:46 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:00:20 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:03:40 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:09:30 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-07-05 20:05:46 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-07-05 20:08:40 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-07-05 20:01:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-07-05 20:02:48 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.029 |  |
| 2026-07-05 20:02:50 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.037 |  |
| 2026-07-05 20:06:20 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.040 |  |
| 2026-07-05 20:03:50 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.041 |  |
| 2026-07-05 20:02:29 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.044 |  |
| 2026-07-05 20:02:15 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.060 |  |
| 2026-07-05 20:05:12 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.078 |  |
| 2026-07-05 20:03:35 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.095 |  |
| 2026-07-05 20:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.228 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)