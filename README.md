# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_16:10:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 16:10:23 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:10:09 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:08:43 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:08:18 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.009 |  |
| 2026-02-14 16:07:42 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:07:24 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.038 |  |
| 2026-02-14 16:07:22 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-14 16:07:03 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:06:38 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:06:28 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.048 |  |
| 2026-02-14 16:06:18 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:05:56 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.066 |  |
| 2026-02-14 16:05:11 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:05:07 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:04:40 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:04:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:04:22 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:04:21 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:04:02 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-14 16:03:49 | Padiyathalawa (Maduru Oya) | 3.80 | 🟢 Normal | -0.337 |  |
| 2026-02-14 16:03:45 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:03:31 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-14 16:03:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:03:19 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:03:03 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-02-14 16:02:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:02:27 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:02:21 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:02:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:01:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:01:35 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:01:29 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:00:58 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:00:52 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-02-14 16:00:30 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:00:21 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 16:03:03 | Weraganthota (Mahaweli Ganga) | -1.64 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-02-14 16:07:22 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-14 16:03:31 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-14 16:04:02 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-14 15:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:04:22 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:03:19 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:02:27 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:02:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:07:03 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 16:01:35 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:00:21 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:01:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:10:23 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 15:04:21 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:04:21 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:04:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:03:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:03:45 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:01:29 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:08:43 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:05:11 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:02:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:10:09 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:02:21 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 16:08:18 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.009 |  |
| 2026-02-14 16:04:40 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:07:42 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:06:18 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:05:07 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:00:58 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:06:38 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:00:30 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-14 16:00:52 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-02-14 16:07:24 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.038 |  |
| 2026-02-14 16:06:28 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.048 |  |
| 2026-02-14 16:05:56 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.066 |  |
| 2026-02-14 16:03:49 | Padiyathalawa (Maduru Oya) | 3.80 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)