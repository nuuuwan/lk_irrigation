# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_12:11:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,869 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 12:11:29 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-02-23 12:09:02 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-02-23 12:08:32 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-02-23 12:08:27 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-02-23 12:06:58 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.083 |  |
| 2026-02-23 12:06:25 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-23 12:06:08 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.038 |  |
| 2026-02-23 12:06:01 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.064 |  |
| 2026-02-23 12:05:59 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.035 |  |
| 2026-02-23 12:05:55 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.036 |  |
| 2026-02-23 12:05:46 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.118 |  |
| 2026-02-23 12:04:57 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-23 12:04:46 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:04:13 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:04:03 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:04:01 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:03:54 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.067 |  |
| 2026-02-23 12:03:50 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-02-23 12:03:49 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.005 |  |
| 2026-02-23 12:03:48 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-23 12:03:39 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:03:18 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.220 |  |
| 2026-02-23 12:03:17 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-02-23 12:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:03:04 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:02:57 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.078 |  |
| 2026-02-23 12:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.099 |  |
| 2026-02-23 12:02:48 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.030 |  |
| 2026-02-23 12:02:43 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:02:39 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-02-23 12:02:39 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:02:37 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 12:02:31 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.011 |  |
| 2026-02-23 12:02:17 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:02:03 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:01:50 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:01:26 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 12:01:08 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-02-23 12:00:45 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-02-23 12:00:20 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 12:09:02 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-02-23 12:06:25 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-23 12:03:48 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-23 12:00:20 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 12:01:26 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 12:02:37 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 12:03:49 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.005 |  |
| 2026-02-23 12:04:46 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:01:50 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:03:04 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:03:09 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:02:03 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:02:17 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:04:01 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:02:39 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:02:43 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:04:13 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:03:39 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 12:11:29 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-02-23 12:08:32 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-02-23 12:02:39 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-02-23 12:04:57 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-23 12:00:45 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-02-23 12:02:31 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.011 |  |
| 2026-02-23 12:08:27 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-02-23 12:03:17 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-02-23 12:03:50 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-02-23 12:01:08 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-02-23 12:02:48 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.030 |  |
| 2026-02-23 12:05:59 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.035 |  |
| 2026-02-23 12:05:55 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.036 |  |
| 2026-02-23 12:06:08 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.038 |  |
| 2026-02-23 12:06:01 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.064 |  |
| 2026-02-23 12:03:54 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.067 |  |
| 2026-02-23 12:02:57 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.078 |  |
| 2026-02-23 12:06:58 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.083 |  |
| 2026-02-23 12:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.099 |  |
| 2026-02-23 12:05:46 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.118 |  |
| 2026-02-23 12:03:18 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.220 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)