# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_01:21:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 01:21:27 | Moragaswewa (Deduru Oya) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:18:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 01:11:58 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-16 01:10:24 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-05-16 01:08:28 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.029 |  |
| 2026-05-16 01:07:58 | Hanwella (Kelani Ganga) | 4.35 | 🟢 Normal | -0.091 |  |
| 2026-05-16 01:07:23 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.020 |  |
| 2026-05-16 01:07:05 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.031 |  |
| 2026-05-16 01:05:55 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:05:53 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:05:39 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.048 |  |
| 2026-05-16 01:05:00 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:04:38 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:04:26 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:04:05 | Giriulla (Maha Oya) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:04:02 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:04:01 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:04:01 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:03:41 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | -0.020 |  |
| 2026-05-16 01:03:37 | Moragaswewa (Deduru Oya) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:03:32 | Badalgama (Maha Oya) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:03:11 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.068 |  |
| 2026-05-16 01:02:53 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.112 |  |
| 2026-05-16 01:02:52 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 01:02:22 | Dunamale (Aththanagalu Oya) | 4.56 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-16 01:02:03 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:01:53 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:01:33 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:01:33 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.073 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 01:18:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 01:02:22 | Dunamale (Aththanagalu Oya) | 4.56 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-16 01:07:23 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.020 |  |
| 2026-05-16 01:02:52 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 01:11:58 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-16 01:04:01 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:21:27 | Moragaswewa (Deduru Oya) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:43 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:04:38 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:04:01 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:01:33 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:04:02 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:05:53 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:05:39 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:14:10 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:01:18 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:05:00 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-16 01:05:55 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:04:05 | Giriulla (Maha Oya) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:01:23 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:02:03 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:03:32 | Badalgama (Maha Oya) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:04:26 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-16 01:01:53 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-05-16 00:05:45 | Horowpothana (Yan Oya) | 2.93 | 🟢 Normal | -0.019 |  |
| 2026-05-16 01:10:24 | Baddegama (Gin Ganga) | 3.14 | 🟢 Normal | -0.020 |  |
| 2026-05-16 01:03:41 | Ellagawa (Kalu Ganga) | 8.66 | 🟢 Normal | -0.020 |  |
| 2026-05-16 01:08:28 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.029 |  |
| 2026-05-16 01:07:05 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.031 |  |
| 2026-05-16 00:05:47 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.047 |  |
| 2026-05-16 01:05:39 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.048 |  |
| 2026-05-16 00:01:11 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.061 |  |
| 2026-05-16 01:03:11 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.068 |  |
| 2026-05-16 01:01:33 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.073 |  |
| 2026-05-16 01:07:58 | Hanwella (Kelani Ganga) | 4.35 | 🟢 Normal | -0.091 |  |
| 2026-05-16 01:02:53 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)