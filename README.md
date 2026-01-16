# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_10:19:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 10:19:49 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-16 10:14:36 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.055 |  |
| 2026-01-16 10:09:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-16 10:08:19 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-16 10:07:28 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:07:21 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:06:17 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:06:17 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 10:06:05 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:05:49 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-01-16 10:05:48 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.079 |  |
| 2026-01-16 10:05:14 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:04:53 | Thanthirimale (Malwathu Oya) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-01-16 10:04:13 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.032 |  |
| 2026-01-16 10:04:12 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:04:12 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:04:11 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-01-16 10:03:51 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:49 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:39 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:03:36 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:24 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 10:03:03 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:02:50 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:02:35 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-01-16 10:02:22 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:02:18 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-01-16 10:02:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-16 10:02:09 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:02:07 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:01:52 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-16 10:01:47 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:01:46 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-01-16 10:01:18 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 10:01:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:01:09 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:00:47 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:00:36 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 10:08:19 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-16 10:01:52 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-16 10:02:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-16 10:09:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-16 10:19:49 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-16 10:06:17 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 10:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 10:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 10:01:18 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:01:10 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:01:09 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:03 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:01:47 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:04:12 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:04:12 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:49 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:06:17 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:02:22 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:06:05 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:02:07 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:51 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:24 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:03:36 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:07:28 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-16 10:02:09 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:05:14 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:03:39 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:07:21 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:00:36 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:02:50 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-16 10:02:35 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-01-16 10:01:46 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-01-16 10:04:53 | Thanthirimale (Malwathu Oya) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-01-16 10:04:11 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-01-16 10:05:49 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-01-16 10:02:18 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-01-16 10:04:13 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.032 |  |
| 2026-01-16 10:14:36 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.055 |  |
| 2026-01-16 10:05:48 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)