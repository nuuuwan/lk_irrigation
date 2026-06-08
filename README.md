# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_17:36:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,973 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 17:36:21 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:15:20 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:11:15 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.018 |  |
| 2026-06-08 17:10:45 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.070 |  |
| 2026-06-08 17:08:32 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-08 17:07:43 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:07:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:07:22 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.020 |  |
| 2026-06-08 17:06:58 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 17:06:42 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:06:32 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-08 17:06:22 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.010 |  |
| 2026-06-08 17:06:03 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:05:08 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.014 |  |
| 2026-06-08 17:04:58 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-06-08 17:04:48 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:04:47 | Nawalapitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-06-08 17:04:41 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.042 |  |
| 2026-06-08 17:04:09 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:03:49 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-06-08 17:03:34 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-06-08 17:03:33 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-08 17:03:31 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:03:12 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.676 |  |
| 2026-06-08 17:03:07 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 17:02:58 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:02:57 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:02:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-08 17:02:16 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:02:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.030 |  |
| 2026-06-08 17:02:09 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 17:01:57 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.093 |  |
| 2026-06-08 17:01:47 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:01:39 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 17:01:03 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:00:48 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:00:35 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:00:35 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:00:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-08 16:59:39 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.676 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 17:04:47 | Nawalapitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-06-08 17:03:49 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-06-08 17:06:32 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-08 17:00:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-08 17:08:32 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-08 17:03:33 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-08 17:06:58 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 17:02:09 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 17:01:39 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 17:03:07 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 17:02:58 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:07:43 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:02:57 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:00:35 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:15:20 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:04:09 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:06:42 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:04:48 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:00:35 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:07:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:01:47 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:02:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:01:03 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:36:21 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:06:03 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:00:48 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:02:16 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 17:06:22 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.010 |  |
| 2026-06-08 17:02:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-08 17:03:34 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-06-08 17:05:08 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.014 |  |
| 2026-06-08 17:11:15 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.018 |  |
| 2026-06-08 17:04:58 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-06-08 17:07:22 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.020 |  |
| 2026-06-08 17:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.030 |  |
| 2026-06-08 17:04:41 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.042 |  |
| 2026-06-08 17:10:45 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.070 |  |
| 2026-06-08 17:01:57 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.093 |  |
| 2026-06-08 17:03:12 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.676 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)