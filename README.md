# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_15:21:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,850 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 15:21:06 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-22 15:18:07 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.177 |  |
| 2026-05-22 15:13:12 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-22 15:10:53 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.039 |  |
| 2026-05-22 15:10:46 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-05-22 15:08:24 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:07:05 | Nagalagam Street (Kelani Ganga) | 1.36 | 🟡 Alert | 0.075 | 🔺 Rising |
| 2026-05-22 15:07:03 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:06:36 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-22 15:06:35 | Glencourse (Kelani Ganga) | 15.43 | 🟡 Alert | -0.038 |  |
| 2026-05-22 15:06:04 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-22 15:06:01 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-05-22 15:05:59 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.064 |  |
| 2026-05-22 15:05:30 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | 54.000 | 🔺 Rising |
| 2026-05-22 15:05:28 | Magura (Kalu Ganga) | 4.40 | 🟡 Alert | 54.000 | 🔺 Rising |
| 2026-05-22 15:05:13 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-22 15:04:38 | Ellagawa (Kalu Ganga) | 9.23 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-22 15:04:33 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:04:27 | Dunamale (Aththanagalu Oya) | 5.06 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-05-22 15:04:05 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-22 15:03:38 | Rathnapura (Kalu Ganga) | 7.74 | 🟠 Minor Flood | -0.043 |  |
| 2026-05-22 15:03:34 | Hanwella (Kelani Ganga) | 8.13 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-05-22 15:03:04 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:58 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.357 |  |
| 2026-05-22 15:02:51 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.63 | 🟡 Alert | 0.111 | 🔺 Rising |
| 2026-05-22 15:02:16 | Deraniyagala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.131 |  |
| 2026-05-22 15:02:14 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:05 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:04 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-22 15:02:02 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:01:57 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-05-22 15:01:51 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-22 15:01:32 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.062 |  |
| 2026-05-22 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-05-22 15:01:05 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:01:03 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:00:16 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:00:14 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 15:00:13 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 15:04:27 | Dunamale (Aththanagalu Oya) | 5.06 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-05-22 15:03:34 | Hanwella (Kelani Ganga) | 8.13 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-05-22 15:03:38 | Rathnapura (Kalu Ganga) | 7.74 | 🟠 Minor Flood | -0.043 |  |
| 2026-05-22 15:05:30 | Magura (Kalu Ganga) | 4.43 | 🟡 Alert | 54.000 | 🔺 Rising |
| 2026-05-22 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.63 | 🟡 Alert | 0.111 | 🔺 Rising |
| 2026-05-22 15:07:05 | Nagalagam Street (Kelani Ganga) | 1.36 | 🟡 Alert | 0.075 | 🔺 Rising |
| 2026-05-22 15:06:35 | Glencourse (Kelani Ganga) | 15.43 | 🟡 Alert | -0.038 |  |
| 2026-05-22 15:06:36 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-05-22 15:05:13 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-22 15:04:38 | Ellagawa (Kalu Ganga) | 9.23 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-22 15:21:06 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-22 15:01:51 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-22 15:00:14 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 15:13:12 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-22 15:04:05 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-22 15:03:04 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:00:16 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:19 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:01:03 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:04:33 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:00:13 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:01:05 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:14 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:51 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:08:24 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:02:02 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:07:03 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-22 15:10:46 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-05-22 15:02:04 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-22 15:06:04 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-22 15:06:01 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-05-22 15:01:57 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-05-22 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.032 |  |
| 2026-05-22 15:10:53 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.039 |  |
| 2026-05-22 15:01:32 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.062 |  |
| 2026-05-22 15:05:59 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.064 |  |
| 2026-05-22 15:02:16 | Deraniyagala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.131 |  |
| 2026-05-22 15:18:07 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.177 |  |
| 2026-05-22 15:02:58 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)