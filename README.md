# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_03:05:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 03:05:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-09 03:05:02 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.143 |  |
| 2026-05-09 03:04:54 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-09 03:04:43 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.298 |  |
| 2026-05-09 03:04:37 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.018 |  |
| 2026-05-09 03:04:31 | Katharagama (Menik Ganga) | 1.29 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-05-09 03:04:01 | Kuda Oya (Kirindi Oya) | 5.52 | 🟢 Normal | -0.653 |  |
| 2026-05-09 03:03:49 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.078 |  |
| 2026-05-09 03:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-09 03:02:59 | Moraketiya (Walawe Ganga) | 2.27 | 🟢 Normal | -0.070 |  |
| 2026-05-09 03:02:53 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-09 03:02:19 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-09 03:02:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 03:02:16 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-05-09 03:02:08 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-09 03:01:33 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-09 03:01:25 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-05-09 03:01:24 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 03:00:53 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-09 03:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.132 |  |
| 2026-05-09 02:50:43 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.011 |  |
| 2026-05-09 02:31:37 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-05-09 02:30:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-09 02:27:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.21 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-09 02:27:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-09 02:27:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-09 02:17:02 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -270.000 |  |
| 2026-05-09 02:17:00 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | -270.000 |  |
| 2026-05-09 02:16:04 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.008 |  |
| 2026-05-09 02:14:23 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.063 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 02:06:00 | Thanamalwila (Kirindi Oya) | 6.39 | 🔴 Major Flood | -0.119 |  |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-09 02:06:48 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-05-09 03:04:31 | Katharagama (Menik Ganga) | 1.29 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-05-09 03:01:25 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-05-09 03:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-09 03:05:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-09 03:02:53 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-09 03:02:19 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-09 03:02:08 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-09 02:04:07 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 03:01:24 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:04:40 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-09 03:04:54 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-08 23:01:55 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-09 00:03:06 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:06:09 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 03:02:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 03:01:33 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:06:44 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:16:04 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.008 |  |
| 2026-05-09 03:00:53 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-09 02:50:43 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.011 |  |
| 2026-05-09 03:04:37 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.018 |  |
| 2026-05-09 00:01:45 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-09 03:02:16 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-05-09 02:06:19 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-09 02:07:30 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.062 |  |
| 2026-05-09 03:02:59 | Moraketiya (Walawe Ganga) | 2.27 | 🟢 Normal | -0.070 |  |
| 2026-05-09 02:01:07 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-05-09 03:03:49 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.078 |  |
| 2026-05-09 03:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.132 |  |
| 2026-05-09 03:05:02 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.143 |  |
| 2026-05-09 03:04:43 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.298 |  |
| 2026-05-09 02:05:42 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.374 |  |
| 2026-05-09 03:04:01 | Kuda Oya (Kirindi Oya) | 5.52 | 🟢 Normal | -0.653 |  |
| 2026-05-09 02:17:02 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -270.000 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)