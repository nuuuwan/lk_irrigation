# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_02:36:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,394 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 02:36:15 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.007 |  |
| 2026-06-08 02:21:16 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | -0.103 |  |
| 2026-06-08 02:17:28 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:10:53 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.035 |  |
| 2026-06-08 02:07:05 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-08 02:06:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:06:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:06:01 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:05:50 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.030 |  |
| 2026-06-08 02:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-06-08 02:05:28 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:04:58 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-06-08 02:03:57 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-08 02:03:57 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:03:43 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.103 |  |
| 2026-06-08 02:03:28 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:03:17 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:03:08 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:02:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.069 |  |
| 2026-06-08 02:02:36 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 02:02:35 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-06-08 02:02:18 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 02:02:13 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.040 |  |
| 2026-06-08 02:02:10 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-06-08 02:02:05 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:02:02 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.010 |  |
| 2026-06-08 02:01:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:01:35 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:01:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:00:13 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.117 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 02:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-06-08 02:07:05 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-08 02:02:36 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 02:02:18 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 01:31:17 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-08 02:03:57 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-08 02:03:28 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:05:44 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:01:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:17:28 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:03:08 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:01:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:06:01 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:05:28 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:03:17 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:06:42 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:02:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:00:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:03:57 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:01:35 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:06:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:02:05 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:13:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:15:25 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:36:15 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.007 |  |
| 2026-06-08 02:02:02 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.010 |  |
| 2026-06-08 02:04:58 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:04:47 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-08 02:02:10 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-06-08 02:05:50 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.030 |  |
| 2026-06-08 02:02:35 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-06-08 02:10:53 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.035 |  |
| 2026-06-08 02:02:13 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.040 |  |
| 2026-06-08 02:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.069 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-08 02:21:16 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | -0.103 |  |
| 2026-06-08 02:00:13 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)