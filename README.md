# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_06:34:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,459 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 06:34:17 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.001 |  |
| 2026-05-30 06:22:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.58 | 🟠 Minor Flood | -0.018 |  |
| 2026-05-30 06:16:36 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:13:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.068 |  |
| 2026-05-30 06:08:02 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-05-30 06:07:52 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.040 |  |
| 2026-05-30 06:06:28 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.213 |  |
| 2026-05-30 06:06:28 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:05:49 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.057 |  |
| 2026-05-30 06:05:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:05:11 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:05:08 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-30 06:04:56 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-05-30 06:04:25 | Magura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.103 |  |
| 2026-05-30 06:04:23 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:04:09 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | -0.048 |  |
| 2026-05-30 06:04:04 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.033 |  |
| 2026-05-30 06:04:04 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.087 |  |
| 2026-05-30 06:03:58 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-05-30 06:03:09 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:02:54 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:02:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:02:45 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-05-30 06:02:45 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-05-30 06:02:08 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.030 |  |
| 2026-05-30 06:01:55 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-30 06:01:54 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.115 |  |
| 2026-05-30 06:01:50 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:01:50 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:01:33 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.097 |  |
| 2026-05-30 06:01:18 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:01:08 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-30 06:00:40 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-30 06:00:37 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 06:00:37 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 06:00:37 | Ellagawa (Kalu Ganga) | 8.14 | 🟢 Normal | -0.066 |  |
| 2026-05-30 06:00:31 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:00:05 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 06:22:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.58 | 🟠 Minor Flood | -0.018 |  |
| 2026-05-30 06:00:37 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 06:00:40 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-30 06:00:37 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 05:17:38 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-30 06:04:23 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:01:50 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:01:50 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:02:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:00:05 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:00:31 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:02:54 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:05:13 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:03:09 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:16:36 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:01:18 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:06:28 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 06:34:17 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.001 |  |
| 2026-05-30 06:08:02 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-05-30 06:05:08 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-30 06:01:55 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-30 06:01:08 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-30 06:04:56 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-05-30 06:02:45 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-05-30 06:02:45 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-05-30 06:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-05-30 06:02:08 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.030 |  |
| 2026-05-30 06:04:04 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.033 |  |
| 2026-05-30 06:07:52 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.040 |  |
| 2026-05-30 06:04:09 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | -0.048 |  |
| 2026-05-30 06:05:49 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.057 |  |
| 2026-05-30 06:00:37 | Ellagawa (Kalu Ganga) | 8.14 | 🟢 Normal | -0.066 |  |
| 2026-05-30 06:13:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.068 |  |
| 2026-05-30 06:04:04 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.087 |  |
| 2026-05-30 06:01:33 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | -0.097 |  |
| 2026-05-30 06:04:25 | Magura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.103 |  |
| 2026-05-30 06:01:54 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.115 |  |
| 2026-05-30 06:06:28 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)