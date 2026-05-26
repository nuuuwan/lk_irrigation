# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_01:10:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,592 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 01:10:55 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | -0.032 |  |
| 2026-05-27 01:08:21 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:07:17 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:06:33 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:06:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2026-05-27 01:06:01 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-27 01:05:46 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:05:43 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.058 |  |
| 2026-05-27 01:05:13 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.030 |  |
| 2026-05-27 01:04:27 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:04:19 | Ellagawa (Kalu Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:04:01 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.078 |  |
| 2026-05-27 01:03:57 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.054 |  |
| 2026-05-27 01:03:45 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:03:36 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-05-27 01:03:31 | Hanwella (Kelani Ganga) | 4.40 | 🟢 Normal | -0.052 |  |
| 2026-05-27 01:03:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:03:26 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:03:16 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:03:13 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:02:49 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 01:02:47 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:02:32 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.091 |  |
| 2026-05-27 01:02:24 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.040 |  |
| 2026-05-27 01:02:11 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:01:25 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:01:20 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-05-27 01:00:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 22:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 01:01:20 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-05-27 00:09:21 | Magura (Kalu Ganga) | 3.00 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-27 01:02:49 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-27 01:06:01 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 01:06:33 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:00:52 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:03:16 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:03:26 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:01:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:07:17 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:01:25 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:03:26 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:02:47 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:05:46 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:06:11 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 00:09:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:04:27 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 01:02:11 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-26 23:28:37 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.007 |  |
| 2026-05-27 01:08:21 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:03:13 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:03:45 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:04:19 | Ellagawa (Kalu Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-05-27 01:03:36 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-27 01:05:13 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.030 |  |
| 2026-05-27 01:10:55 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | -0.032 |  |
| 2026-05-27 01:02:24 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.040 |  |
| 2026-05-27 01:03:31 | Hanwella (Kelani Ganga) | 4.40 | 🟢 Normal | -0.052 |  |
| 2026-05-27 01:03:57 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.054 |  |
| 2026-05-27 01:05:43 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.058 |  |
| 2026-05-27 01:06:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2026-05-27 01:04:01 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.078 |  |
| 2026-05-27 01:02:32 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)