# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_12:11:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,372 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 12:11:19 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.105 |  |
| 2026-06-21 12:09:33 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:09:14 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:08:59 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-06-21 12:08:30 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:07:25 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.052 |  |
| 2026-06-21 12:06:47 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:06:30 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:06:12 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 12:06:04 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:05:32 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:05:25 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:05:13 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:05:06 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:05:00 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:04:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-06-21 12:04:31 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:04:23 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:04:08 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:03:56 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.078 |  |
| 2026-06-21 12:03:51 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 12:03:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-06-21 12:03:06 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.021 |  |
| 2026-06-21 12:03:00 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:03:00 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | -0.020 |  |
| 2026-06-21 12:02:46 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.031 |  |
| 2026-06-21 12:02:40 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.052 |  |
| 2026-06-21 12:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-21 12:02:31 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:02:21 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:02:11 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:02:04 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:51 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 12:01:45 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:42 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:29 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:00:16 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 12:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-21 12:01:51 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 12:03:51 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 12:06:12 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 12:00:16 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:02:21 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:45 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:08:30 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:05:32 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:05:25 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:05:00 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:06:47 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:03:00 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:09:33 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:04:08 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:05:06 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:01:42 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:02:04 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:02:11 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:06:30 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:09:14 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:02:31 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 12:05:13 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:06:04 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:04:23 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:01:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:01:29 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-21 12:03:00 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | -0.020 |  |
| 2026-06-21 12:08:59 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-06-21 12:03:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-06-21 12:03:06 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.021 |  |
| 2026-06-21 12:02:46 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.031 |  |
| 2026-06-21 12:04:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-06-21 12:02:40 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.052 |  |
| 2026-06-21 12:07:25 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.052 |  |
| 2026-06-21 12:03:56 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.078 |  |
| 2026-06-21 12:11:19 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)