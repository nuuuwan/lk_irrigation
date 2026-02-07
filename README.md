# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_11:23:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,533 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 11:23:21 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.007 |  |
| 2026-02-07 11:21:02 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:18:34 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-02-07 11:14:04 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-07 11:12:53 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:11:14 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:08:09 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-02-07 11:07:17 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.113 |  |
| 2026-02-07 11:07:00 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-02-07 11:05:47 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.028 |  |
| 2026-02-07 11:05:03 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.038 |  |
| 2026-02-07 11:04:30 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:04:23 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-02-07 11:04:17 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-02-07 11:04:15 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.062 |  |
| 2026-02-07 11:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | -0.013 |  |
| 2026-02-07 11:03:46 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:03:30 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 11:03:17 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:02:58 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:02:48 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.098 |  |
| 2026-02-07 11:02:28 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:02:26 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:02:25 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:02:23 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 11:02:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:02:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:02:04 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:01:52 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-02-07 11:01:49 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:01:45 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-02-07 11:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:01:31 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:01:28 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-07 11:01:17 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:01:11 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:01:01 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:00:52 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.034 |  |
| 2026-02-07 11:00:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:43:07 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 11:04:17 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-02-07 11:14:04 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-07 11:01:28 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-07 11:02:23 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 11:03:30 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 11:01:17 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:12:53 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:02:25 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:21:02 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:01:49 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:01:11 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:00:33 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:04:30 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:02:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:02:58 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:02:28 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:11:14 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:01:31 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-07 11:23:21 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.007 |  |
| 2026-02-07 11:02:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:01:01 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:03:17 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:03:46 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:02:04 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:02:26 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.010 |  |
| 2026-02-07 11:01:45 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-02-07 11:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | -0.013 |  |
| 2026-02-07 11:18:34 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-02-07 11:08:09 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-02-07 11:01:52 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-02-07 11:05:47 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | -0.028 |  |
| 2026-02-07 11:07:00 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-02-07 11:00:52 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.034 |  |
| 2026-02-07 11:05:03 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.038 |  |
| 2026-02-07 11:04:23 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-02-07 11:04:15 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.062 |  |
| 2026-02-07 11:02:48 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.098 |  |
| 2026-02-07 11:07:17 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)