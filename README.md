# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_06:32:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,152 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 06:32:19 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.010 |  |
| 2026-05-16 06:31:18 | Galgamuwa (Mee Oya) | 3.70 | 🟢 Normal | -0.026 |  |
| 2026-05-16 06:28:19 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:08:49 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.056 |  |
| 2026-05-16 06:08:40 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.041 |  |
| 2026-05-16 06:08:18 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.009 |  |
| 2026-05-16 06:08:10 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-05-16 06:08:02 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-16 06:07:55 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -36.000 |  |
| 2026-05-16 06:07:54 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -36.000 |  |
| 2026-05-16 06:07:34 | Baddegama (Gin Ganga) | 3.02 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:07:26 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-16 06:06:14 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.066 |  |
| 2026-05-16 06:06:09 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.009 |  |
| 2026-05-16 06:05:52 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:05:36 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.037 |  |
| 2026-05-16 06:05:17 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | -0.070 |  |
| 2026-05-16 06:04:50 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:04:24 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.074 |  |
| 2026-05-16 06:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 06:03:51 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 06:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 06:03:12 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | -0.040 |  |
| 2026-05-16 06:03:10 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.030 |  |
| 2026-05-16 06:02:58 | Dunamale (Aththanagalu Oya) | 4.45 | 🟠 Minor Flood | -0.030 |  |
| 2026-05-16 06:02:57 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:02:52 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:02:29 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.195 |  |
| 2026-05-16 06:02:15 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-16 06:02:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 06:02:01 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:01:39 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-05-16 06:01:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-16 06:01:23 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:01:14 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:00:39 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-16 06:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.058 |  |
| 2026-05-16 06:00:23 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:00:21 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-05-16 06:00:21 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-16 06:00:13 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.052 |  |
| 2026-05-16 05:55:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.11 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 06:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 06:02:58 | Dunamale (Aththanagalu Oya) | 4.45 | 🟠 Minor Flood | -0.030 |  |
| 2026-05-16 06:08:02 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-16 06:01:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-16 06:03:51 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-16 06:00:21 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-16 06:02:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 06:01:23 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:28:19 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:00:23 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:04:50 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:01:14 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-16 06:08:10 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-05-16 06:08:18 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.009 |  |
| 2026-05-16 06:06:09 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.009 |  |
| 2026-05-16 06:07:26 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-16 06:02:15 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-16 06:00:39 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-16 06:32:19 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.010 |  |
| 2026-05-16 06:01:39 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-05-16 06:00:21 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-05-16 06:02:01 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:02:52 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:02:57 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:07:34 | Baddegama (Gin Ganga) | 3.02 | 🟢 Normal | -0.020 |  |
| 2026-05-16 06:31:18 | Galgamuwa (Mee Oya) | 3.70 | 🟢 Normal | -0.026 |  |
| 2026-05-16 06:03:10 | Badalgama (Maha Oya) | 3.73 | 🟢 Normal | -0.030 |  |
| 2026-05-16 06:05:36 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.037 |  |
| 2026-05-16 06:03:12 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | -0.040 |  |
| 2026-05-16 06:08:40 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.041 |  |
| 2026-05-16 06:00:13 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.052 |  |
| 2026-05-16 06:08:49 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.056 |  |
| 2026-05-16 06:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.058 |  |
| 2026-05-16 06:06:14 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.066 |  |
| 2026-05-16 06:05:17 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | -0.070 |  |
| 2026-05-16 06:04:24 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.074 |  |
| 2026-05-16 06:02:29 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.195 |  |
| 2026-05-16 06:07:55 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)