# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_10:19:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,079 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 10:19:47 | Weraganthota (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.937 | 🔺 Rising |
| 2025-12-19 10:18:23 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:12:49 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2025-12-19 10:11:15 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:11:07 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:10:41 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-19 10:08:47 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.049 |  |
| 2025-12-19 10:07:17 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2025-12-19 10:06:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:06:56 | Thanthirimale (Malwathu Oya) | 5.36 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2025-12-19 10:06:51 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2025-12-19 10:06:41 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-19 10:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.056 |  |
| 2025-12-19 10:06:16 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:04:58 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:04:22 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-19 10:04:17 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2025-12-19 10:04:07 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.048 |  |
| 2025-12-19 10:04:04 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:03:48 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | -0.021 |  |
| 2025-12-19 10:03:33 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.083 |  |
| 2025-12-19 10:03:24 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2025-12-19 10:03:23 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2025-12-19 10:03:22 | Manampitiya (Mahaweli Ganga) | 4.77 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-19 10:03:08 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.010 |  |
| 2025-12-19 10:03:06 | Padiyathalawa (Maduru Oya) | 1.99 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-19 10:03:04 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2025-12-19 10:03:03 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-19 10:03:03 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2025-12-19 10:02:51 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2025-12-19 10:02:43 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.540 |  |
| 2025-12-19 10:02:23 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:02:20 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-19 10:01:56 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 10:01:30 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:01:26 | Horowpothana (Yan Oya) | 6.11 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2025-12-19 10:01:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:00:31 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | -0.031 |  |
| 2025-12-19 10:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 10:03:22 | Manampitiya (Mahaweli Ganga) | 4.77 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-19 10:01:26 | Horowpothana (Yan Oya) | 6.11 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2025-12-19 10:06:56 | Thanthirimale (Malwathu Oya) | 5.36 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2025-12-19 10:19:47 | Weraganthota (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.937 | 🔺 Rising |
| 2025-12-19 10:03:06 | Padiyathalawa (Maduru Oya) | 1.99 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-19 10:04:22 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-19 10:03:03 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-19 10:01:56 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 10:10:41 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-19 10:01:30 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:11:07 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:06:16 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:18:23 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:06:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:01:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:04:04 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:04:58 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:11:15 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:02:23 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:06:51 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2025-12-19 10:12:49 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2025-12-19 10:06:41 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-19 10:03:08 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.010 |  |
| 2025-12-19 10:07:17 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2025-12-19 10:02:20 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-19 10:03:23 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2025-12-19 10:02:51 | Siyambalanduwa (Heda Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2025-12-19 10:04:17 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2025-12-19 10:03:48 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | -0.021 |  |
| 2025-12-19 10:03:03 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2025-12-19 10:00:31 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | -0.031 |  |
| 2025-12-19 10:03:24 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2025-12-19 10:03:04 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2025-12-19 10:04:07 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.048 |  |
| 2025-12-19 10:08:47 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.049 |  |
| 2025-12-19 10:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.056 |  |
| 2025-12-19 10:03:33 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.083 |  |
| 2025-12-19 10:02:43 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.540 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)