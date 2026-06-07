# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_21:27:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,221 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 21:27:49 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:23:46 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:10:12 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-06-07 21:09:54 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 21:07:46 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-07 21:07:39 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:06:46 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.068 |  |
| 2026-06-07 21:06:44 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-07 21:06:09 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-06-07 21:06:07 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.014 |  |
| 2026-06-07 21:06:02 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 21:06:00 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:05:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.092 |  |
| 2026-06-07 21:05:00 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.011 |  |
| 2026-06-07 21:04:51 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.043 |  |
| 2026-06-07 21:04:50 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.061 |  |
| 2026-06-07 21:04:49 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:04:47 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:04:34 | Magura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.161 |  |
| 2026-06-07 21:04:31 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 21:04:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:03:57 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.094 |  |
| 2026-06-07 21:03:44 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:03:41 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:03:03 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:02:49 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 21:02:47 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:02:46 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:02:23 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-06-07 21:02:19 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.070 |  |
| 2026-06-07 21:02:14 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.042 |  |
| 2026-06-07 21:02:10 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 21:01:55 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:01:45 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 21:01:08 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 21:00:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 21:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-07 21:02:10 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 21:07:46 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-07 21:09:54 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 21:01:45 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 21:01:08 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 21:06:02 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 21:02:49 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 21:04:31 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 21:03:41 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:04:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:06:44 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:02:47 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:03:03 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:07:39 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:00:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:27:49 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:04:49 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:03:44 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:02:46 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:04:47 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:06:00 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:01:55 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 21:05:00 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -0.011 |  |
| 2026-06-07 21:06:07 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.014 |  |
| 2026-06-07 21:02:23 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-06-07 21:10:12 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-06-07 21:06:09 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-06-07 21:02:14 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.042 |  |
| 2026-06-07 21:04:51 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.043 |  |
| 2026-06-07 21:04:50 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.061 |  |
| 2026-06-07 21:06:46 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.068 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-07 21:02:19 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.070 |  |
| 2026-06-07 21:05:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.092 |  |
| 2026-06-07 21:03:57 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.094 |  |
| 2026-06-07 21:04:34 | Magura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)