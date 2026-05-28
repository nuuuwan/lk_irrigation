# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_04:43:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,486 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 04:43:51 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-29 04:40:07 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-05-29 04:12:13 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:08:03 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-29 04:07:20 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.161 |  |
| 2026-05-29 04:07:07 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.146 |  |
| 2026-05-29 04:05:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-05-29 04:05:01 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:04:59 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:04:31 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.010 |  |
| 2026-05-29 04:04:28 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.078 |  |
| 2026-05-29 04:04:21 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 04:04:16 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.215 |  |
| 2026-05-29 04:04:12 | Rathnapura (Kalu Ganga) | 4.88 | 🟢 Normal | -0.135 |  |
| 2026-05-29 04:04:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:03:49 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.051 |  |
| 2026-05-29 04:03:23 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.060 |  |
| 2026-05-29 04:02:49 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-29 04:02:49 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:02:41 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:02:37 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.212 |  |
| 2026-05-29 04:02:11 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.079 |  |
| 2026-05-29 04:02:00 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 04:01:41 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:01:39 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-29 04:01:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:01:33 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:01:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:01:03 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-05-29 04:00:32 | Glencourse (Kelani Ganga) | 12.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 04:00:17 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 03:00:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-05-29 04:04:31 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | -0.010 |  |
| 2026-05-29 04:03:23 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.060 |  |
| 2026-05-29 04:01:39 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-29 04:02:49 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-29 04:00:17 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-29 04:43:51 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-29 03:06:25 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-29 04:00:32 | Glencourse (Kelani Ganga) | 12.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 04:02:00 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 04:04:21 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 04:08:03 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-29 04:01:07 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:01:33 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:12:13 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:02:41 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:01:41 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:05:01 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:04:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:01:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:02:49 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-29 02:06:29 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 04:04:59 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-29 04:40:07 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-05-29 04:01:03 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-05-29 04:05:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-05-29 04:03:49 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.051 |  |
| 2026-05-29 04:04:28 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.078 |  |
| 2026-05-29 04:02:11 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.079 |  |
| 2026-05-29 04:04:12 | Rathnapura (Kalu Ganga) | 4.88 | 🟢 Normal | -0.135 |  |
| 2026-05-29 04:07:07 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.146 |  |
| 2026-05-29 04:07:20 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.161 |  |
| 2026-05-29 03:02:14 | Pitabeddara (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.194 |  |
| 2026-05-29 04:02:37 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.212 |  |
| 2026-05-29 04:04:16 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.215 |  |
| 2026-05-29 03:05:57 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | -1.800 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)