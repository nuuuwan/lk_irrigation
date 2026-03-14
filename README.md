# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_09:12:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 09:12:26 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:11:10 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:10:05 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-14 09:09:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:09:36 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 09:09:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:09:27 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:08:34 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:06:03 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-03-14 09:06:01 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:05:48 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.067 |  |
| 2026-03-14 09:05:41 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-03-14 09:05:37 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.064 |  |
| 2026-03-14 09:04:09 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 09:04:07 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:04:04 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.136 |  |
| 2026-03-14 09:04:03 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-14 09:03:53 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.023 |  |
| 2026-03-14 09:03:40 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.079 |  |
| 2026-03-14 09:03:37 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 09:03:24 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:03:11 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 09:02:53 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-03-14 09:02:31 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.051 |  |
| 2026-03-14 09:02:28 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 09:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.070 |  |
| 2026-03-14 09:02:26 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:02:15 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:02:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:02:10 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:01:51 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 09:01:44 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.060 |  |
| 2026-03-14 09:01:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-03-14 09:01:27 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-03-14 09:01:22 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 09:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 09:00:36 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-14 09:00:19 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 09:01:51 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 09:03:11 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 09:04:03 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-14 09:04:09 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-14 09:03:37 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 09:10:05 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-14 09:01:22 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 09:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 09:02:28 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 09:09:36 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 09:09:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:00:19 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:09:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:00:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:11:10 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:06:01 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:08:34 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:09:27 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:02:45 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:12:26 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:02:26 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:02:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:02:10 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:04:07 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:02:15 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 09:00:36 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-03-14 09:06:03 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-03-14 09:05:41 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-03-14 09:01:27 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-03-14 09:03:53 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.023 |  |
| 2026-03-14 09:02:53 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-03-14 09:01:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-03-14 09:02:31 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.051 |  |
| 2026-03-14 09:01:44 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.060 |  |
| 2026-03-14 09:05:37 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.064 |  |
| 2026-03-14 09:05:48 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.067 |  |
| 2026-03-14 09:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.070 |  |
| 2026-03-14 09:03:40 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.079 |  |
| 2026-03-14 09:04:04 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)