# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_09:27:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,168 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 09:27:12 | Thanthirimale (Malwathu Oya) | 3.46 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-09 09:18:15 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:14:10 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:07:58 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:07:53 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:06:45 | Weraganthota (Mahaweli Ganga) | -1.31 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2025-12-09 09:06:43 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.049 |  |
| 2025-12-09 09:05:53 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-09 09:05:52 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.021 |  |
| 2025-12-09 09:05:31 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:05:21 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:05:16 | Galgamuwa (Mee Oya) | 1.27 | 🟢 Normal | -0.019 |  |
| 2025-12-09 09:05:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:05:03 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:05:00 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:04:47 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.098 |  |
| 2025-12-09 09:04:36 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:04:29 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:04:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:04:16 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:04:12 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2025-12-09 09:03:59 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 09:03:47 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:03:35 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:03:29 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 09:03:14 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:02:49 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 09:02:41 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:02:26 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:02:15 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:02:00 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 09:01:55 | Thanthirimale (Malwathu Oya) | 3.42 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-09 09:01:43 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2025-12-09 09:01:27 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-09 09:01:12 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2025-12-09 09:01:07 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:00:08 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.309 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 09:00:08 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2025-12-09 09:05:53 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-09 09:01:43 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2025-12-09 09:06:45 | Weraganthota (Mahaweli Ganga) | -1.31 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2025-12-09 09:27:12 | Thanthirimale (Malwathu Oya) | 3.46 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-09 09:01:27 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-09 09:02:00 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 09:01:12 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 09:02:49 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 09:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 09:03:29 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 08:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 09:02:15 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:04:16 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 08:04:10 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:05:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:03:59 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:04:36 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:07:58 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:05:31 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:18:15 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:01:07 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:14:10 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:07:53 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:05:21 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:02:26 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:03:47 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:05:00 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:02:41 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:03:35 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:03:14 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:04:29 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2025-12-09 09:05:16 | Galgamuwa (Mee Oya) | 1.27 | 🟢 Normal | -0.019 |  |
| 2025-12-09 09:04:12 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2025-12-09 09:05:52 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.021 |  |
| 2025-12-09 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2025-12-09 09:06:43 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.049 |  |
| 2025-12-09 09:04:47 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)