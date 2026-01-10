# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_17:11:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,969 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 17:11:09 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-10 17:09:50 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-01-10 17:09:48 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:09:44 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:09:01 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-01-10 17:08:13 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:08:13 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:08:03 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 17:07:47 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:07:34 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:06:47 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.012 |  |
| 2026-01-10 17:06:36 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-10 17:06:16 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:05:48 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | -0.009 |  |
| 2026-01-10 17:05:03 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.076 |  |
| 2026-01-10 17:04:33 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:04:26 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:04:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 17:04:04 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:03:54 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:03:48 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.051 |  |
| 2026-01-10 17:03:43 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-01-10 17:03:38 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:03:20 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:03:11 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:03:04 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 17:02:39 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-10 17:02:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:02:00 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:01:50 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:01:38 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:01:35 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | -0.060 |  |
| 2026-01-10 17:01:30 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:01:15 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 17:01:11 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-01-10 17:00:45 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-01-10 17:00:44 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:00:34 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:19:54 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 16:19:09 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 17:06:36 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-10 17:02:39 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-10 17:04:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-10 17:11:09 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-10 17:01:15 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-10 17:03:04 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 17:08:03 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 17:02:31 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:09:44 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:02:00 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:03:54 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:06:16 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:08:13 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:03:20 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:04:33 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:01:38 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:08:13 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:04:26 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:03:38 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:00:44 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:07:34 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:07:47 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:00:34 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 17:05:48 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | -0.009 |  |
| 2026-01-10 17:09:50 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-01-10 17:09:01 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-01-10 17:04:04 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:03:11 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:01:50 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:01:30 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:09:48 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-10 17:00:45 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-01-10 17:06:47 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.012 |  |
| 2026-01-10 17:03:43 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.019 |  |
| 2026-01-10 17:01:11 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-01-10 17:03:48 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.051 |  |
| 2026-01-10 17:01:35 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | -0.060 |  |
| 2026-01-10 17:05:03 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)