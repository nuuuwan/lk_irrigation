# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_00:26:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,684 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 00:26:27 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:26:05 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:25:49 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:25:26 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:14:54 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-14 00:14:18 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-14 00:09:45 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.009 |  |
| 2026-06-14 00:09:08 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:08:24 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:07:32 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:06:32 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-06-14 00:06:30 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.038 |  |
| 2026-06-14 00:05:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-14 00:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.011 |  |
| 2026-06-14 00:05:50 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.010 |  |
| 2026-06-14 00:05:26 | Rathnapura (Kalu Ganga) | 4.51 | 🟢 Normal | -0.088 |  |
| 2026-06-14 00:04:54 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.067 |  |
| 2026-06-14 00:04:44 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-06-14 00:04:40 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.041 |  |
| 2026-06-14 00:03:37 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-14 00:03:26 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.078 |  |
| 2026-06-14 00:03:09 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:03:04 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.036 |  |
| 2026-06-14 00:03:00 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-06-14 00:02:36 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-06-14 00:02:26 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:02:23 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.031 |  |
| 2026-06-14 00:02:20 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 00:02:01 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:27 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:07 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:00:48 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-14 00:00:33 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:00:21 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 00:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.011 |  |
| 2026-06-14 00:05:54 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-14 00:03:37 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-14 00:00:48 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-14 00:02:20 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-14 00:14:54 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-06-14 00:14:18 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-14 00:09:08 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:04:40 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:00:33 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:03:09 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:07 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:26:05 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:52 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:26:27 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:25:26 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:01:27 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-14 00:02:26 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-13 23:31:18 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.007 |  |
| 2026-06-14 00:09:45 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.009 |  |
| 2026-06-13 21:03:19 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-14 00:05:50 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | -0.010 |  |
| 2026-06-14 00:02:36 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-06-14 00:03:00 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-06-14 00:04:44 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-14 00:02:23 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.031 |  |
| 2026-06-13 23:04:30 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.032 |  |
| 2026-06-14 00:03:04 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.036 |  |
| 2026-06-14 00:06:30 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.038 |  |
| 2026-06-14 00:06:32 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-14 00:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.041 |  |
| 2026-06-14 00:04:54 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.067 |  |
| 2026-06-14 00:03:26 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.078 |  |
| 2026-06-14 00:05:26 | Rathnapura (Kalu Ganga) | 4.51 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)