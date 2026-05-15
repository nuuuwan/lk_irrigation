# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_00:14:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,939 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 00:14:10 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:13:43 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:12:30 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.046 |  |
| 2026-05-16 00:11:30 | Moragaswewa (Deduru Oya) | 3.95 | 🟢 Normal | 14.810 | 🔺 Rising |
| 2026-05-16 00:09:39 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.028 |  |
| 2026-05-16 00:09:00 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | -0.021 |  |
| 2026-05-16 00:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-16 00:08:19 | Hanwella (Kelani Ganga) | 4.44 | 🟢 Normal | -0.097 |  |
| 2026-05-16 00:06:50 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:06:50 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-16 00:05:54 | Magura (Kalu Ganga) | 4.07 | 🟡 Alert | -0.028 |  |
| 2026-05-16 00:05:47 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.047 |  |
| 2026-05-16 00:05:45 | Horowpothana (Yan Oya) | 2.93 | 🟢 Normal | -0.019 |  |
| 2026-05-16 00:05:40 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.038 |  |
| 2026-05-16 00:05:39 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.010 |  |
| 2026-05-16 00:05:39 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:05:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:04:50 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:04:37 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:04:36 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:04:25 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-16 00:04:05 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.180 |  |
| 2026-05-16 00:03:44 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:43 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:39 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-05-16 00:03:36 | Moragaswewa (Deduru Oya) | 2.00 | 🟢 Normal | 14.810 | 🔺 Rising |
| 2026-05-16 00:03:29 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:03 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:02 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:02:26 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | -0.010 |  |
| 2026-05-16 00:02:21 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:02:16 | Dunamale (Aththanagalu Oya) | 4.58 | 🟠 Minor Flood | -0.235 |  |
| 2026-05-16 00:01:48 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-16 00:01:30 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:01:25 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-05-16 00:01:15 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:01:11 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.061 |  |
| 2026-05-16 00:01:05 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-16 00:01:04 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.012 |  |
| 2026-05-15 23:57:09 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | -0.235 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 00:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-16 00:02:16 | Dunamale (Aththanagalu Oya) | 4.58 | 🟠 Minor Flood | -0.235 |  |
| 2026-05-16 00:05:54 | Magura (Kalu Ganga) | 4.07 | 🟡 Alert | -0.028 |  |
| 2026-05-16 00:11:30 | Moragaswewa (Deduru Oya) | 3.95 | 🟢 Normal | 14.810 | 🔺 Rising |
| 2026-05-16 00:01:48 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 00:01:05 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:02 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:43 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:04:50 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:44 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:29 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:01:15 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:05:10 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:04:37 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:02:21 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:05:39 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:03:03 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:14:10 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:06:50 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:01:30 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-16 00:02:26 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | -0.010 |  |
| 2026-05-16 00:05:39 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.010 |  |
| 2026-05-16 00:04:25 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-16 00:01:04 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.012 |  |
| 2026-05-16 00:05:45 | Horowpothana (Yan Oya) | 2.93 | 🟢 Normal | -0.019 |  |
| 2026-05-16 00:03:39 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-05-16 00:06:50 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-16 00:09:00 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | -0.021 |  |
| 2026-05-16 00:09:39 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.028 |  |
| 2026-05-16 00:05:40 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.038 |  |
| 2026-05-16 00:12:30 | Rathnapura (Kalu Ganga) | 4.02 | 🟢 Normal | -0.046 |  |
| 2026-05-16 00:05:47 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.047 |  |
| 2026-05-16 00:01:25 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-05-16 00:01:11 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.061 |  |
| 2026-05-16 00:08:19 | Hanwella (Kelani Ganga) | 4.44 | 🟢 Normal | -0.097 |  |
| 2026-05-16 00:04:05 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)