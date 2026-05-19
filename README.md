# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_17:12:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,257 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 17:12:36 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-05-19 17:12:07 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-05-19 17:10:40 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.018 |  |
| 2026-05-19 17:08:41 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:07:34 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:07:23 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:06:28 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:06:08 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:06:03 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.060 |  |
| 2026-05-19 17:05:56 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:05:47 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:05:04 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:04:55 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-19 17:04:52 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:04:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:04:29 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:04:24 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:04:18 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:04:15 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.037 |  |
| 2026-05-19 17:03:57 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:03:41 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:03:39 | Thanthirimale (Malwathu Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:03:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-19 17:03:23 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-05-19 17:03:13 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | -0.039 |  |
| 2026-05-19 17:03:06 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:03:03 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:02:30 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:02:00 | Moragaswewa (Deduru Oya) | 1.63 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-19 17:01:52 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:01:34 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | -0.017 |  |
| 2026-05-19 17:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:01:16 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:00:48 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-05-19 17:00:15 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:00:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:27:16 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 17:00:48 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-05-19 17:03:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-19 17:02:00 | Moragaswewa (Deduru Oya) | 1.63 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-19 17:04:55 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-19 16:14:30 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-19 17:01:52 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:05:56 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:04:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:07:34 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:04:29 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:02:30 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:03:57 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:06:28 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:05:47 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:08:41 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:05:04 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:06:08 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:07:23 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:03:06 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:12:36 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-05-19 17:03:39 | Thanthirimale (Malwathu Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:04:24 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:03:41 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:04:52 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:00:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:04:18 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:03:03 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:00:15 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:04:15 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-19 17:01:16 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-19 16:04:17 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-05-19 17:03:23 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-05-19 17:12:07 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-05-19 17:01:34 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | -0.017 |  |
| 2026-05-19 17:10:40 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.018 |  |
| 2026-05-19 17:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.037 |  |
| 2026-05-19 17:03:13 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | -0.039 |  |
| 2026-05-19 17:06:03 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)