# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_06:08:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,809 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 06:08:33 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 06:08:16 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:07:52 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.046 |  |
| 2025-12-20 06:07:07 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:06:57 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2025-12-20 06:06:41 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.009 |  |
| 2025-12-20 06:05:20 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.019 |  |
| 2025-12-20 06:05:17 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.062 |  |
| 2025-12-20 06:05:10 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-20 06:05:09 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2025-12-20 06:05:01 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:04:45 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:04:31 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 06:04:22 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:04:19 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:03:56 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-20 06:02:49 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:02:48 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-20 06:02:30 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:02:20 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:02:07 | Horowpothana (Yan Oya) | 6.35 | 🟡 Alert | -0.010 |  |
| 2025-12-20 06:01:35 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-20 06:01:17 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-20 06:01:14 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -18.000 |  |
| 2025-12-20 06:01:12 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -18.000 |  |
| 2025-12-20 06:01:10 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-20 06:01:01 | Manampitiya (Mahaweli Ganga) | 4.20 | 🟡 Alert | 0.000 |  |
| 2025-12-20 06:00:49 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:00:44 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 06:00:37 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.065 |  |
| 2025-12-20 06:00:14 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:28:59 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 05:28:58 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 05:21:45 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:16:48 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.062 |  |
| 2025-12-20 05:13:35 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2025-12-20 05:13:20 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:13:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:12:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-20 06:01:01 | Manampitiya (Mahaweli Ganga) | 4.20 | 🟡 Alert | 0.000 |  |
| 2025-12-20 06:02:07 | Horowpothana (Yan Oya) | 6.35 | 🟡 Alert | -0.010 |  |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-20 06:03:56 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-20 06:05:10 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-20 06:08:33 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 06:04:31 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 06:00:44 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 06:00:14 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:02:49 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:04:22 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:04:45 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:05:01 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:08:16 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:00:49 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:04:19 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:02:30 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:08:24 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 05:21:45 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:07:07 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:02:20 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 06:06:41 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | -0.009 |  |
| 2025-12-20 06:01:10 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-20 06:02:48 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-20 06:01:35 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-20 06:05:09 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2025-12-20 06:01:17 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-20 06:06:57 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2025-12-20 06:05:20 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.019 |  |
| 2025-12-20 06:07:52 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.046 |  |
| 2025-12-20 03:07:24 | Padiyathalawa (Maduru Oya) | 1.52 | 🟢 Normal | -0.049 |  |
| 2025-12-20 06:05:17 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.062 |  |
| 2025-12-20 06:00:37 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.065 |  |
| 2025-12-20 05:12:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.080 |  |
| 2025-12-20 04:06:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.112 |  |
| 2025-12-20 06:01:14 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)