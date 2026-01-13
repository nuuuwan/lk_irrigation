# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_09:18:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,333 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 09:18:50 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:16:58 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:12:06 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.039 |  |
| 2026-01-13 09:09:37 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-13 09:09:08 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 09:08:47 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-01-13 09:08:37 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 09:08:35 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.039 |  |
| 2026-01-13 09:07:53 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-13 09:07:35 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-01-13 09:07:34 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:06:36 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.306 |  |
| 2026-01-13 09:05:35 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-13 09:05:35 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-01-13 09:04:49 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:04:48 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:04:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 09:04:39 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:04:39 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.062 |  |
| 2026-01-13 09:04:30 | Horowpothana (Yan Oya) | 3.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 09:04:22 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.012 |  |
| 2026-01-13 09:03:51 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:03:47 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-01-13 09:03:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:03:15 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.098 |  |
| 2026-01-13 09:03:07 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 09:03:05 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 09:03:04 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-01-13 09:02:56 | Thanthirimale (Malwathu Oya) | 2.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 09:02:14 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.032 |  |
| 2026-01-13 09:02:13 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.041 |  |
| 2026-01-13 09:02:08 | Baddegama (Gin Ganga) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-01-13 09:01:37 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:01:35 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.054 |  |
| 2026-01-13 09:01:33 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 09:01:28 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-01-13 09:01:22 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:01:21 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:00:44 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:28:30 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 09:01:28 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-01-13 09:04:30 | Horowpothana (Yan Oya) | 3.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 09:03:05 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 09:02:56 | Thanthirimale (Malwathu Oya) | 2.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 09:07:53 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-13 09:03:07 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 09:04:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 09:09:08 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-13 09:01:22 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:02:13 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:01:21 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:04:49 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:01:37 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:04:39 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:18:50 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:03:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:07:34 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 09:03:51 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 08:28:30 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-01-13 09:07:35 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-01-13 09:05:35 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-13 09:05:35 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-01-13 09:09:37 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-13 09:01:33 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 09:08:37 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 09:02:08 | Baddegama (Gin Ganga) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-01-13 09:04:22 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.012 |  |
| 2026-01-13 09:03:47 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-01-13 09:08:47 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-01-13 09:03:04 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-01-13 09:02:14 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.032 |  |
| 2026-01-13 09:08:35 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.039 |  |
| 2026-01-13 09:12:06 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.039 |  |
| 2026-01-13 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | -0.041 |  |
| 2026-01-13 09:01:35 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.054 |  |
| 2026-01-13 09:04:39 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.062 |  |
| 2026-01-13 09:03:15 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.098 |  |
| 2026-01-13 09:06:36 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.306 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)