# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_18:24:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 18:24:10 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-21 18:08:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:07:46 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-21 18:07:39 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-05-21 18:06:40 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.049 |  |
| 2026-05-21 18:06:38 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 18:06:21 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:05:50 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:05:40 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:05:25 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:04:31 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.031 |  |
| 2026-05-21 18:04:23 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:04:01 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:38 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:33 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-05-21 18:03:32 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.918 | 🔺 Rising |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-21 18:03:25 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:03:24 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-21 18:03:08 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:02:52 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:36 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 18:02:26 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:08 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:03 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:01:41 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:01:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:01:30 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:01:09 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:01:06 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-21 18:00:51 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-21 18:00:27 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:00:19 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:00:13 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 17:38:32 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 18:03:32 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.918 | 🔺 Rising |
| 2026-05-21 18:00:51 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-21 18:07:46 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-21 18:03:24 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-21 18:03:27 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-21 18:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 18:00:13 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 18:01:06 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 18:06:38 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-21 18:01:30 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:52 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:36 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:01:09 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:05:40 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:04:01 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:05:25 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:38 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:26 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:01:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:04:23 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 16:00:42 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:06:21 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:01:41 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:08:03 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:03 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:02:08 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:07:39 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-05-21 18:24:10 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:03:08 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:05:50 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:03:25 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:00:27 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-21 18:03:33 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-05-21 18:04:31 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.031 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-21 18:06:40 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)