# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_18:11:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,007 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 18:11:19 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:11:01 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:09:43 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:09:15 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:08:11 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:06:28 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:06:18 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:05:00 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:52 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:50 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:04:49 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-10 18:04:38 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:31 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:09 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:06 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:03:58 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-01-10 18:03:38 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-10 18:03:35 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-01-10 18:03:35 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:55 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-10 18:02:42 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:42 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 18:02:42 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:40 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.156 |  |
| 2026-01-10 18:02:28 | Horowpothana (Yan Oya) | 2.72 | 🟢 Normal | -0.011 |  |
| 2026-01-10 18:02:26 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:26 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-10 18:02:21 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:01:57 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:45 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:25 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 18:01:22 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:01:11 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.040 |  |
| 2026-01-10 18:00:41 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 18:04:31 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-10 18:01:45 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-10 17:02:39 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-10 18:04:49 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-10 18:02:26 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-10 18:03:38 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-10 18:01:25 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 18:02:42 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 18:01:57 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:26 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:52 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:42 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:22 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:08:11 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:09:43 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:05:00 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:06:28 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:08:13 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:06:18 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:09 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:03:35 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:38 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:55 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:02:42 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:11:19 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:01:35 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:04:06 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-10 18:03:58 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.009 |  |
| 2026-01-10 18:09:15 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:11:01 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:04:50 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:01:22 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-10 18:00:41 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-01-10 18:02:28 | Horowpothana (Yan Oya) | 2.72 | 🟢 Normal | -0.011 |  |
| 2026-01-10 18:02:45 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-10 18:01:11 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.040 |  |
| 2026-01-10 18:03:35 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-01-10 18:02:40 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)