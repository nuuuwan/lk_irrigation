# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_16:11:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,208 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 16:11:50 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.052 |  |
| 2026-02-21 16:08:44 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-02-21 16:08:29 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:08:25 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-21 16:07:43 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-02-21 16:06:43 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-21 16:06:27 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:06:23 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-02-21 16:06:02 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:05:39 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.018 |  |
| 2026-02-21 16:05:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:05:04 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:04:48 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-02-21 16:04:31 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:04:27 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -7.833 |  |
| 2026-02-21 16:04:14 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.085 |  |
| 2026-02-21 16:04:08 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 16:03:35 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.020 |  |
| 2026-02-21 16:03:28 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-21 16:03:27 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:03:23 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:03:20 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:03:15 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-02-21 16:03:07 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:02:36 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 16:02:30 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.041 |  |
| 2026-02-21 16:02:29 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:02:17 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-21 16:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-02-21 16:02:13 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-21 16:02:13 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.099 |  |
| 2026-02-21 16:02:12 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-21 16:01:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:01:51 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:01:46 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 16:01:43 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:01:26 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 16:03:15 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-02-21 16:06:23 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-02-21 16:02:12 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-02-21 16:06:43 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-21 16:08:25 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-21 16:02:13 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-21 16:01:46 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 16:04:08 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 16:02:36 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 16:01:43 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:06:02 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:04:31 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:06:27 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:01:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:03:27 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 15:13:14 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:03:23 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:01:51 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:03:20 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:03:07 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:08:29 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:05:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:05:04 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:02:29 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:01:26 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 16:08:44 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-02-21 16:07:43 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-02-21 16:03:28 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-21 16:02:17 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-21 16:05:39 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.018 |  |
| 2026-02-21 16:04:48 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.019 |  |
| 2026-02-21 16:03:35 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.020 |  |
| 2026-02-21 16:02:30 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.041 |  |
| 2026-02-21 16:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.25 | 🟢 Normal | -0.050 |  |
| 2026-02-21 16:11:50 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.052 |  |
| 2026-02-21 16:04:14 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.085 |  |
| 2026-02-21 16:02:13 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.099 |  |
| 2026-02-21 16:04:27 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -7.833 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)