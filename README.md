# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_14:23:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **212,291 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 14:23:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:21:56 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.040 |  |
| 2026-07-21 14:17:45 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-21 14:17:41 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.008 |  |
| 2026-07-21 14:13:49 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:10:03 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-21 14:09:27 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.066 |  |
| 2026-07-21 14:08:23 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:07:49 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:07:00 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-21 14:06:53 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-07-21 14:06:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:06:37 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:05:40 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:05:19 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:05:06 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:05:02 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-07-21 14:04:42 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.116 |  |
| 2026-07-21 14:04:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-21 14:03:24 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:03:20 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-07-21 14:02:56 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-21 14:02:51 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:48 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:46 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-21 14:02:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:24 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:18 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:18 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:05 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:02 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:01:46 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:01:39 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:01:11 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-21 14:00:51 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:00:41 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-21 14:00:37 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:00:06 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 14:06:53 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-07-21 14:02:46 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-21 14:02:56 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-21 14:10:03 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-21 14:01:11 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-21 14:04:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-21 14:17:45 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-21 14:00:41 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-21 14:08:23 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:03:24 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:01:39 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:48 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:24 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:05:19 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:51 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:00:06 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:06:37 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:00:37 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:05:06 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:05 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:18 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:06:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:05:40 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:07:49 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:00:51 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:18 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:13:49 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:02:02 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:01:46 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:23:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-21 14:17:41 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.008 |  |
| 2026-07-21 14:07:00 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-07-21 14:05:02 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-07-21 14:03:20 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-07-21 14:21:56 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.040 |  |
| 2026-07-21 14:09:27 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.066 |  |
| 2026-07-21 14:04:42 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)