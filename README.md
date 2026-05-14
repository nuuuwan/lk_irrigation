# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_00:28:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,023 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 00:28:28 | Dunamale (Aththanagalu Oya) | 4.48 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 00:28:16 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-15 00:22:27 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-15 00:11:44 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | -0.018 |  |
| 2026-05-15 00:10:06 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:08:46 | Hanwella (Kelani Ganga) | 5.48 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-05-15 00:08:45 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:08:17 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-15 00:08:07 | Holombuwa (Kelani Ganga) | 1.62 | 🟢 Normal | -0.040 |  |
| 2026-05-15 00:07:45 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-15 00:07:18 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-05-15 00:06:56 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-15 00:06:13 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-05-15 00:05:52 | Moragaswewa (Deduru Oya) | 1.66 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-15 00:05:18 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.021 |  |
| 2026-05-15 00:04:49 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:04:40 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-15 00:04:38 | Rathnapura (Kalu Ganga) | 4.89 | 🟢 Normal | -0.030 |  |
| 2026-05-15 00:04:19 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.169 |  |
| 2026-05-15 00:03:50 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:03:46 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.036 |  |
| 2026-05-15 00:03:33 | Deraniyagala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.131 |  |
| 2026-05-15 00:03:30 | Giriulla (Maha Oya) | 3.88 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-15 00:03:28 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 00:03:15 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-15 00:03:05 | Glencourse (Kelani Ganga) | 14.19 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-15 00:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 00:02:50 | Dunamale (Aththanagalu Oya) | 4.48 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 00:02:19 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-15 00:02:12 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:48 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:28 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:26 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:18 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:00:56 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:00:38 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 00:28:28 | Dunamale (Aththanagalu Oya) | 4.48 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 00:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 00:11:44 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | -0.018 |  |
| 2026-05-15 00:07:18 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-05-15 00:08:46 | Hanwella (Kelani Ganga) | 5.48 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-05-15 00:06:56 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-15 00:04:40 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-15 00:03:05 | Glencourse (Kelani Ganga) | 14.19 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-15 00:05:52 | Moragaswewa (Deduru Oya) | 1.66 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-15 00:08:17 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-15 00:02:19 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-15 00:03:30 | Giriulla (Maha Oya) | 3.88 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-15 00:03:28 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 00:28:16 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-15 00:03:15 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-15 00:22:27 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-15 00:07:45 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:48 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:08:45 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:28 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:02:12 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:00:56 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:04:49 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:10:06 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:03:50 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:18 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:03:46 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:05:18 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.021 |  |
| 2026-05-15 00:06:13 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-05-14 23:01:54 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-05-15 00:04:38 | Rathnapura (Kalu Ganga) | 4.89 | 🟢 Normal | -0.030 |  |
| 2026-05-15 00:00:38 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-05-15 00:03:44 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.036 |  |
| 2026-05-15 00:08:07 | Holombuwa (Kelani Ganga) | 1.62 | 🟢 Normal | -0.040 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-15 00:03:33 | Deraniyagala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.131 |  |
| 2026-05-15 00:04:19 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)