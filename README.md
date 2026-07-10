# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_13:17:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,443 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 13:17:44 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:13:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:12:16 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:11:59 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:11:50 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:10:07 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:09:40 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-07-10 13:08:48 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-10 13:08:31 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-10 13:08:27 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:08:11 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.036 |  |
| 2026-07-10 13:05:35 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:05:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:05:31 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:04:04 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-10 13:04:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:41 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:32 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-10 13:03:32 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:30 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.041 |  |
| 2026-07-10 13:03:20 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:18 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 13:03:15 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:10 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:07 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:06 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:02:30 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:02:06 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:01:59 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-07-10 13:01:53 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:01:43 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:01:42 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-07-10 13:00:58 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:46 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-10 13:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-10 13:00:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:11 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:11 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:07 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 13:01:42 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-07-10 13:01:59 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-07-10 13:04:04 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-10 13:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-07-10 13:08:48 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-10 13:08:31 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-07-10 13:03:18 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 13:00:11 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:11 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:20 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:10 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:02:06 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:07 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:58 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:11:59 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:12:16 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:15 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:04:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:01:53 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:17:44 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:11:50 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:02:30 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:10:07 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:32 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:05:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:08:27 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:05:35 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:00:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:41 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:01:43 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:05:31 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:13:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-07-10 13:03:32 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-10 13:00:46 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-10 13:09:40 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-07-10 13:08:11 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.036 |  |
| 2026-07-10 13:03:30 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.041 |  |
| 2026-07-10 13:00:07 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)