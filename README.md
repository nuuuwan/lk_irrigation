# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_13:14:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 13:14:56 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:13:46 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:13:26 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.086 |  |
| 2026-01-04 13:11:48 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.027 |  |
| 2026-01-04 13:11:19 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:10:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-04 13:09:23 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-01-04 13:08:44 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:06:58 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:06:20 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-04 13:05:13 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.067 |  |
| 2026-01-04 13:04:43 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:04:40 | Galgamuwa (Mee Oya) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-01-04 13:04:28 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-04 13:04:07 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:04:01 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-04 13:03:59 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.105 |  |
| 2026-01-04 13:03:58 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:03:51 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.045 |  |
| 2026-01-04 13:03:43 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:03:28 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-01-04 13:03:27 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:03:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-04 13:03:05 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-01-04 13:02:54 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:02:53 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:02:53 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-04 13:02:07 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:02:04 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:02:03 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:01:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:01:30 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-04 13:01:10 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:01:02 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-01-04 13:00:56 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:00:53 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 13:03:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-04 13:10:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-04 13:01:30 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-04 13:02:03 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:02:54 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:02:07 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:14:56 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:03:27 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:04:43 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:13:46 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:01:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:01:10 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:06:58 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:03:43 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:02:53 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:00:56 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:02:04 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:04:07 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:00:53 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-04 12:01:07 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:11:19 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:03:58 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-04 13:09:23 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-01-04 13:04:28 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-04 13:06:20 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-04 13:03:05 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-01-04 13:04:01 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-04 13:03:28 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-01-04 13:02:53 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-01-04 13:01:02 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-01-04 13:11:48 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.027 |  |
| 2026-01-04 12:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.029 |  |
| 2026-01-04 13:04:40 | Galgamuwa (Mee Oya) | 2.56 | 🟢 Normal | -0.030 |  |
| 2026-01-04 13:03:51 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.045 |  |
| 2026-01-04 12:06:39 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.049 |  |
| 2026-01-04 13:05:13 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.067 |  |
| 2026-01-04 13:13:26 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.086 |  |
| 2026-01-04 13:03:59 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)