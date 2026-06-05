# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_02:23:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 02:23:46 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-06 02:23:26 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-06 02:18:05 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.028 |  |
| 2026-06-06 02:12:02 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.094 |  |
| 2026-06-06 02:09:19 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.005 |  |
| 2026-06-06 02:08:47 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-06 02:07:45 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:07:25 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:07:20 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.039 |  |
| 2026-06-06 02:07:02 | Glencourse (Kelani Ganga) | 11.92 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-06 02:06:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:04:42 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.151 |  |
| 2026-06-06 02:04:36 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-06-06 02:04:19 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-06-06 02:04:03 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-06 02:03:48 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 02:03:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-06 02:03:10 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:02:45 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:02:39 | Dunamale (Aththanagalu Oya) | 3.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 02:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | 0.571 | 🔺 Rising |
| 2026-06-06 02:02:24 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.061 |  |
| 2026-06-06 02:01:34 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-06 02:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | 0.571 | 🔺 Rising |
| 2026-06-06 02:01:15 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | -0.010 |  |
| 2026-06-06 02:01:10 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 01:35:57 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.079 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 02:23:46 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-06 02:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | 0.571 | 🔺 Rising |
| 2026-06-06 02:04:36 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-06-06 02:07:02 | Glencourse (Kelani Ganga) | 11.92 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-06 02:08:47 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-06 02:03:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-06 02:02:39 | Dunamale (Aththanagalu Oya) | 3.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 01:21:23 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-06 02:03:48 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 02:06:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:57:06 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:02:45 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 01:07:03 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:03:10 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-06 01:09:28 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:01:10 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:07:45 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-06 01:06:50 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:07:25 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:02:24 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-06 01:05:55 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 01:12:42 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-06 02:09:19 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.005 |  |
| 2026-06-06 02:01:34 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-06 02:04:03 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-06 00:03:00 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-06-06 02:01:15 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | -0.010 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-06 02:04:19 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-06-06 01:08:00 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.023 |  |
| 2026-06-06 02:18:05 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.028 |  |
| 2026-06-06 02:07:20 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.039 |  |
| 2026-06-06 02:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.061 |  |
| 2026-06-06 01:02:14 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.064 |  |
| 2026-06-06 01:35:57 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.079 |  |
| 2026-06-06 02:12:02 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.094 |  |
| 2026-06-06 02:04:42 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)