# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_14:22:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,413 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 14:22:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:17:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:17:35 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:15:22 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:12:26 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:08:47 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.018 |  |
| 2026-01-14 14:08:44 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-01-14 14:08:28 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:08:23 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-01-14 14:07:26 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.126 |  |
| 2026-01-14 14:05:53 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-01-14 14:05:41 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:04:27 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:04:22 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-14 14:03:50 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 14:03:29 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-14 14:03:28 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-14 14:03:10 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-14 14:03:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-01-14 14:03:00 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:55 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:49 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-14 14:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:17 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:03 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:01 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-01-14 14:01:59 | Thanthirimale (Malwathu Oya) | 2.30 | 🟢 Normal | -0.031 |  |
| 2026-01-14 14:01:52 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:01:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 14:01:23 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-14 14:01:22 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:01:12 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:01:00 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:00:52 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:00:44 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:00:21 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.020 |  |
| 2026-01-14 13:54:19 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:35:19 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.018 |  |
| 2026-01-14 13:31:01 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 14:03:10 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-14 14:04:22 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-14 14:01:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 14:03:50 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 14:01:52 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:00:52 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:01:22 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:01:12 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:17:35 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:15:22 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:05:41 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:03:00 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:17 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:01:00 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:49 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:03 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:02:55 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:22:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 13:00:45 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:08:28 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:12:26 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:17:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:00:44 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:08:44 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-01-14 14:08:23 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-01-14 14:03:28 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-14 13:03:12 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-14 14:03:29 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-14 14:01:23 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-14 14:08:47 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.018 |  |
| 2026-01-14 14:00:21 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.020 |  |
| 2026-01-14 14:05:53 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-01-14 14:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-14 14:03:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-01-14 14:01:59 | Thanthirimale (Malwathu Oya) | 2.30 | 🟢 Normal | -0.031 |  |
| 2026-01-14 14:02:01 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-01-14 13:06:43 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | -0.048 |  |
| 2026-01-14 14:07:26 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)