# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_10:17:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,932 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 10:17:10 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.017 |  |
| 2026-05-27 10:14:20 | Rathnapura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-27 10:14:11 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-27 10:10:36 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.044 |  |
| 2026-05-27 10:08:56 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:08:34 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.018 |  |
| 2026-05-27 10:08:14 | Magura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.010 |  |
| 2026-05-27 10:07:54 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 10:06:57 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.061 |  |
| 2026-05-27 10:06:05 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | -0.039 |  |
| 2026-05-27 10:05:44 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:05:18 | Nagalagam Street (Kelani Ganga) | 0.75 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-27 10:05:08 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-05-27 10:05:03 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 10:04:50 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:04:30 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.012 |  |
| 2026-05-27 10:04:19 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-27 10:03:37 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 10:03:28 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.039 |  |
| 2026-05-27 10:03:22 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-27 10:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 10:02:52 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:02:25 | Ellagawa (Kalu Ganga) | 8.46 | 🟢 Normal | -0.041 |  |
| 2026-05-27 10:02:24 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:02:23 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-27 10:02:17 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:02:11 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:02:04 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 10:01:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.005 |  |
| 2026-05-27 10:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:01:37 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:01:12 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:01:12 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:31 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:30 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:18 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-27 10:00:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:06 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 10:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 10:03:22 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-27 10:05:18 | Nagalagam Street (Kelani Ganga) | 0.75 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-27 10:14:11 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-27 10:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-27 10:14:20 | Rathnapura (Kalu Ganga) | 3.52 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-27 10:04:19 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-27 10:02:04 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 10:05:03 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 10:03:37 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 10:07:54 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 10:00:18 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:06 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:02:17 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:01:12 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:02:24 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:30 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:08:56 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:05:44 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:01:37 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:02:52 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:00:31 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:04:50 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:01:12 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:02:11 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 10:01:51 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.005 |  |
| 2026-05-27 10:02:23 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-27 10:08:14 | Magura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.010 |  |
| 2026-05-27 10:05:08 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-05-27 10:04:30 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.012 |  |
| 2026-05-27 10:17:10 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.017 |  |
| 2026-05-27 10:08:34 | Glencourse (Kelani Ganga) | 11.34 | 🟢 Normal | -0.018 |  |
| 2026-05-27 10:03:28 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.039 |  |
| 2026-05-27 10:06:05 | Hanwella (Kelani Ganga) | 3.96 | 🟢 Normal | -0.039 |  |
| 2026-05-27 10:02:25 | Ellagawa (Kalu Ganga) | 8.46 | 🟢 Normal | -0.041 |  |
| 2026-05-27 10:10:36 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.044 |  |
| 2026-05-27 10:06:57 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)