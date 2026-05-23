# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_18:09:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,848 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 18:09:40 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.014 |  |
| 2026-05-23 18:07:51 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.028 |  |
| 2026-05-23 18:07:28 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:07:02 | Nagalagam Street (Kelani Ganga) | 1.22 | 🟡 Alert | 0.000 |  |
| 2026-05-23 18:06:57 | Nagalagam Street (Kelani Ganga) | 1.22 | 🟡 Alert | 0.000 |  |
| 2026-05-23 18:05:13 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:05:07 | Dunamale (Aththanagalu Oya) | 4.90 | 🟠 Minor Flood | -0.039 |  |
| 2026-05-23 18:05:01 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.011 |  |
| 2026-05-23 18:04:53 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | -0.087 |  |
| 2026-05-23 18:04:40 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:03:48 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.021 |  |
| 2026-05-23 18:03:35 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.092 |  |
| 2026-05-23 18:03:21 | Hanwella (Kelani Ganga) | 6.09 | 🟢 Normal | -0.103 |  |
| 2026-05-23 18:03:09 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.041 |  |
| 2026-05-23 18:03:07 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.068 |  |
| 2026-05-23 18:02:43 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:02:42 | Putupaula (Kalu Ganga) | 3.17 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 18:02:26 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-05-23 18:02:22 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:02:21 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-05-23 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 18:02:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:02:04 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 18:02:02 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:45 | Magura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.072 |  |
| 2026-05-23 18:01:42 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-23 18:01:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:35 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:32 | Ellagawa (Kalu Ganga) | 10.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:09 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:07 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:53 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:42 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:30 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 18:05:07 | Dunamale (Aththanagalu Oya) | 4.90 | 🟠 Minor Flood | -0.039 |  |
| 2026-05-23 18:01:32 | Ellagawa (Kalu Ganga) | 10.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 18:02:42 | Putupaula (Kalu Ganga) | 3.17 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 18:07:02 | Nagalagam Street (Kelani Ganga) | 1.22 | 🟡 Alert | 0.000 |  |
| 2026-05-23 18:03:35 | Rathnapura (Kalu Ganga) | 5.62 | 🟡 Alert | -0.092 |  |
| 2026-05-23 18:01:42 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-23 18:02:04 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 18:01:09 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:07 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:35 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:30 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:05:13 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:07:28 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:07:40 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:53 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:02:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:02:02 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:00:42 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:40 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:02:43 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:21:54 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:02:22 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:05:01 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.011 |  |
| 2026-05-23 18:09:40 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.014 |  |
| 2026-05-23 18:02:26 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-05-23 18:03:48 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.021 |  |
| 2026-05-23 18:02:21 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-05-23 18:07:51 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.028 |  |
| 2026-05-23 18:03:09 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.041 |  |
| 2026-05-23 18:03:07 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.068 |  |
| 2026-05-23 18:01:45 | Magura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.072 |  |
| 2026-05-23 18:04:53 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | -0.087 |  |
| 2026-05-23 18:03:21 | Hanwella (Kelani Ganga) | 6.09 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)