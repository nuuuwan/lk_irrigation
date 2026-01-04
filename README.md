# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_12:10:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,394 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 12:10:48 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-01-04 12:10:21 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-01-04 12:08:31 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-01-04 12:08:29 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.028 |  |
| 2026-01-04 12:07:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-04 12:06:43 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-01-04 12:06:39 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.049 |  |
| 2026-01-04 12:05:59 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:05:34 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:05:27 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-04 12:05:23 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-04 12:05:21 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-04 12:05:11 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2026-01-04 12:04:57 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-01-04 12:04:53 | Galgamuwa (Mee Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:04:00 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:03:41 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:03:40 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.094 |  |
| 2026-01-04 12:03:38 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:03:23 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:02:59 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:52 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-01-04 12:02:51 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:02:49 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-01-04 12:02:47 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.095 |  |
| 2026-01-04 12:02:43 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:39 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:02:30 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:20 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:11 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-01-04 12:01:54 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:01:24 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:01:20 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:01:12 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.077 |  |
| 2026-01-04 12:01:07 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:00:52 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:00:46 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 12:07:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-04 12:05:23 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-04 12:05:21 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-04 12:00:46 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-04 12:05:34 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:03:41 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:02:51 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:02:39 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:01:24 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:01:54 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:04:00 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:05:11 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:05:59 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:03:23 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:01:07 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:10:21 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-01-04 12:06:43 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-01-04 12:04:57 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-01-04 12:03:38 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:04:53 | Galgamuwa (Mee Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:59 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:20 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:43 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:01:20 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:30 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:00:52 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.010 |  |
| 2026-01-04 12:02:52 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-01-04 12:02:11 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-01-04 12:05:27 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-01-04 12:02:49 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-01-04 12:08:29 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.028 |  |
| 2026-01-04 12:10:48 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-01-04 12:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2026-01-04 12:08:31 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-01-04 12:06:39 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.049 |  |
| 2026-01-04 12:01:12 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.077 |  |
| 2026-01-04 12:03:40 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.094 |  |
| 2026-01-04 12:02:47 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)