# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_05:25:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,107 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 05:25:09 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:20:00 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.064 |  |
| 2026-05-16 05:13:46 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.052 |  |
| 2026-05-16 05:10:18 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.047 |  |
| 2026-05-16 05:09:15 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.035 |  |
| 2026-05-16 05:08:18 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-05-16 05:08:12 | Baddegama (Gin Ganga) | 3.04 | 🟢 Normal | -0.019 |  |
| 2026-05-16 05:07:01 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-05-16 05:05:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:05:27 | Moragaswewa (Deduru Oya) | 3.34 | 🟢 Normal | -0.363 |  |
| 2026-05-16 05:05:00 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-16 05:03:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:03:43 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.023 |  |
| 2026-05-16 05:03:23 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.134 |  |
| 2026-05-16 05:03:10 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.052 |  |
| 2026-05-16 05:03:06 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 05:03:05 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-05-16 05:03:00 | Hanwella (Kelani Ganga) | 4.14 | 🟢 Normal | -0.041 |  |
| 2026-05-16 05:02:52 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.059 |  |
| 2026-05-16 05:02:49 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-05-16 05:02:45 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-05-16 05:02:40 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-16 05:02:37 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-16 05:02:23 | Dunamale (Aththanagalu Oya) | 4.48 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-16 05:02:15 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:01:52 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-16 05:01:45 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:01:39 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-16 05:01:25 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-16 05:01:07 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 04:22:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.11 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-05-16 05:02:23 | Dunamale (Aththanagalu Oya) | 4.48 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-16 05:05:00 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 05:01:25 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-16 05:03:06 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 05:02:37 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-16 05:03:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:01:45 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:17:00 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:05:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:02:15 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:33:57 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:06:46 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:25:09 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 05:07:01 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-05-16 05:01:52 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-16 05:02:40 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-16 05:01:39 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-16 05:02:49 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-05-16 05:03:05 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-05-16 05:08:18 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-05-16 03:11:00 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.018 |  |
| 2026-05-16 05:08:12 | Baddegama (Gin Ganga) | 3.04 | 🟢 Normal | -0.019 |  |
| 2026-05-16 05:02:45 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-05-16 05:03:43 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.023 |  |
| 2026-05-16 04:02:52 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | -0.032 |  |
| 2026-05-16 05:09:15 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.035 |  |
| 2026-05-16 05:03:00 | Hanwella (Kelani Ganga) | 4.14 | 🟢 Normal | -0.041 |  |
| 2026-05-16 05:01:07 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.043 |  |
| 2026-05-16 05:10:18 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.047 |  |
| 2026-05-16 05:03:10 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.052 |  |
| 2026-05-16 05:13:46 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.052 |  |
| 2026-05-16 05:02:52 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.059 |  |
| 2026-05-16 05:20:00 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.064 |  |
| 2026-05-16 05:03:23 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.134 |  |
| 2026-05-16 05:05:27 | Moragaswewa (Deduru Oya) | 3.34 | 🟢 Normal | -0.363 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)