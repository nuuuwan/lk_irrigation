# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_14:17:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,852 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 14:17:14 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:16:26 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.033 |  |
| 2026-01-10 14:15:27 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-10 14:14:34 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-10 14:13:19 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.018 |  |
| 2026-01-10 14:11:06 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:10:34 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-01-10 14:08:57 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:08:14 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:06:39 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.148 |  |
| 2026-01-10 14:05:52 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:05:26 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:05:22 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-10 14:05:18 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:05:01 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:04:56 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:04:41 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:04:05 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:03:54 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:03:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-10 14:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-01-10 14:03:28 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:03:24 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:03:13 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:03:01 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:52 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:26 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:25 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:18 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:02:16 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.033 |  |
| 2026-01-10 14:02:15 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-01-10 14:02:13 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 14:02:12 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:08 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-01-10 14:01:57 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:01:36 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:01:28 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:01:18 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 14:03:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-10 14:05:22 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-10 14:15:27 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-10 14:02:13 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 14:03:01 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:05:18 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:01:18 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:03:54 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:05:26 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:12 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:08:57 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:05:52 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:03:13 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:25 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:04:05 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:04:41 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:04:56 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:08:14 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:52 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:05:01 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:11:06 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:17:14 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:02:26 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 14:10:34 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-01-10 14:01:36 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:01:57 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:02:18 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:01:28 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:03:24 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:03:28 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.010 |  |
| 2026-01-10 14:14:34 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-10 14:02:15 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-01-10 14:13:19 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.018 |  |
| 2026-01-10 14:02:08 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-01-10 14:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-01-10 14:02:16 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.033 |  |
| 2026-01-10 14:16:26 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.033 |  |
| 2026-01-10 14:06:39 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)