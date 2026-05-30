# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_05:19:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,420 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 05:19:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.080 |  |
| 2026-05-30 05:18:32 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | -0.060 |  |
| 2026-05-30 05:17:38 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-30 05:13:46 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | -0.025 |  |
| 2026-05-30 05:11:59 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.077 |  |
| 2026-05-30 05:10:14 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-05-30 05:07:25 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-05-30 05:07:24 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-05-30 05:06:35 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:06:08 | Magura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.039 |  |
| 2026-05-30 05:06:07 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:05:52 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:05:24 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:05:20 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:04:37 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-05-30 05:04:25 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.066 |  |
| 2026-05-30 05:04:22 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-30 05:03:56 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:03:39 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:03:24 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-30 05:02:53 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:48 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-30 05:02:41 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:28 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:23 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 05:02:20 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:09 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.108 |  |
| 2026-05-30 05:02:09 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:01:49 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.011 |  |
| 2026-05-30 05:01:43 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-30 05:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:01:17 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 05:01:12 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-05-30 05:01:04 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:00:59 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 03:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-30 05:07:25 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-05-30 05:00:59 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-30 05:02:23 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 05:01:17 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 05:17:38 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-30 05:03:56 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:01:04 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:03:39 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:00:08 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:05:24 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:53 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:20 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:05:52 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:08:42 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:06:07 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:06:35 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:09 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:28 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:05:20 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 05:02:48 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-30 05:04:22 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-30 05:01:43 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-30 05:04:37 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-05-30 05:01:12 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-05-30 05:01:49 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.011 |  |
| 2026-05-30 05:10:14 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-05-30 05:03:24 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-05-30 05:13:46 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | -0.025 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-30 05:06:08 | Magura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.039 |  |
| 2026-05-30 05:18:32 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | -0.060 |  |
| 2026-05-30 05:04:25 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.066 |  |
| 2026-05-30 05:11:59 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.077 |  |
| 2026-05-30 05:19:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.080 |  |
| 2026-05-30 05:02:09 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)