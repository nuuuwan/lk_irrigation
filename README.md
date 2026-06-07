# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_22:11:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,255 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 22:11:01 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:09:25 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 22:09:19 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:08:38 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 22:07:50 | Rathnapura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.094 |  |
| 2026-06-07 22:07:41 | Magura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.105 |  |
| 2026-06-07 22:07:28 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 22:06:48 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-06-07 22:06:37 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-07 22:06:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:06:09 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:05:52 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 22:05:50 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 22:05:20 | Glencourse (Kelani Ganga) | 11.67 | 🟢 Normal | -0.041 |  |
| 2026-06-07 22:05:10 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:04:42 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-06-07 22:04:28 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-06-07 22:04:17 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:04:00 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:03:40 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:03:38 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:03:33 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.059 |  |
| 2026-06-07 22:03:27 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:03:25 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:03:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:02:43 | Putupaula (Kalu Ganga) | 1.84 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-07 22:02:29 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.040 |  |
| 2026-06-07 22:02:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.064 |  |
| 2026-06-07 22:02:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 22:01:48 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:01:31 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:01:06 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.021 |  |
| 2026-06-07 22:01:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:00:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:27:49 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:23:46 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 21:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-07 22:06:37 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-07 22:02:43 | Putupaula (Kalu Ganga) | 1.84 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-07 22:05:52 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 22:07:28 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 22:09:25 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 22:05:50 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 22:02:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 22:08:38 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-07 22:03:27 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:00:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:04:00 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:01:48 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:01:01 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:27:49 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:11:01 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:03:38 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:06:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:06:09 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:04:17 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:05:10 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:03:40 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:03:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:09:19 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:01:31 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:03:25 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-06-07 22:04:28 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-06-07 22:01:06 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.021 |  |
| 2026-06-07 22:04:42 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-06-07 22:06:48 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-06-07 22:02:29 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | -0.040 |  |
| 2026-06-07 22:05:20 | Glencourse (Kelani Ganga) | 11.67 | 🟢 Normal | -0.041 |  |
| 2026-06-07 22:03:33 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.059 |  |
| 2026-06-07 22:02:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.064 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-07 22:07:50 | Rathnapura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.094 |  |
| 2026-06-07 22:07:41 | Magura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)