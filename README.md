# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_05:16:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,339 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 05:16:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:13:44 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:10:45 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.028 |  |
| 2026-05-23 05:07:39 | Glencourse (Kelani Ganga) | 12.73 | 🟢 Normal | -0.171 |  |
| 2026-05-23 05:07:29 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | 0.000 |  |
| 2026-05-23 05:07:24 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:05:48 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-05-23 05:05:25 | Ellagawa (Kalu Ganga) | 9.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-23 05:04:58 | Magura (Kalu Ganga) | 4.06 | 🟡 Alert | -0.047 |  |
| 2026-05-23 05:04:48 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-23 05:04:35 | Rathnapura (Kalu Ganga) | 6.52 | 🟡 Alert | -0.078 |  |
| 2026-05-23 05:04:32 | Dunamale (Aththanagalu Oya) | 5.18 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 05:04:29 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-05-23 05:04:24 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.059 |  |
| 2026-05-23 05:03:54 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:03:52 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:03:41 | Deraniyagala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-05-23 05:03:21 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-23 05:02:34 | Hanwella (Kelani Ganga) | 7.38 | 🟡 Alert | -0.107 |  |
| 2026-05-23 05:02:27 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.029 |  |
| 2026-05-23 05:02:12 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:02:11 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.050 |  |
| 2026-05-23 05:01:35 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 05:01:25 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:01:21 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-23 05:01:13 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:00:57 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-23 05:00:48 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:59:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-23 04:31:32 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 05:04:32 | Dunamale (Aththanagalu Oya) | 5.18 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 05:07:29 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | 0.000 |  |
| 2026-05-23 03:15:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-05-23 05:04:58 | Magura (Kalu Ganga) | 4.06 | 🟡 Alert | -0.047 |  |
| 2026-05-23 05:04:35 | Rathnapura (Kalu Ganga) | 6.52 | 🟡 Alert | -0.078 |  |
| 2026-05-23 05:02:34 | Hanwella (Kelani Ganga) | 7.38 | 🟡 Alert | -0.107 |  |
| 2026-05-23 05:03:41 | Deraniyagala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-05-23 05:01:21 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-23 04:04:40 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-23 05:05:25 | Ellagawa (Kalu Ganga) | 9.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-23 03:07:46 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-23 05:01:35 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 05:00:57 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-23 05:00:48 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:01:25 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-23 01:03:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:13:44 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:07:24 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:03:52 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:01:13 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:02:12 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:03:54 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:16:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 04:17:40 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 05:05:48 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-05-23 05:03:21 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-23 04:59:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-23 05:04:48 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-23 05:10:45 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.028 |  |
| 2026-05-23 05:04:29 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-05-23 05:02:27 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.029 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-23 04:00:48 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.036 |  |
| 2026-05-23 05:02:11 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.050 |  |
| 2026-05-23 05:04:24 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.059 |  |
| 2026-05-23 05:07:39 | Glencourse (Kelani Ganga) | 12.73 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)