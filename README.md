# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_03:03:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,867 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 03:03:28 | Ellagawa (Kalu Ganga) | 9.28 | 🟢 Normal | -0.010 |  |
| 2026-05-25 03:03:26 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.114 |  |
| 2026-05-25 03:03:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:03:14 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:03:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:03:10 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 03:02:42 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:39 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:30 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:22 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:18 | Glencourse (Kelani Ganga) | 12.94 | 🟢 Normal | 0.764 | 🔺 Rising |
| 2026-05-25 03:02:18 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-05-25 03:02:03 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:01:39 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:01:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:00:35 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:00:13 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:50:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-25 02:39:28 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.114 |  |
| 2026-05-25 02:16:11 | Deraniyagala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.041 |  |
| 2026-05-25 02:14:55 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-05-25 02:13:05 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.077 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 02:14:55 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-05-25 01:05:49 | Putupaula (Kalu Ganga) | 3.24 | 🟡 Alert | 0.000 |  |
| 2026-05-25 00:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | -0.010 |  |
| 2026-05-25 03:02:18 | Glencourse (Kelani Ganga) | 12.94 | 🟢 Normal | 0.764 | 🔺 Rising |
| 2026-05-25 02:05:39 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-05-25 02:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-25 02:50:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-25 03:03:10 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:03:13 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:01:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:39 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:04:34 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:00:35 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:01:44 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:06:28 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:01:39 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:03:14 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:00:13 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:03 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:03:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:22 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:03:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-25 01:01:30 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-25 03:02:42 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 02:05:28 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.006 |  |
| 2026-05-25 02:08:23 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-05-25 03:03:28 | Ellagawa (Kalu Ganga) | 9.28 | 🟢 Normal | -0.010 |  |
| 2026-05-25 02:03:59 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-25 02:00:43 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-05-25 03:02:18 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-05-25 02:16:11 | Deraniyagala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.041 |  |
| 2026-05-25 02:07:27 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.049 |  |
| 2026-05-25 02:13:05 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.077 |  |
| 2026-05-25 03:03:26 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.114 |  |
| 2026-05-25 02:07:53 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)