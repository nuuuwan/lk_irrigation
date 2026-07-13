# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_01:17:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,567 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 01:17:19 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.008 |  |
| 2026-07-14 01:12:13 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:11:32 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-14 01:10:17 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:08:44 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:08:25 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:07:52 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-14 01:07:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:07:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:06:59 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:06:35 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:06:12 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-14 01:06:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-14 01:05:57 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-07-14 01:05:17 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:05:01 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:04:33 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:04:15 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:02:36 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:02:35 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.060 |  |
| 2026-07-14 01:02:24 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-14 01:02:19 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.070 |  |
| 2026-07-14 01:02:11 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-07-14 01:02:04 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:00:55 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 01:00:34 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:00:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:52:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:52:26 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 01:02:24 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-14 01:06:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-14 01:06:12 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-14 01:07:52 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-14 01:00:55 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 01:05:01 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:12 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:04:15 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:00:33 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:38 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:19:36 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:06:35 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:02:36 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:05:17 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:12:13 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:10:17 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:02:04 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:52:26 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:00:41 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:07:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:08:44 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:04 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:00:34 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:06:59 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:08:25 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:04:33 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:17:19 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.008 |  |
| 2026-07-14 01:11:32 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-14 01:05:57 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-07-14 01:02:11 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-07-13 22:06:18 | Putupaula (Kalu Ganga) | 0.14 | 🟢 Normal | -0.018 |  |
| 2026-07-13 21:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.024 |  |
| 2026-07-14 01:02:35 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.060 |  |
| 2026-07-13 18:03:05 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.067 |  |
| 2026-07-14 01:02:19 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.070 |  |
| 2026-07-14 00:02:52 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)