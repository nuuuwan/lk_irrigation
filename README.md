# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_08:12:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,409 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 08:12:19 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.034 |  |
| 2026-05-14 08:11:30 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:11:00 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | -0.119 |  |
| 2026-05-14 08:10:25 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:09:28 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | -0.028 |  |
| 2026-05-14 08:09:09 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-05-14 08:08:45 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:07:27 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.038 |  |
| 2026-05-14 08:07:15 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:05:55 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.038 |  |
| 2026-05-14 08:05:39 | Galgamuwa (Mee Oya) | 2.68 | 🟢 Normal | -0.021 |  |
| 2026-05-14 08:05:07 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.060 |  |
| 2026-05-14 08:04:45 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.089 |  |
| 2026-05-14 08:04:31 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:04:26 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:04:21 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-14 08:04:18 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:03:56 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | -0.028 |  |
| 2026-05-14 08:03:34 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:03:23 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.34 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-05-14 08:02:40 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.200 |  |
| 2026-05-14 08:02:34 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:02:15 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-05-14 08:02:14 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-05-14 08:02:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-14 08:02:09 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:02:08 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-14 08:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-05-14 08:01:55 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.046 |  |
| 2026-05-14 08:01:55 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:01:55 | Dunamale (Aththanagalu Oya) | 3.09 | 🟢 Normal | -0.053 |  |
| 2026-05-14 08:01:53 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:01:26 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.057 |  |
| 2026-05-14 08:01:23 | Thanthirimale (Malwathu Oya) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:01:19 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:01:02 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.020 |  |
| 2026-05-14 08:00:42 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:00:36 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 08:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.34 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-05-14 08:09:28 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | -0.028 |  |
| 2026-05-14 08:02:12 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-14 08:04:21 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-14 08:02:08 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-14 08:00:36 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-14 08:00:42 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:02:09 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:04:26 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:08:45 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:03:23 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:03:34 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:02:34 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:04:18 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:11:30 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:10:25 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:04:31 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 08:07:15 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:01:19 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:01:23 | Thanthirimale (Malwathu Oya) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:01:55 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:01:53 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-14 08:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-05-14 08:02:14 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-05-14 08:01:02 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.020 |  |
| 2026-05-14 08:05:39 | Galgamuwa (Mee Oya) | 2.68 | 🟢 Normal | -0.021 |  |
| 2026-05-14 08:03:56 | Moraketiya (Walawe Ganga) | 1.73 | 🟢 Normal | -0.028 |  |
| 2026-05-14 08:02:15 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-05-14 08:12:19 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.034 |  |
| 2026-05-14 08:09:09 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-05-14 08:07:27 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.038 |  |
| 2026-05-14 08:05:55 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.038 |  |
| 2026-05-14 08:01:55 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.046 |  |
| 2026-05-14 08:01:55 | Dunamale (Aththanagalu Oya) | 3.09 | 🟢 Normal | -0.053 |  |
| 2026-05-14 08:01:26 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.057 |  |
| 2026-05-14 08:05:07 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.060 |  |
| 2026-05-14 08:04:45 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.089 |  |
| 2026-05-14 08:11:00 | Rathnapura (Kalu Ganga) | 4.35 | 🟢 Normal | -0.119 |  |
| 2026-05-14 08:02:40 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)