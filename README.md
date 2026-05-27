# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_12:11:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,012 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 12:11:32 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:11:05 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-05-27 12:09:21 | Magura (Kalu Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:08:54 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 12:07:09 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:06:52 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.750 |  |
| 2026-05-27 12:06:34 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 12:06:25 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:06:12 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 12:05:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:05:34 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 12:05:23 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-27 12:05:16 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.750 |  |
| 2026-05-27 12:05:02 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 12:04:54 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:04:49 | Rathnapura (Kalu Ganga) | 3.82 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-05-27 12:04:33 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-27 12:04:08 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:04:01 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-27 12:03:53 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:03:47 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:03:29 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 12:03:07 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:03:06 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:02:50 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-27 12:02:49 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-27 12:02:25 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 12:02:18 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:02:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:02:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-05-27 12:02:08 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:02:07 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:01:48 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | -0.032 |  |
| 2026-05-27 12:01:36 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.020 |  |
| 2026-05-27 12:01:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:01:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:01:15 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 12:00:34 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:00:10 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 12:04:49 | Rathnapura (Kalu Ganga) | 3.82 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-05-27 12:04:33 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-27 12:02:49 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-05-27 12:02:50 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-27 12:04:01 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-27 12:06:12 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 12:03:29 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 12:06:34 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 12:05:34 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 12:05:02 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 12:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 12:08:54 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 12:00:34 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:01:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:05:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:02:25 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:09:21 | Magura (Kalu Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:06:25 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:01:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:02:08 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:11:32 | Dunamale (Aththanagalu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:04:08 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:03:53 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:01:15 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:02:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:02:18 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-27 12:05:23 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-27 12:07:09 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:02:07 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:03:06 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:03:47 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:03:07 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-05-27 12:02:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-05-27 12:11:05 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-05-27 12:01:36 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.020 |  |
| 2026-05-27 12:00:10 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-05-27 12:01:48 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | -0.032 |  |
| 2026-05-27 12:06:52 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.750 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)