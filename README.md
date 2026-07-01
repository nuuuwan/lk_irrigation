# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_23:23:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,747 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 23:23:46 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -180.000 |  |
| 2026-07-01 23:23:45 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -180.000 |  |
| 2026-07-01 23:18:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-07-01 23:14:40 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:12:55 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-07-01 23:09:04 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:06:53 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:06:21 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:06:10 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:05:48 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.040 |  |
| 2026-07-01 23:05:37 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:05:28 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-07-01 23:05:20 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.011 |  |
| 2026-07-01 23:04:17 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-07-01 23:04:12 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:04:09 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:03:45 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 23:03:20 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:03:12 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:53 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-07-01 23:02:45 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:02:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:30 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:21 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:11 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:01:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:01:19 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:01:02 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:00:34 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:00:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:00:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 23:02:53 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-07-01 23:03:45 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:11 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:30 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:06:03 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:01:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:00:34 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:21 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:04:09 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:04:12 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:00:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:06:10 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:39 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:00:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:03:20 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:03:12 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:02:09 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:05:37 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:01:02 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-01 22:07:56 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:14:40 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:01:19 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 23:18:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-07-01 23:12:55 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-07-01 23:09:04 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:06:53 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:06:21 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:02:45 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-01 23:05:20 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.011 |  |
| 2026-07-01 22:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.019 |  |
| 2026-07-01 23:05:28 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-07-01 23:04:17 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-07-01 23:05:48 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.040 |  |
| 2026-07-01 22:04:59 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.186 |  |
| 2026-07-01 23:23:46 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)