# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_14:13:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 14:13:26 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.026 |  |
| 2025-12-19 14:13:05 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:12:17 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.009 |  |
| 2025-12-19 14:10:07 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:09:55 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 14:09:21 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:09:17 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2025-12-19 14:07:13 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-19 14:07:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-19 14:06:53 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:05:38 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-19 14:05:03 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2025-12-19 14:04:46 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.823 | 🔺 Rising |
| 2025-12-19 14:04:36 | Thanthirimale (Malwathu Oya) | 5.38 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2025-12-19 14:04:33 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2025-12-19 14:04:21 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -581.760 |  |
| 2025-12-19 14:04:21 | Manampitiya (Mahaweli Ganga) | 4.61 | 🟠 Minor Flood | -0.050 |  |
| 2025-12-19 14:04:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-19 14:03:56 | Katharagama (Menik Ganga) | 4.20 | 🟡 Alert | -581.760 |  |
| 2025-12-19 14:03:50 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:03:43 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-19 14:03:13 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:54 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.050 |  |
| 2025-12-19 14:02:49 | Weraganthota (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-19 14:02:39 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:02:36 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:35 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:21 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | -0.013 |  |
| 2025-12-19 14:02:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:10 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:10 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:08 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.020 |  |
| 2025-12-19 14:02:00 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:01:51 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.823 | 🔺 Rising |
| 2025-12-19 14:01:47 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:01:13 | Horowpothana (Yan Oya) | 6.25 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2025-12-19 14:00:46 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:00:28 | Padiyathalawa (Maduru Oya) | 2.80 | 🟢 Normal | -0.163 |  |
| 2025-12-19 14:00:11 | Nakkala (Kumbukkan Oya) | 1.62 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 14:04:21 | Manampitiya (Mahaweli Ganga) | 4.61 | 🟠 Minor Flood | -0.050 |  |
| 2025-12-19 14:04:36 | Thanthirimale (Malwathu Oya) | 5.38 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2025-12-19 14:01:13 | Horowpothana (Yan Oya) | 6.25 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2025-12-19 14:04:46 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.823 | 🔺 Rising |
| 2025-12-19 14:02:49 | Weraganthota (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-19 14:04:33 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2025-12-19 14:04:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-19 14:07:13 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-19 14:05:38 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-19 14:03:43 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-19 14:09:55 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 14:07:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-19 14:02:10 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:01:47 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:10:07 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 13:03:33 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:36 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:35 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:10 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:02:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:00:46 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:03:50 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:13:05 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:03:13 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:09:17 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2025-12-19 14:12:17 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.009 |  |
| 2025-12-19 14:06:53 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:02:39 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:09:21 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:02:00 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-19 13:05:02 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:05:03 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2025-12-19 14:02:21 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | -0.013 |  |
| 2025-12-19 14:02:08 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.020 |  |
| 2025-12-19 14:13:26 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.026 |  |
| 2025-12-19 14:00:11 | Nakkala (Kumbukkan Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2025-12-19 14:02:54 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.050 |  |
| 2025-12-19 14:00:28 | Padiyathalawa (Maduru Oya) | 2.80 | 🟢 Normal | -0.163 |  |
| 2025-12-19 14:04:21 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -581.760 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)