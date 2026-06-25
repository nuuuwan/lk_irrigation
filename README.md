# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_13:18:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,009 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 13:18:57 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:13:37 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:13:27 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.037 |  |
| 2026-06-25 13:11:58 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:10:48 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-25 13:09:46 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:08:14 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:08:04 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:07:29 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:07:08 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 13:07:04 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 13:06:17 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-06-25 13:06:09 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:05:40 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:05:37 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:05:35 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:05:09 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:04:49 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 13:04:28 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:04:00 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:03:48 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.144 |  |
| 2026-06-25 13:03:44 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:03:33 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-06-25 13:03:09 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 13:02:57 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:02:30 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:02:30 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.061 |  |
| 2026-06-25 13:02:19 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:02:09 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 13:02:08 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 13:01:25 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.011 |  |
| 2026-06-25 13:01:20 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:01:16 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |
| 2026-06-25 13:01:00 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:00:49 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:00:20 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 13:06:17 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-06-25 13:03:09 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-25 13:02:09 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-25 13:07:08 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 13:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 13:04:49 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 13:07:04 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-25 13:10:48 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-25 13:02:30 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:01:00 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 12:03:52 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:18:57 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-25 12:01:27 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:11:58 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:13:37 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:09:46 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:07:29 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:02:19 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:02:57 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:00:49 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:05:37 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:04:00 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:05:40 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:08:04 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:02:30 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:02:08 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-25 13:08:14 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:05:09 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:06:09 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:04:28 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:01:20 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:03:44 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-25 13:01:25 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.011 |  |
| 2026-06-25 13:00:20 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.015 |  |
| 2026-06-25 13:01:16 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |
| 2026-06-25 13:03:33 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-06-25 13:13:27 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.037 |  |
| 2026-06-25 13:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.061 |  |
| 2026-06-25 13:03:48 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)