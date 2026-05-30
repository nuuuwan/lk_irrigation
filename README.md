# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_19:20:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 19:20:15 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-30 19:18:23 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:13:17 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-05-30 19:12:31 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-05-30 19:08:57 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:08:56 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:08:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:08:06 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.028 |  |
| 2026-05-30 19:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.16 | 🟡 Alert | -0.039 |  |
| 2026-05-30 19:06:09 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:06:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.123 |  |
| 2026-05-30 19:05:32 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:05:12 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-30 19:04:30 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-30 19:04:18 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:04:14 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:04:04 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.030 |  |
| 2026-05-30 19:04:03 | Dunamale (Aththanagalu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:03:59 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.021 |  |
| 2026-05-30 19:03:50 | Ellagawa (Kalu Ganga) | 7.12 | 🟢 Normal | -0.120 |  |
| 2026-05-30 19:03:39 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-05-30 19:03:21 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.011 |  |
| 2026-05-30 19:03:06 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-30 19:03:00 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:02:37 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-30 19:02:15 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:02:09 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.070 |  |
| 2026-05-30 19:01:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:01:25 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-05-30 19:01:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:01:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:01:06 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:00:18 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 19:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.16 | 🟡 Alert | -0.039 |  |
| 2026-05-30 19:04:30 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-30 19:05:12 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:00:18 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:01:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:25:20 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:01:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:04:14 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:08:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:05:32 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:01:06 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:01:08 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:04:03 | Dunamale (Aththanagalu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:03:00 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:18:23 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:06:09 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:08:57 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:08:56 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:02:15 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 19:12:31 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.009 |  |
| 2026-05-30 19:13:17 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | -0.009 |  |
| 2026-05-30 19:20:15 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-30 19:02:37 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-30 19:03:06 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-30 19:03:21 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.011 |  |
| 2026-05-30 19:01:25 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-05-30 19:03:59 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.021 |  |
| 2026-05-30 19:03:39 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-05-30 19:08:06 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.028 |  |
| 2026-05-30 19:04:04 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.030 |  |
| 2026-05-30 18:03:01 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-05-30 19:02:09 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.070 |  |
| 2026-05-30 19:03:50 | Ellagawa (Kalu Ganga) | 7.12 | 🟢 Normal | -0.120 |  |
| 2026-05-30 19:06:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.123 |  |
| 2026-05-30 18:02:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -30.857 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)