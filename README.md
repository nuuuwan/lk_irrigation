# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_20:11:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 20:11:29 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | -0.018 |  |
| 2026-05-14 20:10:07 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.094 |  |
| 2026-05-14 20:09:19 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-14 20:08:41 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:07:52 | Magura (Kalu Ganga) | 5.01 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-05-14 20:07:45 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-14 20:07:09 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | -0.079 |  |
| 2026-05-14 20:06:52 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 20:06:36 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.010 |  |
| 2026-05-14 20:05:33 | Badalgama (Maha Oya) | 4.02 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-05-14 20:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-14 20:04:47 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.021 |  |
| 2026-05-14 20:04:07 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-14 20:04:01 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:03:56 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-14 20:03:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-14 20:03:41 | Katharagama (Menik Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:03:37 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:03:25 | Glencourse (Kelani Ganga) | 13.48 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-05-14 20:03:13 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.076 |  |
| 2026-05-14 20:03:09 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-14 20:02:59 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-05-14 20:02:56 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-05-14 20:02:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:02:39 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.173 | 🔺 Rising |
| 2026-05-14 20:02:37 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 20:02:11 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-05-14 20:01:46 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-05-14 20:01:43 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.031 |  |
| 2026-05-14 20:01:42 | Giriulla (Maha Oya) | 3.56 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-14 20:01:22 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:00:22 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:00:19 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:00:05 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-14 19:29:33 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 20:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-14 20:02:39 | Dunamale (Aththanagalu Oya) | 4.02 | 🟡 Alert | 0.173 | 🔺 Rising |
| 2026-05-14 20:07:52 | Magura (Kalu Ganga) | 5.01 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-05-14 20:02:59 | Hanwella (Kelani Ganga) | 4.13 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-05-14 20:03:25 | Glencourse (Kelani Ganga) | 13.48 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-05-14 16:04:04 | Deraniyagala (Kelani Ganga) | 3.81 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-14 20:05:33 | Badalgama (Maha Oya) | 4.02 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-05-14 20:01:42 | Giriulla (Maha Oya) | 3.56 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-14 20:03:56 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-14 20:03:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-14 20:09:19 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-14 20:06:52 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 20:04:07 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-14 20:07:45 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-14 20:02:37 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:00:19 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:02:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:00:22 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:03:41 | Katharagama (Menik Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:08:41 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:04:01 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:03:37 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:01:22 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 20:02:11 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-05-14 20:06:36 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.010 |  |
| 2026-05-14 20:03:09 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-14 20:00:05 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-14 20:11:29 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | -0.018 |  |
| 2026-05-14 20:02:56 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-05-14 20:01:46 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-05-14 20:04:47 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.021 |  |
| 2026-05-14 19:01:08 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.023 |  |
| 2026-05-14 20:01:43 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.031 |  |
| 2026-05-14 20:03:13 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.076 |  |
| 2026-05-14 20:07:09 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | -0.079 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-14 20:10:07 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)