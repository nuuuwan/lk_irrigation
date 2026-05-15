# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_19:24:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,756 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 19:24:17 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-05-15 19:23:37 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-05-15 19:16:06 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.024 |  |
| 2026-05-15 19:10:36 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:09:45 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-15 19:09:01 | Rathnapura (Kalu Ganga) | 4.25 | 🟢 Normal | -0.036 |  |
| 2026-05-15 19:07:49 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.042 |  |
| 2026-05-15 19:07:27 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.066 |  |
| 2026-05-15 19:07:17 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 19:06:17 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.019 |  |
| 2026-05-15 19:05:56 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | -0.113 |  |
| 2026-05-15 19:05:44 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-05-15 19:05:04 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-15 19:04:56 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 19:04:41 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.100 |  |
| 2026-05-15 19:04:40 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:04:04 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.193 |  |
| 2026-05-15 19:03:44 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:03:12 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:02:58 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-15 19:02:56 | Moragaswewa (Deduru Oya) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:02:48 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:02:31 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-15 19:02:28 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 19:02:22 | Dunamale (Aththanagalu Oya) | 4.68 | 🟠 Minor Flood | -0.040 |  |
| 2026-05-15 19:02:21 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:02:20 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:01:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-05-15 19:01:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-15 19:01:49 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.031 |  |
| 2026-05-15 19:01:48 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-15 19:01:38 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-15 19:01:00 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | -0.043 |  |
| 2026-05-15 19:00:43 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-15 19:00:34 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 19:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 19:02:22 | Dunamale (Aththanagalu Oya) | 4.68 | 🟠 Minor Flood | -0.040 |  |
| 2026-05-15 19:01:00 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | -0.043 |  |
| 2026-05-15 19:24:17 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-05-15 19:02:31 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-15 19:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-15 19:00:43 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-15 19:05:04 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-15 19:01:48 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-15 19:04:56 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 19:02:28 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:02:56 | Moragaswewa (Deduru Oya) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:03:12 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:04:40 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:02:20 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:03:44 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:10:36 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:01:38 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:07:17 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:00:34 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:02:21 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:02:48 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-15 19:01:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-15 19:05:44 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-05-15 19:09:45 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-15 19:06:17 | Giriulla (Maha Oya) | 2.90 | 🟢 Normal | -0.019 |  |
| 2026-05-15 19:01:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-05-15 19:02:58 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-15 19:16:06 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.024 |  |
| 2026-05-15 19:01:49 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.031 |  |
| 2026-05-15 19:09:01 | Rathnapura (Kalu Ganga) | 4.25 | 🟢 Normal | -0.036 |  |
| 2026-05-15 19:07:49 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.042 |  |
| 2026-05-15 19:07:27 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.066 |  |
| 2026-05-15 19:04:41 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.100 |  |
| 2026-05-15 19:05:56 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | -0.113 |  |
| 2026-05-15 19:04:04 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)