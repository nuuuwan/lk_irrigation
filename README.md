# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_15:07:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,271 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 15:07:11 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:07:06 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:07:03 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2025-12-19 15:07:02 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 15:07:00 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-19 15:06:14 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2025-12-19 15:05:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:05:32 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:05:21 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:05:00 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-19 15:04:00 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-19 15:03:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:03:14 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:03:11 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-19 15:03:05 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:03:04 | Weraganthota (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-19 15:03:02 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.011 |  |
| 2025-12-19 15:02:38 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2025-12-19 15:02:32 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:31 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:29 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:26 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.229 |  |
| 2025-12-19 15:02:06 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:05 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:01:55 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-19 15:01:53 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:01:48 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2025-12-19 15:01:38 | Manampitiya (Mahaweli Ganga) | 4.54 | 🟠 Minor Flood | -0.073 |  |
| 2025-12-19 15:01:23 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 15:01:19 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2025-12-19 15:01:18 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.035 |  |
| 2025-12-19 15:00:51 | Horowpothana (Yan Oya) | 6.26 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2025-12-19 15:00:43 | Nakkala (Kumbukkan Oya) | 1.59 | 🟢 Normal | -0.030 |  |
| 2025-12-19 15:00:29 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:13:26 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:13:05 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:12:17 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:10:07 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:09:55 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.035 |  |
| 2025-12-19 14:09:21 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:09:17 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 15:01:38 | Manampitiya (Mahaweli Ganga) | 4.54 | 🟠 Minor Flood | -0.073 |  |
| 2025-12-19 15:01:48 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2025-12-19 15:00:51 | Horowpothana (Yan Oya) | 6.26 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2025-12-19 15:06:14 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2025-12-19 15:03:11 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-19 15:03:04 | Weraganthota (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-19 15:04:00 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-19 15:07:02 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 15:01:23 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 15:02:05 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:01:53 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:31 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:07:11 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:32 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:03:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:03:05 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:06 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:05:21 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:05:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:00:29 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:03:50 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:02:29 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:05:32 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-19 14:13:05 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:03:14 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:07:06 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 15:07:00 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2025-12-19 15:05:00 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-19 15:01:55 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-19 15:01:19 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2025-12-19 14:02:00 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-19 15:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.011 |  |
| 2025-12-19 15:07:03 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2025-12-19 15:00:43 | Nakkala (Kumbukkan Oya) | 1.59 | 🟢 Normal | -0.030 |  |
| 2025-12-19 15:02:38 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2025-12-19 15:01:18 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.035 |  |
| 2025-12-19 14:00:28 | Padiyathalawa (Maduru Oya) | 2.80 | 🟢 Normal | -0.163 |  |
| 2025-12-19 15:02:26 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)