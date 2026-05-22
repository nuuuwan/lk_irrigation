# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_22:35:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,111 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 22:35:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.143 | 🔺 Rising |
| 2026-05-22 22:33:34 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-22 22:29:01 | Dunamale (Aththanagalu Oya) | 5.16 | 🟠 Minor Flood | 0.007 | 🔺 Rising |
| 2026-05-22 22:14:18 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-22 22:12:05 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.037 |  |
| 2026-05-22 22:08:13 | Hanwella (Kelani Ganga) | 7.98 | 🟡 Alert | -0.050 |  |
| 2026-05-22 22:07:55 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.045 |  |
| 2026-05-22 22:07:55 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | -0.030 |  |
| 2026-05-22 22:07:48 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-05-22 22:06:53 | Glencourse (Kelani Ganga) | 14.34 | 🟢 Normal | -0.162 |  |
| 2026-05-22 22:06:26 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.058 |  |
| 2026-05-22 22:05:52 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.074 |  |
| 2026-05-22 22:05:21 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-22 22:05:12 | Rathnapura (Kalu Ganga) | 7.11 | 🟡 Alert | -0.098 |  |
| 2026-05-22 22:04:55 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-05-22 22:04:51 | Ellagawa (Kalu Ganga) | 9.60 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-22 22:04:45 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-05-22 22:04:36 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-05-22 22:03:57 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.021 |  |
| 2026-05-22 22:03:46 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:03:10 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-22 22:03:05 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-22 22:02:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:02:22 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-22 22:02:14 | Badalgama (Maha Oya) | 3.75 | 🟢 Normal | -0.033 |  |
| 2026-05-22 22:02:03 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.014 |  |
| 2026-05-22 22:02:01 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:01:28 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:01:28 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-22 22:01:15 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-05-22 22:01:01 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 22:00:54 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 1.017 | 🔺 Rising |
| 2026-05-22 22:00:09 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 22:29:01 | Dunamale (Aththanagalu Oya) | 5.16 | 🟠 Minor Flood | 0.007 | 🔺 Rising |
| 2026-05-22 22:35:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.143 | 🔺 Rising |
| 2026-05-22 22:03:57 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.021 |  |
| 2026-05-22 22:07:55 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | -0.030 |  |
| 2026-05-22 22:08:13 | Hanwella (Kelani Ganga) | 7.98 | 🟡 Alert | -0.050 |  |
| 2026-05-22 22:05:12 | Rathnapura (Kalu Ganga) | 7.11 | 🟡 Alert | -0.098 |  |
| 2026-05-22 22:00:54 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 1.017 | 🔺 Rising |
| 2026-05-22 22:04:51 | Ellagawa (Kalu Ganga) | 9.60 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-22 22:14:18 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-22 22:03:05 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-22 22:33:34 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-22 22:01:01 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 22:00:09 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:03:46 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:10:34 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:02:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:01:28 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:01:15 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:02:01 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:05:21 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-22 22:01:28 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-22 22:03:10 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-22 22:02:22 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-22 22:02:03 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.014 |  |
| 2026-05-22 22:07:48 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-05-22 22:04:36 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-05-22 22:04:45 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-05-22 22:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-05-22 20:05:10 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-22 22:04:55 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-22 22:02:14 | Badalgama (Maha Oya) | 3.75 | 🟢 Normal | -0.033 |  |
| 2026-05-22 22:12:05 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.037 |  |
| 2026-05-22 22:07:55 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.045 |  |
| 2026-05-22 22:06:26 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.058 |  |
| 2026-05-22 22:05:52 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.074 |  |
| 2026-05-22 22:06:53 | Glencourse (Kelani Ganga) | 14.34 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)