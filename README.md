# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_06:30:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,380 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 06:30:53 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:10:44 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-23 06:10:33 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-23 06:10:06 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.112 |  |
| 2026-05-23 06:09:08 | Hanwella (Kelani Ganga) | 7.27 | 🟡 Alert | -0.099 |  |
| 2026-05-23 06:07:55 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.009 |  |
| 2026-05-23 06:07:19 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:07:15 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:06:14 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | -0.066 |  |
| 2026-05-23 06:06:05 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:06:05 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | 0.000 |  |
| 2026-05-23 06:05:59 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.029 |  |
| 2026-05-23 06:05:58 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-23 06:05:50 | Rathnapura (Kalu Ganga) | 6.43 | 🟡 Alert | -0.088 |  |
| 2026-05-23 06:05:44 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-23 06:05:16 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.030 |  |
| 2026-05-23 06:05:07 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:05:05 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.022 |  |
| 2026-05-23 06:04:50 | Ellagawa (Kalu Ganga) | 9.97 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-23 06:04:43 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-23 06:03:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.159 | 🔺 Rising |
| 2026-05-23 06:03:34 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:03:32 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.036 |  |
| 2026-05-23 06:03:24 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | -0.062 |  |
| 2026-05-23 06:03:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:03:19 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:03:04 | Deraniyagala (Kelani Ganga) | 2.30 | 🟢 Normal | -0.152 |  |
| 2026-05-23 06:02:55 | Glencourse (Kelani Ganga) | 12.55 | 🟢 Normal | -0.195 |  |
| 2026-05-23 06:02:55 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-23 06:02:32 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.017 |  |
| 2026-05-23 06:02:07 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.039 |  |
| 2026-05-23 06:01:53 | Dunamale (Aththanagalu Oya) | 5.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 06:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:01:43 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:01:42 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-23 06:00:59 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 06:01:53 | Dunamale (Aththanagalu Oya) | 5.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 06:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.159 | 🔺 Rising |
| 2026-05-23 06:06:05 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | 0.000 |  |
| 2026-05-23 06:03:24 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | -0.062 |  |
| 2026-05-23 06:05:50 | Rathnapura (Kalu Ganga) | 6.43 | 🟡 Alert | -0.088 |  |
| 2026-05-23 06:09:08 | Hanwella (Kelani Ganga) | 7.27 | 🟡 Alert | -0.099 |  |
| 2026-05-23 06:10:33 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-23 06:04:50 | Ellagawa (Kalu Ganga) | 9.97 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-23 06:02:55 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-23 06:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-23 06:05:44 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-23 06:10:44 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-23 06:07:15 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:01:42 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:01:43 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:03:19 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:30:53 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:07:19 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:03:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:05:07 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:03:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:03:34 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:06:05 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 06:07:55 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.009 |  |
| 2026-05-23 06:04:43 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-23 06:05:58 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-23 06:02:32 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.017 |  |
| 2026-05-23 06:00:59 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-05-23 06:05:05 | Baddegama (Gin Ganga) | 2.61 | 🟢 Normal | -0.022 |  |
| 2026-05-23 06:05:59 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.029 |  |
| 2026-05-23 06:05:16 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.030 |  |
| 2026-05-23 06:03:32 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.036 |  |
| 2026-05-23 06:02:07 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.039 |  |
| 2026-05-23 06:06:14 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | -0.066 |  |
| 2026-05-23 06:10:06 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.112 |  |
| 2026-05-23 06:03:04 | Deraniyagala (Kelani Ganga) | 2.30 | 🟢 Normal | -0.152 |  |
| 2026-05-23 06:02:55 | Glencourse (Kelani Ganga) | 12.55 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)