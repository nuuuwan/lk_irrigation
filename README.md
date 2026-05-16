# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_20:19:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,697 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 20:19:01 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | -0.116 |  |
| 2026-05-16 20:15:18 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-16 20:15:03 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-16 20:09:44 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-16 20:09:25 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:08:56 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.046 |  |
| 2026-05-16 20:08:14 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:07:58 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 20:06:31 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-16 20:06:05 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:05:23 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:05:14 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:05:08 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:05:00 | Magura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.039 |  |
| 2026-05-16 20:04:57 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.021 |  |
| 2026-05-16 20:04:56 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.020 |  |
| 2026-05-16 20:04:51 | Dunamale (Aththanagalu Oya) | 3.65 | 🟡 Alert | -0.010 |  |
| 2026-05-16 20:04:31 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.041 |  |
| 2026-05-16 20:04:11 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2026-05-16 20:04:04 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.089 |  |
| 2026-05-16 20:03:55 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.011 |  |
| 2026-05-16 20:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-16 20:03:04 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:02:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-16 20:02:32 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.039 |  |
| 2026-05-16 20:02:25 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-05-16 20:02:18 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:02:16 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:02:13 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-16 20:02:06 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:01:38 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-05-16 20:01:37 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-16 20:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 20:01:28 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | -0.032 |  |
| 2026-05-16 20:01:25 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 20:01:25 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 20:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 20:04:51 | Dunamale (Aththanagalu Oya) | 3.65 | 🟡 Alert | -0.010 |  |
| 2026-05-16 20:09:44 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-16 20:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-16 20:15:18 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-16 20:01:37 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-16 20:06:31 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-16 20:01:25 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 20:07:58 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 20:02:13 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-16 20:05:23 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:05:08 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:05:14 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:02:16 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:03:04 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:06:05 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:08:14 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:09:25 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:02:06 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:02:18 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 20:15:03 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-16 20:01:38 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-05-16 20:02:35 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-16 20:01:25 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-16 20:03:55 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.011 |  |
| 2026-05-16 20:02:25 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-05-16 20:04:56 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.020 |  |
| 2026-05-16 20:04:57 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.021 |  |
| 2026-05-16 20:04:11 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-16 20:01:28 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | -0.032 |  |
| 2026-05-16 20:02:32 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.039 |  |
| 2026-05-16 20:05:00 | Magura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.039 |  |
| 2026-05-16 20:04:31 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.041 |  |
| 2026-05-16 20:08:56 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.046 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-16 20:04:04 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.089 |  |
| 2026-05-16 20:19:01 | Moragaswewa (Deduru Oya) | 2.71 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)